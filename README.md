File Compression Project

Overview

This project implements a simple file compression algorithm using a predefined mapping of characters to binary numbers. 

The project consists of two main scripts:

code.py: Compresses a text file into a binary format based on the provided character-to-binary mapping.

decode.py: Decompresses the binary file back into the original text using the binary-to-character mapping.

Project Files

- code.py: Script to compress text files.

- decode.py: Script to decompress binary files back to text.

- Table.xlsx: Excel file containing the character-to-binary mappings.

- list.txt: Sample text file to be compressed.

- BinOutput.txt: Output file containing the compressed binary data.

- TextOutput.txt: Output file containing the decompressed text.


Character-to-Binary Mapping


The character-to-binary mapping is defined in the Table.xlsx file. Here is a sample of the mapping:

<img width="161" alt="Untitled" src="https://github.com/aichaa30/File_Compression-/assets/114168218/4ba6334c-5997-405b-97b4-5b082c25207e">


Encoding Text


To encode a text file, run the code.py script: python code.py

This will read the list.txt file, compress its content based on the mappings, and output the binary data to BinOutput.txt.

Decoding Binary


To decode a binary file, run the decode.py script: python decode.py

This will read the BinOutput.txt file, decompress its content based on the mappings, and output the original text to TextOutput.txt.

How It Works

Loading the Character Mapping:

- The loadSheet function reads the Table.xlsx file and creates dictionaries for character-to-binary and binary-to-character mappings.

Encoding Process:

- The Code function reads the input text file (list.txt), converts each character or word to its corresponding binary representation, and writes the result to BinOutput.txt.

Decoding Process:

- The Decode function reads the binary data from BinOutput.txt, converts each binary sequence back to its corresponding character or word, and writes the result to TextOutput.txt.
