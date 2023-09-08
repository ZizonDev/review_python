# list : 원소들이 연속적으로 저장되는 형태의 자료형.
# 크기가 정해지지 않음. 원소에 모든 자료형이 올 수 있다. 중첩된 list 사용이 가능하다.
# mutable 객체. (즉, list를 읽고 쓰기가 가능하다.) cf) tuple은 원소가 변할 수 없으므로 읽기만 가능한 immutable 객체.
number = [1,2,3,4,5,6]
fruits = ["apple", "banana", "cherry", "orange"]
mixed = [1, True, "Seoul", 3.1415]
doubled = [[1,2,3,4,5], ["apple", "키위"]]

# 변수와 list 비교하기 (입력 받을 성적의 수가 정해져 있는 경우)
kor, mat, eng = map(int, input("성적 입력 : ").split())
total = sum([kor, mat, eng])
print(f"총점 : {total}")

# 입력받을 성적의 수가 정해져 있지 않은 경우
score = list(map(int, input("성적 입력 : ").split()))
print(f"총점 : {sum(score)}")
print(f"평균 : {sum(score)/len(score)}")

# list indexing, slicing
str_name = ["seoul", "busan", "daegu", "jeju", "incheon"]
print(str_name)
print(str_name[1])          # index 1의 요소인 busan 출력됨.
print(str_name[1][2])       # index 1 요소 busan의 index 2 문자 s 출력됨!
slice = str_name[1:3]       # str_name의 index 1 이상 index 3 미만 잘라서 출력.
print(slice)                # busan, daegu 출력됨.
print(len(slice))           # 자른 리스트의 길이 2 출력됨.
print(len(slice[0]))        # 자른 리스트 busan, daegu의 0번째 요소의 길이 즉, busan의 길이 5가 출력됨.

primes = [2,3,5,7,11]
print(primes[0])
print(primes[-1])           # index -1은 뒤에서부터 첫번째 즉, 가장 마지막의 요소 나타냄.
print(primes[-2:])          # 뒤에서 2번째 요소부터 순서대로 끝까지 출력.

# list 연산자 : 연결(+), 반복(*), len()
list_a = [1,2,3]
list_b = [4,5,6]
print(list_a + list_b)
print(list_a * 3)
print(len(list_a + list_b))

# list 요소 추가하기 (append, insert)
# append() : list의 맨 마지막에 요소 추가
# insert(index, 값) : 해당 index에 값 추가
list_c = [1,2,3]
list_c.append(4)
list_c.append(5)
list_c.insert(1, 1.5)
print(list_c)

# list 요소 제거하기 (pop, remove, clear, del)
# pop() : 괄호 안 index에 해당하는 값을 삭제 후 삭제한 값을 보여 줌. index가 없다면 가장 마지막의 값 삭제 후 보여 줌.
# remove() : 괄호 안 index 값을 반환하지 않고 바로 삭제함. 동일한 값이 여러 개인 경우 모든 인덱스값 제거.
# clear() : list의 모든 값을 삭제함. 다만 list 자체는 삭제하지 않고 빈 list로 둠.
# del : del listname[index], index에 해당하는 값을 지워 줌.
list_d = [0,1,2,3,4,5,6,7,8,9,"a","b","c","d","korea","python"]
print(list_d)               # -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'korea', 'python']
print(list_d.pop(11))       # -> b
print(list_d.pop())         # -> python
print(list_d)               # -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'c', 'd', 'korea']
print(list_d.remove(3))     # remove는 반환 값이 없어서 None 출력.
print(list_d)               # index 3의 값 제거한 list_d 나타남. -> [0, 1, 2, 4, 5, 6, 7, 8, 9, 'a', 'c', 'd', 'korea']
del list_d[5]
print(list_d)               # -> [0, 1, 2, 4, 5, 7, 8, 9, 'a', 'c', 'd', 'korea']
list_d.clear()
print(list_d)               # -> []

# list의 중복 값 제거하기
my_list = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,1,2,3,4]
new_list=[]
for e in my_list:
    if e not in new_list:
        new_list.append(e)
print(new_list)             # -> [1, 2, 3, 4, 5, 6, 7, 8, 9]

# map(반환 함수 형태, 입력 자료형), filter(반환 함수, 입력 자료형)
nums1 = list(map(int, input("값 : ").split()))        # 여기서 int는 반환 함수인 int[] 에서 함수 구현부 []를 뺀 것. int 함수 대신 lambda 등 여러 함수가 올 수 있다.
print(nums1)
nums2 = list(map(lambda e: int(e)*int(e), input("값 : ").split()))
print(nums2)
nums3 = list(filter(lambda e: int(e)%2==0, input("값 : ").split()))      # filter(lambda e: int(e)%2==0 -> 짝수인 e값만 출력)
print(nums3)                                         # cf)filter를 걸어주면 str형태로 출력된다. 다시 int로 바꿔주면 됨.

# list의 원소 스캔하기
newjeans = ["민지", "하니", "다니엘", "해린", "혜인"]
# 향상된 for문 형식
for e in newjeans:
    print(e)
# 범위 기반 for문 형식 : range(초기값, 최종값, 증감값)
for i in range(len(newjeans)):
    print(newjeans[i])