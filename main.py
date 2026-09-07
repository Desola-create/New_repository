print('Hi There')

def addition ():
	a=10
	b=20
	m=a+b
	print("Result = " + str(m))
	print("Result = ", m)


def subtractrion():
	c=100
	d=75
	f=c-d
	print("Total=",f)

def multiplication():
	a=2
	b=4
	h=a*b
	print("Total=",h)

def division():
	r=14
	j=2
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


print("*****************************************")
addition()
subtractrion() 
multiplication()
division()
print("*****************************************")
addition1(2, 3)
subtraction1(1, 7) 
multiplication1(8, 3)
division1(9, 0)
