# 별 찍기
"""
*
* *
* * *
* * * *
* * * * *
"""
n = int(input("별 개수 입력 : "))
for i in range(n):
    for j in range(i+1):
        print("*", end=' ')
    print()


"""
* * * * *
* * * *
* * *
* *
*
"""
n = int(input("별 개수 입력 : "))
for i in range(n+1, 0, -1):
    for j in range(i-1):
        print("*", end=' ')
    print()
# 선생님 풀이
n = int(input("별 개수 입력 : "))
for i in range(n):
    for j in range(n-i):
        print("*", end=" ")
    print()


"""
* * * * *
 * * * *
  * * *
   * *
    *
"""
# 선생님 풀이
n = int(input("별 개수 입력 : "))
for i in range(n, 0, -1):
    for s in range(n-i):
        print(" ", end="")
    for j in range(i):
        print("*", end=" ")
    print()


"""
* * * * *
  * * * *
    * * *
      * *
        *
"""
# 선생님 풀이
n = int(input("별 개수 입력 : "))
for i in range(n):
    for s in range(i):
        print(" ", end=" ")
    for j in range(n-i):
        print("*", end=" ")
    print()