from reception import reception

def registration_checker():
    vistor = input("Enter is your first name: ")
    category = input("Enter your category:")

    
    if vistor and (category == "vip"):
        return reception.check_vip(vistor)
    elif vistor and (category == "ordinary"):
        return reception.check_ord(vistor)
   

print(registration_checker())