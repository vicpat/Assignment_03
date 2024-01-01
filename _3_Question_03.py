            ############# Question no 3 #############

# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

x = 'The quick Brow Fox'
def char(x):
    uc = 0
    lc = 0
    for i in x:
        if i>='a' and i<='z':
            lc += 1
        if i >='A' and i<='Z':
            uc += 1
    print("UpperCase letter in the String is",uc)
    print("LowerCase letter in the String is",lc)
    
char(x)