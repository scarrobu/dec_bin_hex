import random
import hashlib

def route(choice):
    if choice == "1":
        try:
            num = int(input("Inset decimal number to conversion: "))
            print()
            print("hexadecimal value is: ", hex(num).lstrip("x0"))
            binar = bin(num).replace("0b", "")
            print("binary value is:      ", binar.zfill(8))
            print()
        except ValueError:
            print("NO number was entered!")
            print()
            
    elif choice == "2":
        binary_string = input("Inset binary number to conversion: ")
        print()
        try:
            decimal = int(binary_string,2)  
            print("decimal value is: ", decimal)
            print()
    
        except ValueError:
            print("Wrong binary number, use only digits 0 and 1!")
            print()
                
def bitcoin():
    k = ""
    for i in range(257):
        k += str(random.randint(0,1))
    return k



print("Selection:")
print("1. Conversion DEC-BIN,")
print("2. Conversion BIN-DEC,")
print("3. Creating a 256 digit binary number (+ SHA256).")
choice = input("Enter the choice of what you want to do: ")
if choice == "1":
    route(choice)
    input("press ENTER to exit")
elif choice == "2":
    route(choice)
    input("press ENTER to exit")
elif choice == "3":
    bitcoin()
    hashik = bitcoin()
    que = input("Write the created number also in SHA256 format? Y/N ")
    if que == "y" or que == "Y":
        print()
        print(hashik)
        print()
        print(hashlib.sha256(hashik.encode('utf-8')).hexdigest())
        print()
    else:
        print()
        print(hashik)
        print()
    input("press ENTER to exit")
else:
    print("Wrong choice!")

