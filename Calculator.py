
def calculator(): 

	a=float(input("Enter the first number: "))
	b=float(input("Enter the second number: "))
	m=a+b
	print("Result = " + str(m))
	print("Result = ", m)

def subtractrion():
	c=float(input("Enter the first number: "))
	d=float(input("Enter the second number: "))
	f=c-d
	print("Total=",f)

def multiplication():
	a=float(input("Enter the first number: "))
	b=float(input("Enter the second number: "))
	h=a*b
	print("Total=",h)

def division():
	r=float(input("Enter the first number: "))
	j=float(input("Enter the second number: "))
	k=r/j
	print("Total=",k)

def addition1 (a , b):
	c = a + b 
	print("addition:",c)


def subtraction1 (a , b):
	c= a - b
	print ("subtraction:",c)


def multiplication1 (a , b):
	c = a * b
	print ("multiplication:",c)


def division1 (a, b):                                   
        try:
                c = a / b
                print ("division:", c)
        except:
                print("not divisible by zero")

def operation(a, b, c, d, e):
    f = a + b + c + d + e
    print("The total of the five numbers is:", f)


x1 = float(input("Enter the first number: "))
x2 = float(input("Enter the second number: "))
x3 = float(input("Enter the third number: "))
x4 = float(input("Enter the fourth number: "))
x5 = float(input("Enter the fifth number: "))
operation(x1, x2, x3, x4, x5)

def calculator():
    pass