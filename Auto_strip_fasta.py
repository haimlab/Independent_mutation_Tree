import os

def strip_fasta(input_file):
    Data_list = []
    with open(input_file , "r") as file:
        index = 0
        file = list(file)
        for line in file:
            line_list = line
            if ">" in line_list:
                Data_list.append([])
                if ">Con" in line.split():
                    index = len(Data_list)-1
            line = line.strip()
            for sec in line.split():
                Data_list[-1].append(sec)
        out_pop = Data_list.pop(index)
        Data_list.insert(0,out_pop)
    
    return Data_list
if __name__ == '__main__':
    infile = "Input_files/Con_amino_B_lin.fa"


    string = strip_fasta(infile)

    print(string[0] == string[1])