max = -2000000000
min = 2000000000
n = int(input())
for i in range(n):
    a = int(input())
    if(a<min):
        min = a
    if(a>max):
        max = a
print(min)
print(max)