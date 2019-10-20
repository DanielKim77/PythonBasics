def add(a, b):
	answer = a+ b
	return answer
answer= add(6, 7)

def subtract(a, b):
	answer = a-b
	return answer
answer= subtract(7, 6)

def multiplication(a,b):
	answer= a*b
	return answer
answer= multiplication(7, 6)

def division(a,b):
	answer= a/b
	return answer
answer= division(18,9)

def exponents(a,b):
	answer=a**b
	return answer
answer= exponents(1,2)

def SquareRoots (a,b):
	answer=a**1/b
	return answer
answer= SquareRoots(1,1)
def calculator():
	a=input('enter number ')
	b=input('enter other number ')
	c=input('enter equation ')
	a=int(a)
	b=int(b)
	if c == '+':
		answer=add(a, b)
		print(answer)
	elif c == '-':
		answer=subtract(a,b)
		print(answer)
	elif c == '*':
		answer=multiplication(a,b)
		print(answer)
	elif c == '/':
		answer=division(a,b)
		print(answer)
	elif c == '^':
		answer=exponents(a,b)
		print(answer)
	else:
		calculator()
	calculator()
calculator()