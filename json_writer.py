'''Building a fibonacci sequence and then storing it in a json object'''
import json

fib = [0, 1]

for i in range(0,50):
	#next = fib[i] + fib[i + 1]
	#print(next)
	#fib.append(next)
	fib.append(fib[i] + fib[i + 1])

print(fib)#<<