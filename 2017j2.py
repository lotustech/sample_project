#2017j2

n = int(input())
k = int(input())
sum = 0
for i in range(k+1):
    sum = sum + n*(10**i)
    print(sum)
print(sum)