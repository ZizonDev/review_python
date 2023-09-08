# 여러 개의 값을 한 번에 입력 받아 리스트로 만들기
# 최댓값, 최솟값, 합계, 평균, 합계를 5로 나눈 몫과 나머지, 리스트의 오름차순, 내림차순 정렬 결과 출력하기
ls = list(map(int, input().split()))
print(f"최댓값 : {max(ls)}")
print(f"최솟값 : {min(ls)}")
print(f"합 계 : {sum(ls)}")
print(f"평 균 : {sum(ls) / len(ls)}")
print(f"몫과 나머지 : {divmod(sum(ls), 5)}")
print(f"몫 : {divmod(sum(ls),5)[0]} 나머지 : {divmod(sum(ls),5)[1]}")
print(f"오름차순 정렬 : {sorted(ls)}")
print(f"내림차순 정렬 : {sorted(ls, reverse=True)}")


