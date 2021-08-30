import xml.etree.ElementTree as ET
import os
os.system("srcml simple_demo.cpp -o input.xml")
os.system("srcml simple_demo.cpp -o input.txt")

tree = ET.parse('input.xml')
root = tree.getroot()

f = open("input.txt")
data = f.readlines()


def handle_block_str(line):
    n = line.find("</block_content>")
    if(n!=-1):
        return "O(1)"


    line = line[line.index('>')+1 : ]
    line = line[line.index('>')+1 : ]
    line = line.strip()
    if(len(line)==0):
        return "O(1)"
    
    # TODO : add handling of other statements

def handle_expr_stmt_str(line):
    n = line.find("<call>")
    if(n==-1):
        return "O(1)"

    # TODO : add handling of other statements

def handle_function_str(line):
    # TODO : store the name of the function and parameters in a global list
    return "O(1)"

i=0
for line in data:
    
    line = line.strip()
    if(line==""):
        i+=1
        continue
    tag = line[line.index('<')+1 : line.index('>')]
    if(i>0):
        print(i, end=" ")
    else:
        i=1
        continue
        
    if(tag == "block" or tag == "/block_content"):
        print(handle_block_str(line))
    elif(tag == "expr_stmt"):
        print(handle_expr_stmt_str(line))
    elif(tag == "function"):
        print(handle_function_str(line))
    else:
        print("O(1)")
    
    i+=1
    #TODO : add for statements, if statements, function calls



