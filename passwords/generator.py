import random #import random module

print("Password Generator") #name
while 1:
    try: #except errors
        length = int(input("Enter length: ")) + 1 # get length
    except KeyboardInterrupt: #except ctrl+c
        print("Exiting...") #ctrl+c message
        raise SystemExit #exit
    except: # except other errors
        print("Enter a number!") #error message
        raise SystemExit #exit
    try:
        bigletter_index = random.randint(0, length-1) #index generate
        specialsymbol_index = random.randint(0, length-1) # index generate

        while bigletter_index == specialsymbol_index: #check matches
            specialsymbol_index = random.randint(0, length-1)
    except KeyboardInterrupt:
        print("Ctrl+C")
        raise SystemExit
    text = [random.choice('abcdefghijklmnopqrstuvwxyz123456789') for _ in range(length)] #generate random password
    text[bigletter_index] = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') #add big letter
    text[specialsymbol_index] = random.choice('!@#$%^&*()') #add special symbol
    text[-1] = ""
    print(''.join(text)) #print password
    try: input("Enter to continue, Ctrl+C to exit... ") 
    except: raise SystemExit
