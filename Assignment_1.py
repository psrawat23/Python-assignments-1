#Sort the list based on the top level domain (edu, com, org, in) using custom sorting
import re
url = ['www.annauniv.edu', 'www.google.com', 'www.ndtv.com', 'www.website.org','www.bis.org.in', 'www.rbi.org.in']
y=lambda x: list(reversed(x.split('.')))
print(sorted(url,key=y))

#2.	Given a list of strings, return the count of the number of strings where the string length is 2 or more and the first and last chars of the string are the same.  
x=['axa', 'xyz', 'gg', 'x', 'yyy']
y=['x', 'cd', 'cnc', 'kk']
z=['bab', 'ce', 'cba', 'syanora']
def strlen(str):
    count=0
    for i in str:
        if len(i)>=2 and i[0]==i[-1]:
            count+=1
    return count
print(strlen(x)) 
print(strlen(y)) 
print(strlen(z))

#return a list with the strings in sorted order, except group all the strings that begin with 'x' first
l=['mix', 'xyz', 'apple', 'xanadu', 'aardvark','xdfh'] 
l1=['bbb', 'ccc', 'axx','xaa','xzz']
l2=['mix', 'xyz', 'apple', 'xanadu', 'aardvark','xzz']

def strx(x):
    xstr=[]
    for str1 in x:
        print(x)
        if str1.startswith('x'):
            print(str1)
            x.remove(str1)
            xstr.append(str1)
    xstr=sorted(xstr)
    x=sorted(x) 
    xstr.extend(x)
    return xstr
print(strx(l))
print(strx(l1))
print(strx(l2))

#4.	Given a list of non-empty tuples, return a list sorted in increasing order by the last element in each tuple
tup=[(1, 7), (1, 3), (3, 4, 5), (2, 2)] 
tup1=[(1, 3), (3, 2), (2, 1)]
tup2=[(1, 7), (1, 3), (3, 4, 5), (2, 2)]

def sort(x):
    
    return x[-1]
print(sorted(tup,key=sort))
print(sorted(tup1,key=sort))
print(sorted(tup2,key=sort))

#5.	Given a list of numbers, return a list where all adjacent == elements have been reduced to a single element, so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or modify the passed in list.
l1= [1, 2, 2, 3]
l2= [2, 2, 3, 3, 3]
def unique(list1):
    list1=set(list1)
    return list(list1)
print(unique(l1))
print(unique(l2))

#6.	Write a function to print the information in the dictionary(bookstore) in the given format

bookstore={"New Arrivals":{"COOKING":["Everyday Italian","Giada De Laurentiis","2005","30.00"],
"CHILDREN":["Harry Potter”, J K. Rowling","2005","29.99"],"WEB":["Learning XML","Erik T. Ray","2003","39.95"]}}
def printvalue(bookstore):
  print(bookstore["New Arrivals"]["WEB"])
  print(bookstore["New Arrivals"]["COOKING"])
  print(bookstore["New Arrivals"]["CHILDREN"])
printvalue(bookstore)

#7 
str1="""Python is a widely used high-level programming language for
general-purpose programming, created by Guido van Rossum and first
released in 1991. An interpreted language, Python has a design 
philosophy which emphasizes code readability (notably using whitespace
indentation to delimit code blocks rather than curly braces or keywords),
and a syntax which allows programmers to express concepts in fewer lines 
of code than possible in languages such as C++ or Java. The language provides
constructs intended to enable writing clear programs on both a small and large
scale .Python features a dynamic type system and automatic memory management
and supports multiple programming paradigms, including object-oriented, 
imperative, functional programming, and procedural styles. It has a large and
comprehensive standard library. Python interpreters are available for 
many operating systems, allowing Python code to run on a wide variety of systems.
CPython, the reference implementation of Python, is open source software and has 
a community-based development model, as do nearly all of its variant implementations.
CPython is managed by the non-profit Python Software Foundation."""

str_list=str1.split()
dic={}
count=[]
for element in str_list:
    if element not in dic.keys():
        dic[element]=str_list.count(element)

dic=sorted(dic.items(),key=lambda value:(value[1],value[0]))
print(dic)
for x in list(reversed(list(dic)))[0:5]:
    print(x)


#8.	Given a string,
str1="""Python is a widely used high-level programming language
for general-purpose programming, created by Guido van Rossum and
first released in 1991. An interpreted language, Python has a 
design philosophy which emphasizes code readability (notably using 
whitespace indentation to delimit code blocks rather than curly braces
or keywords), and a syntax which allows programmers to express concepts 
in fewer lines of code than possible in languages such as C++ or Java. 
The language provides constructs intended to enable writing clear programs 
on both a small and large scale. Python features a dynamic type system and
automatic memory management and supports multiple programming paradigms,
including object-oriented, imperative, functional programming, and procedural
styles. It has a large and comprehensive standard library. Python interpreters 
are available for many operating systems, allowing Python code to run on a wide
variety of systems. CPython, the reference implementation of Python, is open source
software and has a community-based development model, as do nearly all of its 
variant implementations. CPython is managed by the non-profit Python Software Foundation ."""
#i.	E.g. Python  [is, has, features, interpreters, code, Software]. In this example the words listed are likely to follow “Python”

str1=str1.replace(".","")
str1=str1.replace("\n","")
str1=str1.replace(",","")
str_list=str1.split()
dict1={}
def getvalue(value): 
    temp1=[]
    temp2=[]
    for x in range(len(str_list)-1):
        if str_list[x]==value and str_list[x+1] not in temp1:
            temp1.append(str_list[x+1])
            temp2.append(str1.count(str_list[x]+' '+str_list[x+1]))
    return temp1,temp2

for x in range(len(str_list)-1):
    dict1[str_list[x]]=getvalue(str_list[x])
for x,y in dict1.items():
    print(x,':',y[0])

 #b.Given a word predict the word that’s likely to follow.
predict=input("Enter the world to predict next value:")
for x,y in dict1.items():
    if x==predict:
        m=max(y[1])
        m_index=y[1].index(m)
        print("Possible next word would be:",y[0][m_index])


        break


#Interface		IP-Address	OK? 	Method Status	Protocol
 
import re
ipconfig='''FastEthernet0/0   192.168.1.242	YES 	manual up	up 
FastEthernet1/0       unassigned	YES 	unset		down 
Serial2/0              	192.168.1.250	YES 	manual up	up 
Serial3/0              	192.168.1.233	YES 	manual up	up 
FastEthernet4/0        unassigned	YES 	unset  		down	
FastEthernet5/0        unassigned	YES        unset 		down'''

for line in ipconfig.splitlines():
  search=re.search("([\w/]*\s+)(\d{1,4}.\d{1,4}.\d{1,4}.\d{1,4}|unassigned)\s+(YES|NO)\s+(unset|manual up)\s+(\w+)",line)
  print(search.group(1).strip()," :",search.group(4).strip())


##10.	Given a number line from -infinity to +infinity. You start at 0 and can go either to the left or to the right. The condition is that in i’th move, you take i steps. In the first move take 1 step, second move 2 steps and so on. 
x=100000
num=0
count=0
def steps(x):
  global num,count
  if x>0:
    count+=1
    num=num+1
    steps(x-num)
  elif x<0:
    count+=1
    if -x<=num:
      steps(0)
    else:
      num+=1
      steps(x+num)
  return count
print(steps(x))