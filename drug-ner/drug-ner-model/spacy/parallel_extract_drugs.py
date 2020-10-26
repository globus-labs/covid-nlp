from multiprocessing import Process, cpu_count, Queue
from tqdm import tqdm
import pickle
import spacy
import sys
import os

Q = Queue()


def extract_drugs(pid: int, text: list, model: str):
    # os.sched_setaffinity(0, (pid,))
    counter = dict()
    nlp = spacy.load(model)
    for line in tqdm(text, ascii=True, desc=f"#{pid:2}", mininterval=1):
        line = line[:1000000] # Spacy length limit: 1M chars
        doc = nlp(line)
        for ent in doc.ents:
            s = ent.text.strip().lower()
            if s not in counter:
                counter[s] = 0
            counter[s] += 1 
    # counter = sorted(counter.items(), key=lambda item: item[1], reverse=True)
    # if outfile:
    #     with open(outfile, 'w') as fout:                
    #         for k, v in counter:
    #             fout.write(f"{k}|{v}\n")
    # else:
    #     for k, v in counter:
    #         print(f"{k}|{v}")
    
    # saving results to disk for the main process to read. This avoids overflowing the Queue
    temp_file = f"./tempdata_{pid}.pkl"
    with open(temp_file, 'wb') as f:
        pickle.dump(counter, f)
    Q.put(temp_file)
    Q.close()


# def test_extract_drugs(pid: int, text: list, model: str):
#     os.sched_setaffinity(0, (pid,))
#     counter = dict()
#     for i, s in enumerate(text):
#         counter[i] = s
#     Q.put(counter)


if __name__ == '__main__':
    model = sys.argv[1]
    infile = sys.argv[2]
    outfile = sys.argv[3]
    n_cpu = int(sys.argv[4])
    # n_cpu = cpu_count()
    print(f"# of CPUs: {n_cpu}")
    with open(infile) as f:
        text = f.read().splitlines()
        ps = list()
        for i in range(n_cpu):
            p = Process(target=extract_drugs, args=(
                i,
                text[len(text)*i//n_cpu:
                     (len(text)*(i+1)//n_cpu) if i < n_cpu-1 else None],
                model))
            ps.append(p)
            p.start()
        # Caution: Must read from Queue before join()!! Otherwise may deadlock.
        dicts = list()
        while len(dicts) < n_cpu:
            temp_file = Q.get(block=True)
            with open(temp_file, 'rb') as f:
                d = pickle.load(f)
            dicts.append(d)
        for p in ps:
            p.join()
    print("all joined!")
    
    print(f"Got {len(dicts)} dicts!")
    for i in range(1, n_cpu):
        print(f"Processing dict #{i}...")
        for k, v in tqdm(dicts[i].items(), ascii=True, desc=f"dict #{i}"):
            if k not in dicts[0]:
                dicts[0][k] = 0
            dicts[0][k] += v
    print("Start sorting...")
    counter = sorted(dicts[0].items(), key=lambda item: item[1], reverse=True)
    print("Start writing to file...")
    with open(outfile, 'w') as fout:
        for k, v in tqdm(counter, ascii=True):
            fout.write(f"{k}|{v}\n")
