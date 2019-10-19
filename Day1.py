def add(a, b):
	answer = a+ b
	return answer
answer= add(6, 7)
print(answer)

def subtract(a, b):
	answer = a-b
	return answer
answer= subtract(7, 6)
print(answer)

def multiplication(a,b):
	answer= a*b
	return answer
answer= multiplication(9,10)
print(answer)

def division(a,b):
	answer= a/b
	return answer
answer= division(18,9)
print(answer)

a=input('enter number ')
b=input('enter other number ')
c=input('enter equation ')
a=int(a)
b=int(b)
if c == '+':
	answer=add(a, b)
	print(answer)
else:
	if c == '-':
		answer=subtract(a,b)
		print(answer)
	else:
		if c == '*':
			answer=multiplication(a,b)
			print(answer)
		else:
			if c == '/':
				answer=division(a,b)
				print(answer)