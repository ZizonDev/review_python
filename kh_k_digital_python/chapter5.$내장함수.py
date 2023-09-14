# 내장함수 : python이 기본으로 제공하는 함수. import 필요 없음.

# 최댓값, 최솟값 추출하기 (max, min)
print(max(1,2,3,4,5,6,7,77,777,88,99,100))
print(min(1,2,3,4,5,6,7,77,777,88,99,100))

# 총합 도출하기 (sum)
print(sum([1,2,3,4,5,6,7,8,9,10]))          # [] : list
print(sum((1,2,3,4,5,6,7,8,9,10)))          # () : tuple
num = list(map(int, input("정수 값 입력 : ").split()))
print(f"입력 받은 값들의 총합 : {sum(num)}")

# 평균 도출하기 (sum / len)
print(f"입력 받은 값들의 평균 : {sum(num)/len(num)}")

# 몫과 나머지 추출하기 (divmod)
print(f"몫과 나머지 : {divmod(10, 4)}")      # 결과는 (2, 2) 출력됨. 즉 10을 4로 나눈 (몫, 나머지) 형태로 출력됨. tuple의 동작 원리와 유사.

# 오름차순 정렬하기 (sorted)
my_list = [9,5,7,4,1,3,2,8,6,10]
print(sorted(my_list))
# 내림차순 정렬하기 (reverse=True)
print(sorted(my_list, reverse=True))