'''
To solve this problem:
Don't use the input function in this code
1. Assign a value of 5 to the variable tree_height
2. Print a tree like you saw in the video with 4 rows and a stump on the bottom
TIP 1
You should use a while loop and 3 for loops.
TIP 2
I know that this is the number of spaces and hashes for the tree
4 - 1
3 - 3
2 - 5
1 - 7
0 - 9
Spaces before stump = Spaces before top
TIP 3
You will need to do the following in your program :
1. Decrement spaces by one each time through the loop
2. Increment the hashes by 2 each time through the loop
3. Save spaces to the stump by calculating tree height - 1
4. Decrement from tree height until it equals 0
5. Print spaces and then hashes for each row
6. Print stump spaces and then 1 hash

Here is the sample program
How tall is the tree : 5
        #
       ###
      #####
     #######
    #########
        #
'''

# Sets 5 for tree_height (as an integer)
height = int(5)
# spaces starts as height - 1
spaces = stumpspaces = height -1
# hashes start as 1
hashes = 1
# This loop goes until the height limit is reached
# height will be decreased by 1 each iteration of the loop
while height >= 1:
    # Prints a space for the number of spaces before the hashes
    # This starts at height-1, just like the stump, and decreases 1 per iteration
    # end="" does not print a new line
    for i in range(spaces):
        print(" ", end="")
    # Prints the hashes
    # which starts at 1 and increases by 2 per iteration
    for j in range(hashes):
        print('#', end="")
    # prints a new line after each iteration of the spaces and hashes
    print()
    # spaces decreases 1 per iteration
    spaces -= 1
    # hashes increase 2 per iteration
    hashes += 2
    # This is what makes it go down to the next level
    height -= 1
# Prints the spaces before the hash stump
# which is height-1
for i in range(stumpspaces):
    print(' ', end="")
# Prints the hash stump
print("#")
