num1 = int(input("Scrivere il primo numero:"))
num2 = int(input("Scrivere il secondo numero:"))
num3 = int(input("Scrivere il terzo numero:"))

def max(num2, num1):
    if num1>num2 :
        return num1
    else :
       return num2

def maxDi3(num1, num2,num3) :
    if max(num1,num2)>num3:
        return max(num1,num2)
    else :
        return num3
print(maxDi3(num1,num2,num3))