import newick

# Function to read and parse a Newick tree using the 'newick' library
def tree(input_file):
    f = open(input_file, "r")
    data = newick.read(input_file)
    f.close

    return data


def count_leaves(node):
    if len(node.descendants) <= 0:
        return 1
    else:
        sum = 0
        for child in node.descendants:
            sum += count_leaves(child)
        return sum

    


if __name__ == "__main__":
    group_list = [149,134,128,127,125,124,122,121,113,104,93,91,87,84]
    clade = "B"
    for in_number in group_list:
        input_tree = f'Clade_{clade}_Slac_data/{in_number}.new'
        # Specify the path to your Newick fil

        newick_file = tree(input_tree)[0]
        
        # Get the count of leaf nodes
        leaf_count = count_leaves(newick_file)
        
        print(f"Number of leaf nodes: {leaf_count}")
