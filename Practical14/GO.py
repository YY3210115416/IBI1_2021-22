import xml.dom.minidom
from xml.dom.minidom import parse
import matplotlib.pyplot as plt
from numpy import*

DOMTree =parse("go_obo.xml")
collection = DOMTree.documentElement
terms= collection.getElementsByTagName("term")
number=len(terms)
print('the total number of terms:', number)

#For every term, put all parentNodes into a set.
dic={} #key：term id，value：direct parents id
def fun(direct_id,parent):
    pa_direct=dic[direct_id]#find direct parents id data 
    if len(pa_direct):#if have direct parents
        for j in pa_direct:#each direct parent put into a set called parent
            parent.add(j)
            fun(j,parent)#nest, find direct parent's parents until all are included

dic_number={} #key：term id，value：childNodes number
translation=[]
for term in terms:
    ids=term.getElementsByTagName('id')[0].childNodes[0].data#find term id
    direct_parents_id=[] # store direct parents
    for is_a in term.getElementsByTagName('is_a'):
        direct_parents_id.append(is_a.childNodes[0].data)#find term <is_a> id data
    dic[ids]= direct_parents_id
    dic_number[ids]=0
    if term.getElementsByTagName("defstr")[0].childNodes[0].data.find("translation"or"Translation")!=-1:
        translation.append("yes")
    else:
        translation.append("no")

# dic_result key ：term id， value：childNodes number
for key in dic.keys():
    parent=set()#one set for each term, containing the term's all parentNodes
    fun(key,parent)
# Parent term id's childnode number +1
    for k in parent:
        dic_number[k]+=1

average_list=[]
translation_number=[] #If a term is associated with translation, its childnodes number will be add to this list
for i,(k,v)in enumerate(dic_number.items()):
    average_list.append(v)
    if translation[i]=="yes":
        translation_number.append(v)
        
# draw the boxplot of all terms and terms related to translation
plt.boxplot(dic_number.values(),vert=True,whis=1.5,patch_artist=True,notch=False)
plt.title('Distribution of child nodes across terms in Gene Ontology')
plt.xlabel("all terms in Gene Ontology")
plt.ylabel('Child Nodes Number')
plt.show()

plt.boxplot(translation_number,vert=True,whis=1.5,patch_artist=True,notch=False)
plt.title('Distribution of child nodes across terms associated with translation')
plt.xlabel('terms related to translation')
plt.ylabel('Child Nodes Number')
plt.show()

#judge whether 'translation'terms contain more childNodes than overall GO
ave=mean(average_list)
ave_transition=mean(translation_number)
if ave>ave_transition:
    print("The translation terms contain, on average, a smaller number	of child nodes than the	overall	Gene Ontology.")
else:
    print("The translation terms contain, on average, a greater number	of child nodes than the	overall	Gene Ontology.")







