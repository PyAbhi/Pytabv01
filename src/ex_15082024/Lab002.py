# Dt 13/8/2024 Homework
# Create a program for user input of two nos. and find the maximum, power1 num to num2
# subtraction, multiplication, division, addition, subtraction
# format your output with f{""}
num1 = int(input("enter number 1"))
num2 = int(input("enter number 2"))
result = max(num1,num2)
power = pow(num1,num2)
print("The Maximum number is:", result)
print("Sum value is", num1+num2)
print("Subtract value is", num1-num2)
print("Multiply value is", num1*num2)
print("Division value is", num1/num2)
print("Power of number is", power)
