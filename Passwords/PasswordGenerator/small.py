import random; password = str()
for symb in range(0, 16):
    password += random.choice("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM123456789")
print(password)