#My own code for Collatz Conjecture
n=int(input("Program for Collatz conjecture\nEnter a positive integer: "))
if n<=0:
    print("Enter a positive integer greater than 0")
elif n==1:
    print("1!")
else:
    print("The collatz sequence of",n)
    while(n!=1):
        if n%2==0:
            n=n//2
        else:
            n=3*n+1
        print(n,end=" ")
