remove1=[]
remove2=[]
solution=[]
with open("C:\\Users\\rohan\\Desktop\\programmig\\75000\\4001.txt","r") as reader:
    for line in reader.readlines():
        remove1.append(line)
print(remove1)
for mac in remove1:
    raw = mac.replace('\xe2\x80\x9d','"')
    remove2.append(raw)
for mac in remove2:
    raw = mac.replace('\xe2\x80\x9c','"')
    solution.append(raw)
with open("C:\\Users\\rohan\\Desktop\\programmig\\Automation\\1 tra.txt","w") as f:
    for i in solution :
        f.write(i)