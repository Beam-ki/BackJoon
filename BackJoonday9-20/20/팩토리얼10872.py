
def Fact(n):
    result=1
    if n>0:
        result=n * Fact(n-1)
    return result
n = int(input())
print(Fact(n))