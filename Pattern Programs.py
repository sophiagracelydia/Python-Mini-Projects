# square pattern
n = 5
for i in range(n):
    for j in range(n):
        print("* ",end='')
    print()
print("----------------------------")
# increasing triangle
n = 5
for i in range(n):
    for j in range(i+1):
        print("* ",end='')
    print()
print("----------------------------")
# decreasing triangle
n = 5
for i in range(n):
    for j in range(i, n):
        print("* ", end='')
    print()
print("----------------------------")
# Right sided triangle
          *
        * *
      * * *
    * * * *
  * * * * *
n = 5
for i in range(n):
    for j in range(i, n):
        print(" ",end=" ")
    for k in range(i+1):
        print("*",end=" ")
    print()
# Right Sided triangle:
  * * * * *
    * * * *
      * * *
        * *
          *
n = 5
for i in range(n):
    for j in range(i+1): # inc space
        print(" ",end=" ")
    for k in range(i, n): # dec star
        print("*", end=" ")
    print()
# Hill pattern
n = 5
for i in range(n):
    for j in range(i, n):
        print(" ", end=' ')
    for k in range(i):
        print("*", end=' ')
    for m in range(i+1):
        print("*", end=' ')
    print()
print("----------------------")
# Reverse hill pattern
n = 5
for i in range(n):
    for j in range(i+1):
        print(" ", end=' ')
    for k in range(i, n-1):
        print("*", end=' ')
    for m in range(i, n):
        print("*", end=' ')
    print()
#Diamond pattern
          *
        * * *
      * * * * *
    * * * * * * *
  * * * * * * * * *
    * * * * * * *
      * * * * *
        * * *
          *
n = 5
for i in range(n-1):
    for j in range(i, n):
        print(" ", end=' ')
    for k in range(i):
        print("*", end=' ')
    for m in range(i+1):
        print("*", end=' ')
    print()
for i in range(n):
    for j in range(i+1):
        print(" ", end=' ')
    for k in range(i, n-1):
        print("*", end=' ')
    for m in range(i, n):
        print("*", end=' ')
    print()
# Pyramid
n = 5
for i in range(n):
    for j in range(i, n):
        print(" ", end=' ')
    for k in range(i+1):
        print("*  ", end=' ')
    for m in range(i, n):
        print(" ", end=' ')
    print()
print("------------------------")
n = 5
for i in range(n):
    for j in range(i+1):
        print(" ", end=' ')
    for k in range(i, n):
        print("*  ", end=' ')
    for m in range(i+1):
        print(" ", end=' ')
    print()
# sandglass
    *  *  *  *
     *  *  *
       *  *
         *
       *  *
     *  *  *
    *  *  *  *
n = 4
for i in range(n-1):
    for j in range(i+1):
        print(" ", end=' ')
    for k in range(i, n):
        print("*  ", end=' ')
    for m in range(i+1):
        print(" ", end=' ')
    print()
for i in range(n):
    for j in range(i, n):
        print(" ", end=' ')
    for k in range(i+1):
        print("*  ", end=' ')
    for m in range(i, n):
        print(" ", end=' ')
    print()
'''

# Double hill pattern
n = 5
for i in range(n):
    for j in range(i, n):
        print(" ", end=' ')
    for k in range(i):
        print("*", end=' ')
    for m in range(i+1):
        print("*", end=' ')

    for j in range(i, n-1):
        print("   ", end=' ')
    for k in range(i):
        print("*", end=' ')
    for m in range(i+1):
        print("*", end=' ')
    print()
