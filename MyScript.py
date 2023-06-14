import os
import sys
import datetime

def create_file_guard(filename):
    # Remove any invalid characters from the string
    file_name = os.path.splitext(filename)[0]

    # Convert file name to upper case
    file_guard = file_name.upper()

    # Replace characters other than alphanumeric with underscores
    file_guard = ''.join(c if c.isalnum() else '_' for c in file_guard)

    return file_guard

def create_header_file(filename, file_guard):
    global file_name1
    if os.path.isfile(filename):
        print(filename+"    File Already exists.")
    else:
        with open(filename, 'w') as file:
            file.write("/*\n  * File:  "+filename.split("\\")[-1]+" \n *	SWC:    "+file_name1+"\n *	Version: 1.0 \n *  Created on: "+datetime.datetime.now().strftime("%d-%m-%Y")+" \n *  Author: Abdallah ragab \n */"  + "\n")
            file.write("#ifndef " + file_guard + "\n")
            file.write("#define " + file_guard + "\n\n")
            file.write("#endif // " + file_guard + "\n")
            file.close()


def create_C_file(filename):
    global file_name1
    if os.path.isfile(filename):
        print(filename+"    File Already exists.")
    else:
        with open(filename, 'w') as file:
            file.write("/*\n  * File:  "+filename.split("\\")[-1]+" \n *	SWC:    "+file_name1+"\n *	Version: 1.0 \n *  Created on: "+datetime.datetime.now().strftime("%d-%m-%Y")+" \n *  Author: Abdallah ragab \n */"  + "\n")
            file.close()

# Receive string from Eclipse
received_string = sys.argv[1]
file_name1=sys.argv[2]
print(sys.argv[1])

config_file_guard = create_file_guard(file_name1 + "_Config_H")
private_file_guard = create_file_guard(file_name1 + "_Private")
Interface_file_guard = create_file_guard(file_name1 + "_Interface")

create_header_file(sys.argv[1]+"_Config.h", config_file_guard)
create_header_file(sys.argv[1]+"_Private.h", private_file_guard)
create_header_file(sys.argv[1]+"_Interface.h", Interface_file_guard)
create_C_file(sys.argv[1]+"_Program.c")
