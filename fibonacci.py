# Write a program to calculate Fibonacci numbers and find its step count.
import time
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return (fib(n-1)+fib(n-2))

num = int(input("enter the number:-"))
start_ns = time.perf_counter_ns()
for i in range(0,num+1):
    print(fib(i), end=" ")
end_ns = time.perf_counter_ns()
elapsed_ns = end_ns - start_ns
print()
print(elapsed_ns)

#reverser order
import time

def fib(n):
    fib_sequence = []
    a, b = 0, 1
    for i in range(n + 1):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence[::-1]

num = int(input("Enter the number: "))
start_ns = time.perf_counter_ns()
result = fib(num)
for val in result:
    print(val, end=" ")
end_ns = time.perf_counter_ns()

elapsed_ns = end_ns - start_ns
print()
print("Time taken (ns):", elapsed_ns)

#fractorial 

import time

def fract(num):
    start = time.time()
    if num == 0 or num == 1:
        return 1
    else:
        return num * fract(num -1)
    
num = int(input("enter a number: "))
start_ns = time.perf_counter_ns()
result = fract(num)
end_ns = time.perf_counter_ns()
print(f"Time elapsed (nanoseconds): {end_ns - start_ns}")
print(f"Result: {result}")
