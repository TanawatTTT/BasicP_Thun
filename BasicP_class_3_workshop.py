Pluem = 1200
w1 = 400
w2 = 600
w3 = 200

while True:
    option = input("Enter number :")
    if option == "1" :
        print("Fighting")
        optionnumber = int(input("how many :"))
        print("w1 = 500")
        print("w2 = 400")
        print("w3 = 300")
        for i in range(optionnumber):
            W = input("Choose Weapon :")
            if W == "w1":
                print("U choose w1")
                Pluem -= w1
                print(Pluem)        
        
            
            

    elif option == "2" :
        print("run")
        break