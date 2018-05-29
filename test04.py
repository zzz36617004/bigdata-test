s = """We encourage everyone to contribute to Python. If you still have 
questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new 
contributors through the process."""

s = s.upper()
list=[]
s = s.replace(","," ")
s = s.replace("."," ")
s = s.replace("\n"," ")
s = s.split()
# for i in s:
#     print(i)
a = set([])
for i in s:
    p = i+":"+str(s.count(i))
    a.add(p)

for i in a:
     list.append(i)
list.sort()
for i in list:
 print(i)