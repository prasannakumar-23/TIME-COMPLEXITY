
import xml.etree.ElementTree as ET
import os
os.system("srcml simple_demo.cpp -o input.xml")
os.system("srcml simple_demo.cpp -o input.txt")
tree = ET.parse('for_and_while.xml')
root = tree.getroot()

f = open("input.txt")
data = f.readlines()
# print(root.tag)
# print(root.attrib)
functions_list=[]
for_list =[]
complexity_at_point=""

class Method:
    def __init__(self, type ="void", name = "null" , parameters = [], complexity = "", block=None):
        self.name = name
        self.type = type
        self.parameters = parameters
        self.complexity = complexity
        self.block = block
    


def handle_block(block, comp, method_name):
    block_content = block[0]
    for children in block_content:
        tag = str(children.tag)
        tag = tag[tag.index('}')+1 : ] 
        # print(tag, "block", "function " + method_name)   
        if(tag=="if_stmt"):
            handle_if_stmt(children, comp, method_name)   
        if(tag=="for"):
            handle_for(children, comp, method_name) 
    #TODO: add more statements
        


def handle_func(func,comp):
    method = Method()
    method.complexity=""
    method.parameters=[]
    method.block=None
    for children in func:
        tag = str(children.tag)
        tag = tag[tag.index('}')+1 : ]
        # print(tag , "inside function")
        if tag=='type':
            method.type = children[0].text
        elif tag=="name":
            method.name = children.text
        elif tag=="parameter_list":
            parameter_list = children
            j=0       
            while(j<len(parameter_list)):                   
                method.parameters.append([parameter_list[j][0][0][0].text, parameter_list[j][0][1].text])
                #this is giving us data type and name of the variable
                j+=1            
        elif tag=='block':
            method.block=children
            handle_block(children, comp, method.name)
    functions_list.append(method)
    # print(method.type, method.name, method.parameters, method.complexity)

def handle_if_stmt(if_stmt, comp, method_name):
    for children in if_stmt:
        tag = str(children.tag)
        tag = tag[tag.index('}')+1 : ]
        if(tag=="if"):
            handle_if(children,comp, method_name)
        elif(tag=="else"):
            handle_else(children,comp, method_name)

def handle_if(if_, comp, method_name):
    # TODO: write for if
    condition = if_[0]
    for call in condition.iter("{http://www.srcML.org/srcML/src}call"):
        
        print(call[0].text, "Found a function call")

    block =if_[1]
    handle_block(block, comp,method_name)


        
    # for children in if_:
    #     tag = str(children.tag)
    #     tag = tag[tag.index('}')+1 : ]

def handle_else(else_, comp, method_name):
    #TODO: write for else
    block = else_[0]
    handle_block(block,comp, method_name)

def handle_control(control, comp, method_name):
    
    increment = control[2]
    increment =increment[0] # points to expr
    exp1 =""
    op1=""
    for children in increment:
        if children.tag == "{http://www.srcML.org/srcML/src}operator" and children.text != "=":
            op1 = op1 +children.text
        exp1 = exp1 +children.text
    
    exp1 = exp1[exp1.find(op1):]
    exp1 =exp1[len(op1):] # op contains the operator and exp is the value
    
    exp2=""
    op2=""
    condition = control[1]
    condition=condition[0]
    for children in condition:
        if children.tag == "{http://www.srcML.org/srcML/src}operator" and children.text != "+" and children.text != "-" and children.text != "*" and children.text != "/":
            op2 = op2 +children.text
        exp2 = exp2 +children.text
    
    exp2 = exp2[exp2.find(op2):]
    exp2 =exp2[len(op2):] # op contains the operator and exp is the value

    exp3=""
    op3=""
    initial = control[0]
    initial=initial[0]
    for children in initial:
        if children.tag == "{http://www.srcML.org/srcML/src}operator" and children.text == "=":
            op3 = op3 +children.text
        exp3 = exp3 +children.text
    
    exp3 = exp3[exp3.find(op3):]
    exp3 =exp3[len(op3):] # op contains the operator and exp is the value
    print(op3, exp3, op2, exp2, op1, exp1)
    
    is_exp2_digit=True
    for character in exp2:
        if character.isalpha():
            is_exp2_digit=False
    is_exp3_digit=True
    for character in exp3:
        if character.isalpha():
            is_exp3_digit=False

    
    # print(is_exp2_digit, is_exp3_digit)
    if (not is_exp3_digit) or (not is_exp2_digit):
        if ((op1=="+=" and exp1.isdigit()) or op1=="++" or op1=="--" or (op1=="-=" and exp1.isdigit()) or (op1=="+" and exp1.isdigit()) or(op1=="-" and exp1.isdigit()) ):
            comp = "n"+comp
            print(comp)
            return comp
        if ((op1=="*=" and exp1.isdigit()) or  (op1=="/=" and exp1.isdigit()) or (op1=="*" and exp1.isdigit()) or (op1=="/" and exp1.isdigit())):
            comp = comp + "log(n)b(" + exp1 +")"
            print(comp)
            return comp
    print(comp)
    return comp
    





    # for ele in control.iter():
    #     if(ele.tag=="{http://www.srcML.org/srcML/src}condition" or ele.tag=="{http://www.srcML.org/srcML/src}incr"):
    #         exp = exp+";"
        
    #     if(ele.text):
    #         exp = exp + ele.text
    # exp = exp+")"
    # start= exp[exp.index("=")+1 : exp.index(";")]


    
def handle_for(for_, comp, method_name):
    control =for_[0]
    comp = handle_control(control, comp, method_name)
    
    block =for_[1]
    handle_block(block, comp, method_name)




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



for child in root:
    tag = str(child.tag)
    tag = tag[tag.index('}')+1 : ]
    print(tag)
    if( tag == 'function'):
        func = child
        handle_func(func, "")


    

        # print(func[1].text) # it will give you function name
        # print(func[0][0].text) # it will give you function return type
        
            
        
                        
            
        # print(parameter_list[0][0][1].text) # this gives you the name of the parameter
       
        
        
            

# print(root[2])
# for tags in root[2]:
#     print(tags.text,tags)






    
    
