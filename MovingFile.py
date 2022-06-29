#Moving of files

import os

#-----------------------------Fill this block---------------------------
source_path = ""           #Also add the format: example_file.xlsx
source_file_name = ""      #replace backslash with forward slash /
destination = ""           #Also add the format: example_file.xlsx
destination_file_name = ""
#----------------------------------------------------------------------






file_name = source_file_name
f_name = destination_file_name
source = f"{source_path}/{file_name}"
dst = f"{destination}/{f_name}"
if os.path.isfile(f"{source}"):
    try:
        os.rename(source, dst)
    except FileExistsError:
        os.remove(f"{destination}/{f_name}")
        os.rename(source, dst)
    finally:
        if os.path.isfile(f"{dst}"):
            print("Sucessful!")
else:
    print(f"{file_name} doesn't exist at {source_path}")
