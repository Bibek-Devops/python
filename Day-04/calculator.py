import sys
def Name(a,b):
    name=a+b
    return name


def Age(c,d):
    days=float(c+d)
    return days


def Fingers(l_l_fingers,r_l_fingers,l_hand,r_hand):
    total=l_l_fingers+r_l_fingers+l_hand+r_hand
    return total

a=sys.argv[1]
b=sys.argv[2]
c=float(sys.argv[1])
d=float(sys.argv[2])
f_condition=float(sys.argv[3])
condition=sys.argv[3]
if condition == "Name":
    name= Name(a, b)
    print(name)
elif f_condition == "Age":
    days= Age(c,d)
    print(days)
    