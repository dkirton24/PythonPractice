

list1 = []
found = []
count = []

f = open("test.txt","r")
while True:
    c = f.read(1)
    list1.append(c)
    if not c:
      break

for i in range(0, len(list1)):
    if list1[i] not in found:
        found.append(list1[i])
        count.append(1)
    else:
        count[found.index(list1[i])] += 1
        
for j in range(len(found)):
    print(found[j],"\t",count[j])
