def menu():
    print("[1] for Rectangel")
    print("[2] for Circle")
    print("[3] for Triangel")
    
menu()
option = int(input("Choose your option: "))

if option == 1:
    l = int(input("Enter Length: "))
    w = int(input("Enter Width: "))
    a = int(l*w)
    print("Your ans.: ")
    print(a)
    pass

if option == 2:
    r = int(input("Enter Raidus: "))
    ca = int(r*22/7*2)
    print("Your ans.: ")
    print(ca)
    pass
    


if option == 3:
    h = int(input("Enter Height: "))
    b = int(input("Enter base: "))
    ta = int((1/2)*b*h)
    print("Your ans.: ")
    print(ta)
    pass

if option != 1:
    if option != 2:
        if option != 3:
            print("Invaild Option")