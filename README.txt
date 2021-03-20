Title: BLAST-Viewer
Author: Meghana Balasubramanian


About the program:

BLAST-Viewer is a web application designed to visualize the BLAST output generated from the command line in a more readable format using a web browser. The user can choose between different BLAST programs and databases available at NCBI or utilize their own database.


Installation:
The program is written in python and HTML and is combined together using Flask, and uses the following versions:
- Python 3.8.5
- pip 21.0.1

Install Flask using pip:
$ pip install Flask

Install Biopython using pip:
$ pip install biopython

Install BLAST+ executables using:
Depending on the environment utilized by the you, you may choose to download the software best suited for your environment from:
 	https://ftp.ncbi.nlm.nih.gov/blast/executables/LATEST/

Running the program:
The program can be run from the terminal as:
	python blast-viewer.py

Navigating to the link displayed, the user may input the following:
- Input sequence: Input a single DNA/RNA/amino acid sequence
- Type of sequence: FASTA/ FASTQ must be specified
- BLAST program to be used: Choose between 5 different BLAST programs
- Enter database: Should the user choose to use their own database, the exact name of the database must be written upon clicking the checkbox or use one of the existing databases
- Submit: Upload the sequences and direct you to the output page


Results:
The result generated is an alignment file which is downloaded to your working directory as outputhtml.xml. The alignment visaulization, however, can be viewed on the web page.














