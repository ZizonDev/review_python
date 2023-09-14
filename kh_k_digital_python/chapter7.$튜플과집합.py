# 튜플 정의하기
person = ('Alice', 30, 'New York')

# 튜플 요소에 접근하기
print(person[0])  # 'Alice'
print(person[1])  # 30

# 튜플 언패킹하기
name, age, city = person
print(name)  # 'Alice'
print(age)   # 30
print(city)  # 'New York'

# 튜플을 이용한 함수 반환값 다루기
def get_person():
    name = 'Bob'
    age = 25
    city = 'London'
    return name, age, city

result = get_person()
print(result)  # ('Bob', 25, 'London')
name, age, city = get_person()
print(name)    # 'Bob'
print(age)     # 25
print(city)    # 'London'

tp = (1,1,2,2,2,3,3,3,3)

print(tp.count(3))      #원하는 데이터의 개수를 세주는 함수
print(tp.index(1))      #원하는 데이터의 시작 인덱스번호를 알려주는 함수
print(tp.__len__())     #튜플 데이터의 개수 (공간의 개수) len(tp)
print(tp.__str__())     #문자열 형태로 변환

# 튜플 요소 삭제하기. (삭제되지 않음)
t1 = (1, 2, 'a', 'b')
del t1[0]
print(t1)

# 튜플의 요소 indexing.
t1[0]
t1[3]
print(t1)

# 튜플의 요소 slicing.
t1[1:]
print(t1)

# 튜플끼리 더하기.
t2 = (3, 4)
t1 + t2
print(t1)

# 튜플의 길이 구하기.
print(len(t1))

# 패킹(packing) : 여러 타입의 데이터들을 하나의 튜플이나 리스트로 묶어 선언하는 것.
tuple1 = 10, "열", True

# 언패킹(unpacking) : 하나의 튜플이나 리스트의 요소들을 여러 개의 변수에 나누어 대입하는 것
a, b, c = tuple1
print(a)
print(b)
print(c)

# set() : 집합, 순서가 없음, 고유한 값을 가지며 중복된 값이 올 수 없다. mutable 특성.
s1 = set([1,2,3,4,5])
s2 = set([4,5,6,7,8])

# 중복 제거
s3 = set([1,2,3,4,5,6,2,3,4,5])
print(s3)

# 교집합
print(s1.intersection(s2))
(s1 & s2)

# 합집합
print(s1.union(s2))
print(s1 | s2)

# 차집합
print(s1.difference(s2))
print(s1 - s2)