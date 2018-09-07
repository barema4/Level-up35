
file1 = open("vip_list.txt", 'r')
vipList = file1.readlines()

file2 = open("ordinary_list.txt", 'r')
ordList = file2.readlines()
vip_list = []
ordinary_list = []
for name in vipList:
    vip_list.append(name.rstrip('\n'))

for name in ordList:
    ordinary_list.append(name.rstrip('\n'))

def check_vip(name):
    j = []
    for person in vip_list:
        x =name.lower()
        y = person.lower()
        if x in y:
            j.append(person)
           
    if len(j) == 0:
        return "Not registered"

    j.append("vip")
    return j
   
    

def check_ord(name):
    j = []
    for person in ordinary_list:
        x =name.lower()
        y = person.lower()
        if x in y:
            j.append(person)
    if len(j) == 0:
        return "Not registered"
    j.append("ordinary")        
    return j 
file1.close()
file2.close()