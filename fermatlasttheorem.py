#Fermat's Last Theorem 

a = int(input("Enter value a: "))
b = int(input("Enter value b: "))
c = int(input("Enter value c: "))
n = int(input("Enter value n: "))


def check_fermat(a,b,c,n):
    if(n > 2):
        x = a**n + b**n
        y = c**n
        if(x==y): 
            print("Holy smokes, Fermat was wrong!")
    else:
        print("No that does not work!")


    

print(check_fermat(a,b,c,n))
