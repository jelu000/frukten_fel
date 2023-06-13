import random

#Definerar en funktion
def print_fruit(userinput):
    fnr =  int(userinput)
    print("\n" + frukter[fnr-1] + " kommer här!")

frukter =("Apelsin", "Banan", "Äppler", "Päron", "Kiwi")

looping = True

while looping:
    print("-----------------------------")
    print("\n-:FruktAutomat:-\n")

    i = 1

    for frukt  in frukter:
        print( i + ": " + frukt)
        i += 1
        
        
    fruktnr = input("\nMata in siffra för vald frukt: ")
    print_fruit(fruktnr)
    
    go = input("Vill du välja en frukt till? j/n: ")

    if (go == "N"):
        break

print("\n-----------------------------------\n")
print("Föresten här får du en frukt till! ")
slumpfrukt = random.randint(1, 5)
print_fruit(slumpfrukt)