import random

num_list = []
for i in range(5):
    num_list.append(random.randrange(1, 9))
for i in num_list:
    print(i, end="")

i = len(num_list) - 1
while i > 1:
    j = 0
    while j < i:
        print()
        print("{} > {}".format(num_list[j], num_list[j+1]))
        if num_list[j] > num_list[j+1]:
            print("Switch")
            temp = num_list[j]
            num_list[j] = num_list[j+1]
            num_list[j+1] = temp
            print()
        else:
            print("Dont switch")
        j += 1
        for k in num_list:
            print(k, end = "")
        print()
    print("End of round")
    i -= 1
    for k in num_list:
        print(k, end="")
    print()


import random
num_list = []
for i in range(5):
    num_list.append(random.randrange(1, 9))
for i in num_list:
    print(i, end="")

i = len(num_list) - 1
while i > 1 :
    j = 0
    while j < i :
        print()
        print("{} > {}".format(num_list[j], num_list[j+1]))

        if num_list[j] > num_list[j+1]:
            print("switch")
            temp = num_list[j]
            num_list[j] = num_list[j + 1]
            num_list[j + 1] = temp
            print()
        else:
            print("Don't switch")
        j += 1
        for k in num_list:
            print(k, end="")
        print()
    i -= 1
    for k in num_list:
        print(k, end="")
    print()
