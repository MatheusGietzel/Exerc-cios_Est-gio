def check_fibonacci(number):
    
    a, b = 0, 1
    while a <= number:
        if a == number:
            return f"{number} pertence à sequência de Fibonacci."
        a, b = b, a + b
    return f"{number} não pertence à sequência de Fibonacci."

# Ex:
number = 34 
result = check_fibonacci(number)
print(result)
