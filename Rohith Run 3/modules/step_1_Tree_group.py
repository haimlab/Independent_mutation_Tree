# Import necessary modules
import newick # To work with Newick format trees
import re # Regular expressions for text processing
import os.path # File path manipulations

class glob_var():
    # Global variable to store the output list
    def __init__(self, tree_search,out_folder):
        self.out_list = []
        self.leaves_to_prune = []
        self.out_folder = out_folder
        self.tree_search = tree_search

# Function to check if a string represents a float
def is_float(string):
    if string.replace(".", "").isnumeric():
        return True
    else:
        return False

# Function to read a Newick tree from a file and return it
def tree(input_file):
    trees = newick.read(input_file)
    return trees

# Function to compute the total length of a tree, including its descendants
def get_tree_length(input_tree):

    # Get the descendants (subtrees) of the input tree
    descendants = input_tree.descendants

    # Extract the distance (length) from the Newick string representation
    distance = newick.dumps(input_tree).split(":")[-1].strip(";").strip("'")
    length = float(distance.strip(";"))
    max_length = 0
    for nodes in descendants:
        returned_length = get_tree_length(nodes)
        max_length = max(max_length,returned_length)

    out_length = length + max_length
    return out_length

# Function to count the number of nodes in the tree
def count_nodes(input_tree):
    # Convert the tree to its Newick string representation
    tree_string = newick.dumps(input_tree)

    # Convert the tree string to a list of characters
    lst = list(tree_string)

     # Initialize count for opening parentheses (nodes)
    x = "("
    count = 1

    # Loop through each character in the list and count the opening parentheses
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count

# Function to recursively search the tree and split groups
def recursive_tree_search(input_tree,max_group_size,glob,min_group_size):

    # Declare global variables for search and pruning
    
    recursive = True

    # If the tree has fewer than max_group_size leaf nodes, start pruning
    if min_group_size < count_nodes(input_tree) < max_group_size:

        # Create a unique file name based on the number of nodes in the tree
        f_name = glob.out_folder + "/" + str(count_nodes(input_tree)) + "-0"

        # If the file already exists, increment the filename number
        while os.path.isfile(f_name):
            f_name = f_name.split("-")[0] + "-" + str(int(f_name.split("-")[-1])+1)

        # Create an empty file with the generated name
        with open(f_name,"w") as f:
            f.close()

        # Write the Newick tree to the file
        newick.write(input_tree, f_name)

        # Open the file in append mode to finalize the operation
        with open(f_name,"a") as f:
            f.close()
            recursive = False # No further recursion needed for this tree

            # Convert the tree to a Newick string and split it into leaves (nodes)
            tree_string = newick.dumps(input_tree)
            leafs = re.split(r"[\( \), \-!?]+",tree_string)

            # Remove any empty strings from the list
            while '' in leafs:
                leafs.remove('')

            new_leafs = []
            # Process each leaf to remove any leaf that is a float (i.e., a distance value)
            for n in leafs:
                n = n.split(':')[0] # Take only the name, ignoring the distance
                if not is_float(n): # Only add non-numeric names to new_leafs
                    new_leafs.append(n)

            # Add the names of leaves to prune to the global list
            glob.leaves_to_prune += new_leafs

            # Prune the tree by removing the identified leaves
            glob.tree_search.prune_by_names(new_leafs)

    # Recursively process all descendants of the current tree
    if recursive:
        descendants = input_tree.descendants
        for nodes in descendants:
            recursive_tree_search(nodes,max_group_size,glob,min_group_size) # Recursively prune each descendant tree


if __name__ == '__main__':

    #============== Input file path for the tree in Newick format
    input_tree = 'Input_files/B_rooted_2535.NWK'

    # Output folder where results will be saved
    out_folder = "1_Clade_B"

    # Input max group size
    max_group_size = 150
    min_group_size = 80
    #=============================================================

    trees = tree(input_tree)

    descendants = trees[0].descendants

    n = str(trees[0].descendants[0].name)
    n = "0.01"


    glob = glob_var(trees[0],out_folder)
    tree_search = glob.tree_search
    recursive_tree_search(tree_search,max_group_size,glob,min_group_size)