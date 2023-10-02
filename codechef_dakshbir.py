def fibonacci_(n):
    if n<= 0:
        print("Incorrect input")
    
    elif n == 1:
        return 0
    
    elif n == 2:
        return 1
    
    else:
        return fibonacci_(n-1)+fibonacci_(n-2)
 
def golden_ratio(n):
    if n==0:
        print("Incorrect input")
    elif n==1:
        print("golden ratio cannot be calculated")
    elif n==2:
        print("golden ratio cannot be calculated")
    
    else:
        n1=fibonacci_(n)
        n2=fibonacci_(n-1)
        return n1/n2


n=int(input("Enter a number to calculate its fibonacci sequence and golden ratio"))
print("Fibonacci Sequence number is:",fibonacci_(n))
print("Golden ratio is:",golden_ratio(n))
