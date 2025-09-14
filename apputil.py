def fib(n):             
    #Defining a function to calculate nth Fibonacci number
    if n == 0:
        # If n is 0, return 0(first Fibonacci number)
        return 0

    elif n == 1:
        #If n is 1, return 1 (second fibonacci number)
        return 1
    else:
        #Recursive case:
        #The nth Fibonacci number is the sum of the (n-1)th and (n-2)th numbers
        return fib(n-1) + fib(n-2)

print("fib(9)=", fib(9))
