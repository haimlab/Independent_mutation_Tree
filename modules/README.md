

### Step 1: Grouping Sequences 

<!-- Script: *1_Tree_group.py* -->

**Inputs:**

input_tree: Newick tree file (e.g., B_rooted_2535.NWK) 

out_folder: Output folder for groups (e.g., 1_Clade_B) 

max_group_size: Maximum number of sequences per group (e.g., 150) 
This script divides the phylogenetic tree (from the Newick file) into smaller groups, each containing no more than 150 sequences. 

### Step 2: Splitting FASTA Files by Group 

Script: *2_Split_fasta_by_group.py*

**Inputs:**

input_amino_acid: FASTA file with amino acid sequences (e.g., strip_CladeB_AminoAcid_HXBC2(2535).fa) 

input_nucleotide: FASTA file with nucleotide sequences (e.g., strip_CladeB_Nucleotide_HXBC2(2535).fa) 

input_folders: Folder containing sequence groups (e.g., 1_Clade_B) 

Amino_Root_sequence_path: FASTA file with the amino acid consensus sequence (e.g., Con_amino_B_lin.fa) 

Nucleotide_Root_sequence_path: FASTA file with the nucleotide consensus sequence (e.g., Con_nuc_B_lin.fa) 

out_folders: Folder to store Amino acid output files (e.g., 2_Clade_B) 

out_folders: Folder to store nucleotide output files (e.g., 3_Clade_B) 

This script generates a striped FASTA files for each file in the input folder. Striped Fasta files have the sequance on the same line as the name. 

### Step 3: Generating and Rerooting Trees 

Script: *step_3_Strip_endline.py*

Inputs: 

in_folder: Folder containing the processed FASTA files (e.g., 3_Clade_B) 

out_folders: Folder to store output files (e.g., 4_Clade_B) 

This script generates two separate FASTA files for each group (one for amino acids, one for nucleotides). The consensus sequence is appended to both files. 

### Step 4: Prepare Nucleotide Data for SLAC 

Script: *4_by_codon_list.py*

Inputs: 

in_folder: Folder containing the processed FASTA files (e.g., 4_Clade_B) 

out_file: Folder where the cleaned FASTA files for SLAC will be saved (e.g., 5_Clade_B) 

Description: 
Before running SLAC (Selective DNA Substitution Analysis), nucleotide sequences need to be cleaned of stop codons, as SLAC cannot process sequences containing stop codons. 

Script Functionality: 
The script 4_by_codon_list.py scans the input nucleotide FASTA files and replaces any stop codons with three gap characters to prepare them for SLAC analysis. 