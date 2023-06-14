# Embedded_Drivers_Genrator
a script to generate Drivers headers for Eclipse IDE
## Requirements:
Eclipse  Neon.3 Release (4.6.3) or higher

Python 3.8.8 or higher

## How To Install

To install the script to your Eclipse IDE, Follow these steps:

1- download the script to your system 

2-open External Tools Configuration

![image](https://github.com/abdallaragab/Embedded_Drivers_Generator/assets/53912540/9a438721-9cf2-481f-9f81-e725f3025102)

3-
in Location Field insert the location of your Python interpreter.
in working Directory insert the location where the Files_G.py file is saved in.

in Arguments Field insert:
 " Files_G.py ${resource_loc}\${resource_name} ${resource_name} "Default" "
 
you can replace Default parameter with the desired user Name ,otherwise the OS user Name is generated


![image](https://github.com/abdallaragab/Embedded_Drivers_Generator/assets/53912540/707cfaf9-6880-4110-b3ec-fc3b6a9f46ca)

4-
copy these Settings 

![image](https://github.com/abdallaragab/Embedded_Drivers_Generator/assets/53912540/f546604d-f3cd-42d4-a9f3-694772c93b36)


![image](https://github.com/abdallaragab/Embedded_Drivers_Generator/assets/53912540/bcfcad5d-02d2-4db6-b997-7daf64bfa893)


![image](https://github.com/abdallaragab/Embedded_Drivers_Generator/assets/53912540/53760a38-ea8e-4271-94e5-2b74cd0c654d)



## HOW TO USE:

1-Create a folder with the desired SWC Name
2- Choose that Folder in Project Explorer
3- Run the Tool from External Tools menu

![image](https://github.com/abdallaragab/Embedded_Drivers_Generator/assets/53912540/c28ce3f1-6e55-443c-b426-899144d10f71)



![image](https://github.com/abdallaragab/Embedded_Drivers_Generator/assets/53912540/67668254-a7a9-4615-973a-b2f862aa6601)







this code is written by Abdallah Ragab


