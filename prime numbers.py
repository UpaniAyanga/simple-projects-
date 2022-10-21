# a code created to find whether any given integer is a prime number or not  

i = int(input('enter number'))
j = 2
while (j <= (i/j)):
    if not(i%j): 
        print("not a prime")
        break
    j = j + 1
if (j > i/j): 
    print ("prime")
