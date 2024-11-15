import os

def files_of_name_in_dir(in_path,file_extension):

    files = os.listdir(in_path)

    files = [f for f in files if os.path.isfile(in_path +'/'+f)]

    files = [f for f in files if f.split(".")[-1].upper() == file_extension.upper()]

    return(files)

def run_strip_line(Mafft_In,Consensus_mapped_reference_out_path,extensions):

    print("A3_Strip_endline")

    file_list = files_of_name_in_dir(Mafft_In,extensions)

    print(file_list)

    for file_name in file_list:

        input_file = os.path.join(Mafft_In,file_name)

        print(input_file)

        Data_list = []

        with open(input_file , "r") as file:
            index = 0
            file = list(file)
            for line in file:
                line_list = list(line)
                if ">" in line_list:
                    Data_list.append([])
                    if ">Con" in line.split():
                        index = len(Data_list)-1
                line = line.strip()
                Data_list[-1].append(line)
            print(index)
            out_pop = Data_list.pop(index)
            Data_list.insert(0,out_pop) 

        out_file_name = os.path.join(Consensus_mapped_reference_out_path,"strip_"+ str(file_name))

        print(out_file_name)

        with open(out_file_name,'w') as file:
            for line in Data_list:
                file.write(line[0] + "\t")
                for char in line[1:]:
                    file.write(char)
                file.write("\n")

            file.close()

        print(out_file_name)

if __name__ == '__main__':
    # Input and output paths
    #=============================================================
    reference_in_path = "strip_reference"
    reference_out_path = "strip_reference_Out"
    File_extension = "fa"
    #=============================================================

    run_strip_line(reference_in_path,reference_out_path,File_extension)

