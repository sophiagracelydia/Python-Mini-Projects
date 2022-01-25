'''#******************************* CESAR CIPHER  **********************
msg = input("Enter the message: ")
key = int(input("Enter the key value: "))
secret_msg = ""

for char in msg:
    if char.isalpha():
        code = ord(char)
        code += key
        if char.isupper():
            if code > ord("Z"):
                code -= 26
            elif code < ord("A"):
                code += 26
        else:
            if code > ord("z"):
                code -= 26
            elif code < ord("a"):
                code += 26
        secret_msg += chr(code)
    else:
        secret_msg += char
print("Encrypted msg: ", secret_msg)

key = -key
original_msg = ""

for char in secret_msg:
    if char.isalpha():
        code = ord(char)
        code += key
        if char.isupper():
            if code > ord('Z'):
                code -= 26
            elif code < ord('A'):
                code += 26
        else:
            if code > ord('z'):
                code -= 26
            elif code < ord('a'):
                code += 26
        original_msg += chr(code)
    else:
        original_msg += char
print("Decrypted msg: ", original_msg)
------------------------------------------------------------------------
************************  SYMMETRICAL & PALINDROME  ****************************

msg = str(input("Enter the string: "))
half = int(len(msg)/2)

if len(msg)%2 == 0:
    first_str = msg[:half]
    second_str = msg[half:]
else:
    first_str = msg[:half]
    second_str = msg[half+1:]

if first_str == second_str:
    print(msg,"is Symmetric")
else:
    print(msg, "not Symmetric")

if first_str == second_str[::-1]:
    print(msg, "is palindrome")
else:
    print(msg, "is not palindrome")
*********************  REVERSE THE WORDS IN STRING  ****************************

string = input("Enter the string: ")
string = string.split(' ')
rev = ' '.join(reversed(string))
print(rev)


------------------------------------------------  FILES  ------------------------------

import os
with open("mydata.txt", mode="w", encoding="utf-8") as my_file:
    my_file.write("Some random texts\n more and more\nwill see the data")

with open("mydata.txt", encoding="utf-8") \
        as my_file:
    print(my_file.read())
print(my_file.closed)

---------------------------- '''

msg = str(input("Enter the string: "))
half = int(len(msg)/2)

if len(msg)%2 == 0:
    first_str = msg[:half]
    second_str = msg[half:]
else:
    first_str = msg[:half]
    second_str = msg[half+1:]

if first_str == second_str:
    print(msg,"is Symmetric")
else:
    print(msg, "not Symmetric")

if first_str == second_str[::-1]:
    print(msg, "is palindrome")
else:
    print(msg, "is not palindrome")
