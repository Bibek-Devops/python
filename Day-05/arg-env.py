import sys
import os

num1=float(sys.argv[1])
num2=float(sys.argv[2])
operation=sys.argv[3]

if operation == "Add":
    total=num1+num2
    print(total)

elif operation == "Subs":
    total=num1-num2
    print(total)

elif operation == "Div":
    total=num1/num2
    print(total)

elif operation == "Mul":
    total=num1*num2
    print(total)

env_details=os.getenv("SDKMAN_PLATFORM")
print(env_details)