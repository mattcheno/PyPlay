'''Building a fibonacci sequence and then storing it in a json object'''
import json

fib = [0, 1]
filename = 'fib.json'

for i in range(0,50):
	fib.append(fib[i] + fib[i + 1])

print(fib)

with open(filename, 'w') as f_obj:
	json.dump(fib, f_obj) #<<