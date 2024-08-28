def gcdcalculator(a,b):
    gcd = 1
    for i in range(1, min(a,b) + 1):
        if a%i == 0 and b%i == 0:
            gcd = i
    return gcd
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("The GCD is ",gcdcalculator(num1,num2))
lcm = (num1*num2)/gcdcalculator(num1,num2)
print("The LCM is ",lcm)
