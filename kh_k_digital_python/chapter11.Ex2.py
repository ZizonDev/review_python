# [문제] 주어진 세 변의 길이로 삼각형이 직각인지 아닌지 구분하시오.
# [입력] 입력은 여러개의 테스트케이스로 주어지며 마지막줄에는 0 0 0이 입력된다.
#       각 테스트케이스는 모두 30,000보다 작은 양의 정수로 주어지며, 각 입력은 변의 길이를 의미한다.
#       세 변의 길이의 입력 순서는 정해져 있지 않다.
# [출력] 각 입력에 대해 직각 삼각형이 맞다면 "right", 아니라면 "wrong"을 출력한다.

rst = []                # 결과를 출력하기 위한 빈 리스트 생성.
while True:
    ls = list(map(int, input().split()))
    ls.sort()           # 오름차순 정렬. -> 리스트의 가장 마지막 값이 빗변이 되도록.
    if ls[0] == 0 and ls[1] == 0 and ls[2] == 0:
        break
    elif ls[0]**2 + ls[1]**2 == ls[2]**2:
        rst.append("right")
    else:
        rst.append("wrong")
for e in rst:
    print(e)

