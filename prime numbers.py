# Complete the code to find if a given number is a prime number?
# The program will take a positive integer greater than 1 as input and indicate if it is a prime number by saying "prime",
# and if it is not a prime number saying "not a prime". 
# Note there are 3 places in the given code that you need to fix for this code to work properly and give the expected output. 

i = int(input('enter number'))
j = 2
while (j <= (i/j)):
    if not(i%j): 
        print("not a prime")
        break
    j = j + 1
if (j > i/j): 
    print ("prime")
