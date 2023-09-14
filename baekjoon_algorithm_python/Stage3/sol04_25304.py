x = int(input())
n = int(input())
rst = 0
for e in range(n):
    a, b = map(int, input().split())
    rst = rst + a*b
if rst == x:
    print("Yes")
else:
    print("No")