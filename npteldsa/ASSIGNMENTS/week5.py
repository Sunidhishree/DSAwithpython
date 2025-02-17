import math
students = {}
i=0
sub={}
grades=[]
gr = {
    "A": 10,
    "AB": 9,
    "B": 8,
    "BC": 7,
    "C": 6,
    "CD": 5,
    "D": 4
}
# Read students
while True:
    inp = input()
    if inp == "Students":
        break
    if '~' in inp:
        sub[inp.split('~')[0]]=[]

while True:
    inp = input()
    if inp == "Grades":
        break
    roll_number, full_name = inp.split("~")
    students[roll_number] = full_name
    sub[roll_number] = []

# Read grades
while True:
    inp = input()
    if inp == "EndOfInput":
        break
    grad = inp.split("~")
    grades.append(grad)
for i in range(0,len(grades)):
        if grades[i][0] in sub:
            sub[grades[i][0]].append([grades[i][3],grades[i][4]])


std=[]
for i in students:
    std.append([i,students[i]])

for i in std:
    r = i[0]
    for j in sub:
        for k in sub[j]:
            if k[0] == r:
                grade = k[1]
                if grade in gr:
                    i.append(gr[grade])


ss=[]
for i in std:
    ss.append([i[0],i[1]])

for i in range(0,len(std)):
    sum=0
    n=0
    for j in range(2,len(std[i])):
        sum+=std[i][j]
        n+=1
    if(n>0):
        rsum=round(sum/n,1)
        ss[i].append(rsum)
    else:
        ss[i].append(sum)
output=[]
ss.sort(key=lambda x: x[0])

for i in ss:
    output.append(f"{i[0]}~{i[1]}~{i[2]}")
print("\n".join(output))
