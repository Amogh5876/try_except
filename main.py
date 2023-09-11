output = 0
try:
    v1 = input("enter a number: ")
    output = 100/(int(v1)-10)

except ZeroDivisionError :
    print("Number cant be divisible by zero")
    output = 1
else:
    print("No problem in the code")

print("outout is:", output)
