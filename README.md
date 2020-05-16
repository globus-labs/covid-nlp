# COVID Molecules

### ** The contents of this repository website are for research and educational purposes only. **

This repository contains a crowd sourced list of molecules derived from literature and other sources to aid computational screenings for molecules that have been screened experimentally or computationally against coronaviruses (SARS,MERS, SARS-CoV-2).

## Data Structure
`/LIT/LIT.csv` - A csv file with headers ["molecule", "virus", "reference", "type", "smiles", "pubchem_id", "similarity_calculated", "release"]
* molecule - the name of the molecule (best effort)
* virus - the virus the molecule was screened against (SARS, MERS, SARS-CoV-2)
* reference - the reference from which the information was collected
* type - the type of screening performed ["computational","experimental","mixed"]
* pubchem_smiles - The SMILES as retrieved from pubchem
* canonical_smiles - The oBabel canonical SMILES as computed from the pubchem SMILES
* pubchem_id - The PubChem ID of the molecule if available
* similarity_calculated - `1` if similarities have been calculated to other databases, `0` otherwise
* release - The current release associated with the row of information

Note that similarities will be calculated to molecules in the databases available from the The [nCov-Group Data Repository](https://2019-ncovgroup.github.io/data/), and made available in future releases.

`/LIT/references.csv` - A line delimited set of references that have been surveyed to arrive at the results

## Updates
`v0.1 (2020-04-21)` - initial availability

`v0.2 (2020-05-08)` - new molecules and inlude Pubchem and canonical SMILES


# Acknowledgements
Yadu Nand Babuji, Ben Blaiszik, Kyle Chard, Ryan Chard, Ian Foster, India Gordon, Zhi Hong, Kasia Karbarz, Zhuozhao Li, Linda Novak, Susan Sarvey, Marcus Schwarting, Julie Smagacz,Logan Ward, Monica Orozco White

Research was supported by the DOE Office of Science through the National Virtual Biotechnology Laboratory, a consortium of DOE national laboratories focused on response to COVID-19, with funding provided by the Coronavirus CARES Act.

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

# Disclaimer

## For All Information

Unless otherwise indicated, this information has been authored by an employee or employees of the UChicago Argonne, LLC., operator of the Argonne National laboratory with the U.S. Department of Energy. The U.S. Government has rights to use, reproduce, and distribute this information. The public may copy and use this information without charge, provided that this Notice and any statement of authorship are reproduced on all copies.

While every effort has been made to produce valid data, by using this data, User acknowledges that neither the Government nor UChicago Argonne LLC. makes any warranty, express or implied, of either the accuracy or completeness of this information or assumes any liability or responsibility for the use of this information. Additionally, this information is provided solely for research purposes and is not provided for purposes of offering medical advice. Accordingly, the U.S. Government and UChicago Argonne LLC. are not to be liable to any user for any loss or damage, whether in contract, tort (including negligence), breach of statutory duty, or otherwise, even if foreseeable, arising under or in connection with use of or reliance on the content displayed on this site.

For Scientific and Technical Information Only © Copyright UChicago Argonne LLC. All Rights Reserved.

