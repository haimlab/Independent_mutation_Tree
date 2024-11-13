# Import necessary libraries
import re
import os

# Read the root sequence from the file
def read_root_sequence(Root_sequence_path):
    with open(Root_sequence_path,"r") as f:
        file_list = list(f)
        sequence = file_list[0].strip("/n") + "\n"
        for line in file_list[1:]:
            sequence += line.strip("/n")
        
        return sequence

# Function to check if a string can be converted to a float
def is_float(string):
    if string.replace(".", "").isnumeric():
        return True
    else:
        return False
    
# Function to get a list of files in a directory (only files, not directories)    
def files_of_name_in_dir(in_path):

    files = os.listdir(in_path)

    files = [f for f in files if os.path.isfile(in_path +'/'+f)]

    files = [f for f in files ]

    return(files)

def main(input_folders,Root_sequence_path,input_amion_acid,out_folders,fasta_type):
    # Get the list of files in the input folder
    file_list = files_of_name_in_dir(input_folders)


    Root_sequence = read_root_sequence(Root_sequence_path)

    # Get the list of files in the input folder
    for file in file_list:
        Out_put = "Out_put_group.fa"

        # Construct the full path of the input group file
        input_Group = input_folders +"/" + file

        # Read the group file to extract leaf names from the tree string
        with open(input_Group,"r") as f:
            tree_string = list(f)[0]
            leafs = re.split(r"[\( \), \-!?]+",tree_string)
            while '' in leafs:
                leafs.remove('')
            new_leafs = []
            for n in leafs:
                n = n.split(':')[0]
                n = n.split('/')[0]
                if not is_float(n):
                    new_leafs.append(n)
            while '' in new_leafs:
                new_leafs.remove('')

        Out_list = [] # List to store sequences that match the leaves

        # Read the amino acid sequence file and match sequences with the leaf names
        with open(input_amion_acid,"r") as f:
            file_list = list(f) # Read all lines of the amino acid sequence file
            dic = {} # Dictionary to store sequence for each leaf

            # Loop through the lines in the sequence file
            for line in file_list:

                # Split the line to get the sequence name (first element)
                sequence_name = line.split()
                
                # Extract the accession number from the sequence name
                ascension_number = sequence_name[0].strip(">")
                ascension_number = ascension_number.split('/')[0]
                ascension_number = ascension_number.split()[0]
                print("sequence_name",ascension_number )
                ascension_number = ascension_number.split('.')[-1]

                # If the accession number is found in the leaf list, store the sequence
                if ascension_number in new_leafs:
                    dic[ascension_number] = line # Map the accession number to the sequence line
                    Out_list.append(line) # Append the sequence to the output list

        # Construct the output file path with the group file name
        Out_put = out_folders +"/"+ file + fasta_type + "_" + Out_put 
        print(Out_put)
        
        # Write the matched sequences to the output file
        with open(Out_put,"w") as f: 
            for line in new_leafs: # For each leaf in the new leaf list
                # Write the sequence in FASTA format
                f.write(f">{line}\n")
                f.write(f"{dic[line].split()[1]}\n")

            # Write the root sequence at the end of the file
            f.write(f"{Root_sequence.split()[0]}\n")
            f.write(f"{Root_sequence.split()[-1]}\n")

if __name__ == '__main__':


    # Input and output paths
    #=============================================================
    input_amion_acid = "Input_files/strip_CladeB_AminoAcid_HXBC2(2535).fa"
    input_Nucleotide = "Input_files/strip_CladeB_Nucleotide_HXBC2(2535).fa"
    input_folders = "1_Clade_B"
    Amino_Root_sequence_path = "Input_files/Con_amino_B_lin.fa"
    nucleotide_Root_sequence_path = "Input_files/Con_nuc_B_lin.fa"
    out_folders = "2_Clade_B"
    file_extension_nwk = "_amino"
    file_extension_nuc = "_nuc"
    #=============================================================


    main(input_folders,Amino_Root_sequence_path,input_amion_acid,out_folders,file_extension_nwk)
    main(input_folders,nucleotide_Root_sequence_path ,input_Nucleotide,out_folders,file_extension_nuc)