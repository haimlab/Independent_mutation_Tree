Files: 

File_1: A Newick (.NWK) file containing the full phylogenetic tree. 
Example: B_rooted_2535.NWK 
File_2: A Striped FASTA file with the amino acid sequences for all taxa in the tree. 
Example: strip_CladeB_AminoAcid_HXBC2(2535).fa 
File_3: A StripedFASTA file with the nucleotide sequences for all taxa in the tree. 
Example: strip_CladeB_Nucleotide_HXBC2(2535).fa 
File_4: A FASTA file containing the amino acid consensus sequence for the clade. 
Example: Con_amino_B_lin.fa 
File_5: A FASTA file containing the nucleotide consensus sequence for the clade. 
Example: Con_nuc_B_lin.fa 
Script 1: 0_Strip_endline.py 

Inputs: 

reference_in_path: Path to the input FASTA files (e.g., strip_reference) 
reference_out_path: Path to output the processed files (e.g., strip_reference_Out) 
File_extension: File extension to match (e.g., .fa) 
This script Strips all files in the reference_in_path directory with the specified extension, removes unnecessary line breaks, and outputs the Striped files to reference_out_path. These new files have “strip_” added to the beginning of their name. 

Step 1: Grouping Sequences 

Script: 1_Tree_group.py 

Inputs: 

input_tree: Newick tree file (e.g., B_rooted_2535.NWK) 
out_folder: Output folder for groups (e.g., 1_Clade_B) 
max_group_size: Maximum number of sequences per group (e.g., 150) 
This script divides the phylogenetic tree (from the Newick file) into smaller groups, each containing no more than 150 sequences. 

Step 2: Splitting FASTA Files by Group 

Script: 2_Split_fasta_by_group.py 

Inputs: 

input_amino_acid: FASTA file with amino acid sequences (e.g., strip_CladeB_AminoAcid_HXBC2(2535).fa) 
input_nucleotide: FASTA file with nucleotide sequences (e.g., strip_CladeB_Nucleotide_HXBC2(2535).fa) 
input_folders: Folder containing sequence groups (e.g., 1_Clade_B) 
Amino_Root_sequence_path: FASTA file with the amino acid consensus sequence (e.g., Con_amino_B_lin.fa) 
Nucleotide_Root_sequence_path: FASTA file with the nucleotide consensus sequence (e.g., Con_nuc_B_lin.fa) 
out_folders: Folder to store output files (e.g., 2_Clade_B) 
This script generates two separate FASTA files for each group (one for amino acids, one for nucleotides). The consensus sequence is appended to both files. 

Step 3: Generating and Rerooting Trees 

For each group generated in Step 2 

Generate a phylogenetic tree: Use FastTree to build a tree from the amino acid or nucleotide sequences. 
Reroot the tree: Reroot the generated tree using the consensus sequence to ensure proper alignment. 
Step 4: Prepare Nucleotide Data for SLAC 

Script: 4_by_codon_list.py 

Inputs: 

in_folder: Folder containing the processed FASTA files (e.g., 4_Clade_B) 
out_file: Folder where the cleaned FASTA files for SLAC will be saved (e.g., 5_Clade_B) 
Description: 
Before running SLAC (Selective DNA Substitution Analysis), nucleotide sequences need to be cleaned of stop codons, as SLAC cannot process sequences containing stop codons. 

Script Functionality: 
The script 4_by_codon_list.py scans the input nucleotide FASTA files and replaces any stop codons with three gap characters to prepare them for SLAC analysis. 

Step 5: Generate SLAC Files 

For each group created in Step 2, follow these steps: 

Generate a FASTA file: Use the Newick tree produced in Step 3 and the nucleotide FASTA file generated in Step 4 to create a corresponding SLAC file. The Hyphy-Slac tool on Galaxy is recommended for this.  
Download SLAC files: Upload the Slac file to the  HyPhy Viewer website and retrieve the JSON and Newick files associated with each SLAC file from the HyPhy Viewer website. 
 

Step 6: Count Independent Mutations 

For each group created in Step 2, run the following script: 

Script: 6_Count_independent_mutation_Tree.py 

Inputs: 



 