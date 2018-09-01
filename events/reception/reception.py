
y = open("vip_list.txt", 'r')
vipList = y.readlines()

x = open("ordinary_list.txt", 'r')
ordList = x.readlines()
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
            j.append("vip")
    return j   
   
    

def check_ord(name):
    j = []
    for person in ordinary_list:
        x =name.lower()
        y = person.lower()
        if x in y:
            j.append(person)
            j.append("ordinary")
    return j 
y.close()
x.close()