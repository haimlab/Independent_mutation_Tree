import os
def files_of_name_in_dir(in_path,file_extension):

    files = os.listdir(in_path)

    files = [f for f in files if os.path.isfile(in_path +'/'+f)]

    files = [f for f in files if f.split(".")[-1].upper() == file_extension.upper()]

    return(files)


def main(in_folder,out_file,extension):
    cwd = os.getcwd()

    files = files_of_name_in_dir(in_folder,extension)



    for file in files:
        Data_list = []
        input_file = in_folder + "/" + file
        with open(input_file , "r") as f:
            file_list = list(f)

            for line in file_list:

                line = line.strip()
                line_split = line.split()
                Data_list.append([line_split[0],line_split[-1]])

        with open(f"{out_file}/{file}","w") as f:
            for index,i in enumerate(Data_list):
                y = i[-1].split()[-1]
                f.write(f"{i[0].split('/')[0]}\n")
                for x in range(0,len(y),3):
                    codon = y[x:x+3]
                    codon = codon.upper()
                    if "-" in codon or "N" in codon or (codon == "TAA") or (codon == "TAG") or (codon == "TGA"):
                        codon = "---"
                    f.write(f"{codon}")
                f.write("\n")
            f.close()
            
if __name__ == '__main__':
    in_folder = "4_Clade_B"
    out_file = "5_Clade_B"
    extension = "fa"
    main(in_folder,out_file,extension)