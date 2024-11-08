# Import necessary modules
import newick # To work with Newick format trees
import re # Regular expressions for text processing
import os # File path manipulations

import step_1_Tree_group as step_1
import step_2_Split_fasta_by_group as step_2
import step_3_Strip_endline as Strip
import Step_4_by_codon_list as step_4

def run_step_0(folders_list):
    """Start Step 0 create empty folder"""

    step_on = 0

    print("Start Step 0 create empty folder")
    
    for folder in folders_list:
        if not os.path.isdir(folder):
            os.mkdir(folder)
            print(f"Added folder {folder}")

    print("End Step 0 create empty folder")

def run_step_1(input_tree,out_folder,max_group_size):

    trees = step_1.tree(input_tree)

    descendants = trees[0].descendants

    newick.write(trees, 'fname')

    n = str(trees[0].descendants[0].name)
    n = "0.01"


    glob = step_1.glob_var(trees[0],out_folder)
    tree_search = glob.tree_search
    step_1.recursive_tree_search(tree_search,max_group_size,glob)

def run_step_2(input_amion_acid,input_Nucleotide,input_folders,Amino_Root_sequence_path,nucleotide_Root_sequence_path,out_folders,file_extension_nwk,file_extension_nuc,step_2_out_folder_2):
    step_2.main(input_folders,Amino_Root_sequence_path,input_amion_acid,out_folders,file_extension_nwk)
    step_2.main(input_folders,nucleotide_Root_sequence_path ,input_Nucleotide,step_2_out_folder_2,file_extension_nuc)

def run_step_3(step_3_reference_in_path,step_3_out_path,step_3_File_extension):
    Strip.run_strip_line(step_3_reference_in_path,step_3_out_path,step_3_File_extension)

def main(folders_list,step_1_input_tree,step_1_out_folder,step_1_max_group_size,step_2_input_amion_acid,step_2_input_Nucleotide,step_2_input_folders,step_2_Amino_Root_sequence_path,step_2_nucleotide_Root_sequence_path,step_2_out_folders,step_2_file_extension_nwk,step_2_file_extension_nuc,step_2_out_folder_2,step_3_reference_in_path,step_3_out_path,step_3_File_extension,step_4_in_folder,step_4_out_file,step_4_extension):
    run_step_0(folders_list)
    run_step_1(step_1_input_tree,step_1_out_folder,step_1_max_group_size)
    run_step_2(step_2_input_amion_acid,step_2_input_Nucleotide,step_2_input_folders,step_2_Amino_Root_sequence_path,step_2_nucleotide_Root_sequence_path,step_2_out_folders,step_2_file_extension_nwk,step_2_file_extension_nuc,step_2_out_folder_2,)
    run_step_3(step_3_reference_in_path,step_3_out_path,step_3_File_extension)
    step_4.main(step_4_in_folder,step_4_out_file,step_4_extension)


if __name__ == '__main__':
    clade = "B"

    #============== Input file path for the tree in Newick format
    step_1_input_tree = 'Input_files/B_rooted_2535.NWK'

    # Output folder where results will be saved
    step_1_out_folder = "1_Clade_B"

    # Input max group size
    step_1_max_group_size = 150
    #=============================================================

        # Input and output paths
    #=============================================================
    step_2_input_amion_acid = "Input_files/strip_CladeB_AminoAcid_HXBC2(2535).fa"
    step_2_input_Nucleotide = "Input_files/strip_CladeB_Nucleotide_HXBC2(2535).fa"
    step_2_input_folders = "1_Clade_B"
    step_2_Amino_Root_sequence_path = "Input_files/Con_amino_B_lin.fa"
    step_2_nucleotide_Root_sequence_path = "Input_files/Con_nuc_B_lin.fa"
    step_2_out_folders = "2_Clade_B"
    step_2_file_extension_nwk = "_amino"
    step_2_file_extension_nuc = "_nuc"

    step_2_out_folder_2 = "3_Clade_B"
    #=============================================================

        # Input and output paths
    #=============================================================
    step_3_reference_in_path = "3_Clade_B"
    step_3_out_path = "4_Clade_B"
    step_3_File_extension = "fa"
    #=============================================================

        # Input and output paths
    #=============================================================
    step_4_in_folder = "4_Clade_B"
    step_4_out_file = "5_Clade_B"
    step_4_extension = "fa"
    #=============================================================
    

    folders_step_1 = f"1_Clade_{clade}"
    folders_step_2 = f"2_Clade_{clade}"
    folders_step_3 = f"3_Clade_{clade}"
    folders_step_4 = f"4_Clade_{clade}"
    folders_step_5 = f"5_Clade_{clade}"
    folders_step_6 = f"6_Clade_{clade}"

    folders_list = [folders_step_1,folders_step_2,folders_step_3,folders_step_4,folders_step_5,folders_step_6]
    main(folders_list,step_1_input_tree,step_1_out_folder,step_1_max_group_size,step_2_input_amion_acid,step_2_input_Nucleotide,step_2_input_folders,step_2_Amino_Root_sequence_path,step_2_nucleotide_Root_sequence_path,step_2_out_folders,step_2_file_extension_nwk,step_2_file_extension_nuc,step_2_out_folder_2,step_3_reference_in_path,step_3_out_path,step_3_File_extension,step_4_in_folder,step_4_out_file,step_4_extension)