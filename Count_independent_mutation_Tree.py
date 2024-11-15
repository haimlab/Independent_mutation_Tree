import newick
import os

# Global Variables Initialization

global reversions
global total_mutation 
global independent_mutation
global used_names

used_names =[]
total_mutation = 0
independent_mutation = 0
reversion_ratio = 0

total_mutation = 0
independent_mutation = 0

reversion_ratio = 0


def files_of_name_in_dir(in_path,file_extension):

    files = os.listdir(in_path)

    files = [f for f in files if os.path.isfile(in_path +'/'+f)]

    files = [f for f in files if f.split(".")[-1].upper() == file_extension.upper()]

    files.sort()

    return(files)

# Helper function to count occurrences of an element in a list
def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count

# Helper function to count nodes in a Newick formatted tree
def count_leaves(node):
    if len(node.descendants) <= 0:
        return 1
    else:
        sum = 0
        for child in node.descendants:
            sum += count_leaves(child)
        return sum


# Check if a string can be converted to a float
def is_float(string):
    if string.replace(".", "").isnumeric():
        return True
    else:
        return False

# Function to read and parse a Newick tree using the 'newick' library
def tree(input_file):
    f = open(input_file, "r")
    data = newick.read(input_file)
    f.close

    return data

# Recursively process the tree to track mutations at each node
def recursive_tree_search(input_tree,Name_list):

    global total_mutation, independent_mutation, reversion_ratio, used_names

    working_tree = input_tree
    tree_name = input_tree[0].name
    data_list = []

    node_list = working_tree[0].descendants

    for node in node_list:
        data_list.append(recursive_tree_search([node],Name_list))

    if len(Name_list) == 1:
        return []
    Name = Name_list.pop(0).strip('"[],')
    used_names.append(Name)
    if Name in Data_dict:
        raw_data = Data_dict[Name]
        sublist = separate_list_by_markers(raw_data,'[',']')
        data = [sublist[1][0].split(',')[site].strip().strip(' "'),sublist[0][0].split(',')[site].strip().strip(' "')]
    else:
        data = "none found"

    for codon in data_list:
        if codon[1] == data[1]:
            pass
            if data[0] != base_sequence:
                pass
        else:
            independent_mutation.append(codon[1])

    return data
    
# Split a list into sublists based on two markers (used to process JSON-like structures)    
def separate_list_by_markers(input_list,marker1,marker2):
    sublists = []
    sublist = []  
    for item in input_list:
        if item[-1] == marker1:
            sublist = []
        elif item[0] == marker2:
            sublists.append(sublist)
        else:
            item = item.strip('"[],')
            sublist.append(item)
    
    return sublists

# Function to parse a SLAC (Statistical Likelihood Analysis of Codon Substitution) file
def codon_library(slac_file):
    f = open(slac_file, "r")
    data = f.read()
    lines = data.splitlines()
    f.close
    for line in lines:
        print_list = line.split()
        for item in print_list:
            item1 = item.strip(',"}{:[]')
            if len(item1) < 1:
                print_list.remove(item)
            else:
                print_list[print_list.index(item)] = item1.strip("'").strip(',"}{:[]')

# Function to read lines between two markers in a file
def read_lines_between_markers(file_path, start_marker, end_marker):
    lines = []
    start_found = False

    with open(file_path, 'r') as file:
        for line in file:
            if start_marker in line:
                start_found = True
                continue
            elif end_marker in line:
                break
            elif start_found:
                if len(line.strip()) > 1 or '},' in line:
                    lines.append(line.strip())

    return lines

# Create a dictionary from a list of data (used for parsing key-value pairs)
def create_dictionary_from_list(data_list):
    result_dict = {}
    current_key = None
    current_values = []

    for item in data_list:
        if item.endswith(":{"):

            # Extract key from the item
            current_key = str(item[:-2]).strip('"[],')
            current_values = []
        elif current_key and "}" in item:

            # Extract values between current key and "},"
            values = item.split("},")[0]
            current_values.append(values)
            while("" in current_values):
                current_values.remove("")
            result_dict[current_key] = current_values
            current_key = None
        elif current_key:
            # Append values if not reaching "},"
            current_values.append(item)

    return result_dict

# Print values for each key in the dictionary (useful for debugging or displaying data)
def print_values_for_keys(dictionary, keys_list):
    for key in keys_list:
        if key in dictionary:
            print("Values for key '{}':".format(key))

# Main function to process each group in a specific clade and track mutations
def main():
    global Data_dict
    file_path = input_jason 
    start_marker = "branch attributes"
    end_marker = "data partitions"
    
    lines_between_markers = read_lines_between_markers(file_path, start_marker, end_marker)
    
    if lines_between_markers:
        Data_dict_pre = create_dictionary_from_list(lines_between_markers)

    Name_list = read_lines_between_markers(file_path,"NAMES","RESOLVED")


    Data_dict = {}

    for Name in  Name_list:
        name = Name.strip('"[],')
        if name in Data_dict_pre:
            Data_dict[name] = Data_dict_pre[name]

    total_sequence_number = len(Name_list)-1

    amino_acid_expression_list = []
    for Name in Data_dict:
        raw_data = Data_dict[Name]
        sublist = separate_list_by_markers(raw_data,'[',']')
        data = [sublist[1][0].split(',')[site].strip().strip(' "'),sublist[0][0].split(',')[site].strip().strip(' "')]
        amino_acid_expression_list.append(data[-1])

        from config import clade_consensus as con

        with open(con,"r") as f:
            con = list(f)[1]

        count_amino = countX(amino_acid_expression_list,con[site])

    if count_amino > len(amino_acid_expression_list) /2:
        recursive_tree_search(tree(input_tree),Name_list)
        return True
    else:
        return False


if __name__ == '__main__':

    global clade


    #============== Change the clade Here
    from config import clade as clade
    #====================================

    # Initialize the output file name
    Out_file_name = f"Clade_{clade}_Count_independent_mutation.txt"

    # Clear the output file (prepare for writing)
    with open(Out_file_name,"w") as f:
        f.write("")

    # Select the group list (e.g., clade B)

    #===================================
    from config import Slac_data as Slac_data
    input_folder = Slac_data
    listOfFiles = files_of_name_in_dir(input_folder,"json")
    group_list = [n.split(".")[0] for n in listOfFiles]
    #====================================

    # Initialize HXCB2 for mutation analysis

    from config import HXCB2 as HXCB2

    with open(HXCB2,"r") as f:
        HXCB2 = list(f)[1].strip("\n")

    # Iterate through sites and process mutation analysis
    site_list = []
    for index,char in enumerate(HXCB2):
        site_list.append([index+1,char,"AAA"])
        print([index+1,char,"AAA"])
    for site_pos in site_list:
        group_amino_count_list = []
        print(f"Site_{site_pos[0]}_{HXCB2[site_pos[0]-1]}")
        for in_number in group_list:

            # Generate paths to input files based on the group
            

            input_jason = f'{input_folder}/{in_number}.json'
            input_tree = f'{input_folder}/{in_number}.new'

    
            total_leafs = in_number 
            group_amino_count_list.append([total_leafs])

            print(f"Group {in_number}")

            # Perform mutation analysis for each group
            base_sequence = site_pos[2]
            Amino_acid = site_pos[1]
            site = site_pos[0]
            adjust = 1
            site = site - adjust

            # Reset mutation tracking variables
            reversions = 0
            total_mutation = 0
            independent_mutation = []

            # Run the main function
            main_boole = main()

            # Process results for amino acid counts
            Amino_acid_list = ["A","C","D","E","F","G","H","I","K","L","M","N","P","Q","R","S","T","V","W","Y"]
            
            total_leafs = count_leaves(tree(input_tree)[0])-1

            for Amino in Amino_acid_list:
                if main_boole:
                    group_amino_count_list[-1].append(countX(independent_mutation,Amino)/total_leafs)
                else:
                    group_amino_count_list[-1].append("-")

        # Write the mutation analysis results to the output file
        print(Out_file_name)
        with open(Out_file_name,"a") as f:
            f.write(f'\n')
            f.write(f'\n')
            f.write(f'\n')
            for index in range(len(group_amino_count_list[0])):
                header = [f"Site_{site_pos[0]}_{HXCB2[site_pos[0]-1]}"] + Amino_acid_list
                f.write(f"{header[index]}\t")
                for item in group_amino_count_list:
                    f.write(f'{item[index]}\t')
                f.write(f'\n')

