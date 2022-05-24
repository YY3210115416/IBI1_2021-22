import numpy as np
from xml.dom.minidom import parse as parse
import xml.dom.minidom
import matplotlib.pyplot as plt

#the number of terms:47340
file=parse("go_obo.xml")
root=file.documentElement
term=root.getElementsByTagName("term")
number=len(term)
print("The number of terms:",number) 

ID=[]
for i in range (0,len(term)):
    id_text=term.item(i).getElementsByTagName("id")[0].childNodes[0]
    ID.append(id_text.data)
    
nodes_number1=[]
def child_nodes(node,term,ID,count_base=0):
    global nodes_number1
    sub_node=node.getElementsByTagName("is_a")
    if sub_node!=None:
        count_base=count_base+len(sub_node)
        #print(count_base)
        for i in range (0,len(sub_node)):
            j = ID.index(sub_node[i].childNodes[0].data)
            if j <= len(nodes_number1)-1:
                count_base = count_base + nodes_number1[j] + 1
            else:
                node=term.item(j)
                count_base = child_nodes(node,term,ID,count_base)
    return count_base
            
nodes_number2=[]
for i in range(0,len(term)):
    node=term.item(i)
    def_node=node.getElementsByTagName("def").item(0)
    def_str_text=def_node.getElementsByTagName("defstr")[0].childNodes[0].data
    sub_node_number=child_nodes(node, term, ID)
    if "translation" in def_str_text:
        nodes_number2.append(sub_node_number)
    nodes_number1.append(sub_node_number)

#boxplot1    
plt.boxplot(nodes_number1)
plt.title("Distribution of the number of childnodes in each term")
plt.ylabel("Number of child nodes")
plt.show()
#boxplot2 
plt.boxplot(nodes_number2)
plt.title("Distribution of the number of childnodes in each term with gene expression")
plt.ylabel("Number of child nodes")
plt.show()

if np.average(np.array(nodes_number1))>np.average(np.array(nodes_number2)):
    print("The translation terms contain a smaller number of child nodes.")
else:
    print("The translation terms contain a greater number of child nodes.")
# The translation terms contain a greater number of child nodes than the overall Gene Ontology on average.