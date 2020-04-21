# COVID Molecules

### ** The contents of this repository website are for research and educational purposes only. **

This repository contains a crowd sourced list of molecules derived from literature and other sources to aid computational screenings for molecules that have been screened experimentally or computationally against coronaviruses (SARS,MERS, SARS-CoV-2).

## Data Structure
`literature_molecules.csv` - A csv file with headers ["molecule", "virus", "reference", "type", "smiles", "pubchem_id", "similarity_calculated", "release"]
* molecule - the name of the molecule (best effort)
* virus - the virus the molecule was screened against (SARS, MERS, SARS-CoV-2)
* reference - the reference from which the information was collected
* type - the type of screening performed ["computational","experimental","mixed"]
* smiles - The oBabel canonical SMILES as retrieved from pubchem
* pubchem_id - The PubChem ID of the molecule if available
* similarity_calculated - `1` if similarities have been calculated to other databases, `0` otherwise
* release - The first release in which the row of information was available

Note that similarities will be calculated to the databases available from the The [nCov-Group Data Repository](https://2019-ncovgroup.github.io/data/), and made available in future releases.

`references.csv` - A line delimited set of references that have been surveyed to arrive at the results

## Updates
`v0.9 (2020-04-21)` - initial availability
* 


# Acknowledgements
Yadu Nand Babuji, Ben Blaiszik, Kyle Chard, Ryan Chard, Ian Foster, India Gordon, Zhi Hong, Kasia Karbarz, Zhuozhao Li, Linda Novak, Susan Sarvey, Marcus Schwarting, Julie Smagacz,Logan Ward, Monica Orozco White

Data storage and computational support for this research project has been generously supported by the following resources. The data generated have been prepared as part of the nCov-Group Collaboration, a group of over 200 researchers working to use computational techniques to address various challenges associated with COVID-19.

**[Petrel Data Service](https://press3.mcs.anl.gov/petrel/) at the Argonne Leadership Computing Facility (ALCF)**
This research used resources of the Argonne Leadership Computing Facility, a DOE Office of Science User Facility supported under Contract DE-AC02-06CH11357.

**[Argonne Leadership Computing Facility (ALCF)](https://www.alcf.anl.gov)**
This research used resources of the Argonne Leadership Computing Facility, a DOE Office of Science User Facility supported under Contract DE-AC02-06CH11357.

**[Frontera at the Texas Advanced Computing Center (TACC)](https://www.tacc.utexas.edu)**

**[Comet at the San Diego Supercomputing Center (SDSC)](https://www.sdsc.edu)**


**Data and Computing Infrastructure**
Many aspects of the data and computing infrastructure have been leveraged from other projects including but not limited to:

Data processing and computation:
 * ExaLearn and the <a href="https://www.exascaleproject.org">Exascale Computing Project</a>
 * <a href="https://parsl-project.org">Parsl</a>: parallel scripting libarary (NSF 1550588)
 * <a href="https://www.funcx.org">funcX</a>: distributed function as a service platform (NSF 2004894)

Data Tools, Services, and Expertise:
 * <a href="https://www.globus.org">Globus</a>: data services for science (authentication, transfer, users, and groups) 
 * <a href="https://chimad.northwestern.edu">CHiMaD</a>: <a href="https://materialsdatafacility.org">Materials Data Facility </a> and <a href="http://pppdb.uchicago.edu">Polymer Property Predictor Database</a> (NIST 70NANB19H005 and NIST 70NANB14H012)


# How to Contribute
*** Under Construction ***

