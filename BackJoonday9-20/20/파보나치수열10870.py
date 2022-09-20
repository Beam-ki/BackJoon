def Pabo(n):
    if n<=1:
        return n
    return Pabo(n-1) + Pabo(n-2)
n = int(input())
print(Pabo(n))