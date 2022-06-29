#This function write binary of integers

def binary(x):
        a = ""
        while x != 0:
                a += str(x%2)
                x = x//2
        return a[::-1]

I = int(input('Write any integer to get its binary: '))
print(format(I, "b")) # To cross-check if equal or not
print(binary(I))
