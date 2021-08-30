from bs4 import BeautifulSoup
with open('recursion.xml', 'r') as f:
    data = f.read()

Bs_data = BeautifulSoup(data, "xml")
b_function = Bs_data.find_all('call')
print(b_function)