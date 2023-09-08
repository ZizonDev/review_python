# 영어 소문자, 대문자로 이루어진 단어를 입력받은 뒤, 대문자는 소문자로, 소문자는 대문자로 바꾸어 출력하는 프로그램.
# 선생님 풀이
rst = ""                    # 결과값 초기화
for e in input():           # 입력받는 문자열(개수)만큼 for문이 돈다. (자동 순회)
   if e.islower():          # e번째 문자가 소문자면
       rst += e.upper()     # 대문자로 바꾼다.
   else:
       rst += e.lower()
print(rst)



# print(ord("A"))     # 65
# print(ord("Z"))     # 90
# print(ord("a"))     # 97
# print(ord("z"))     # 122

word = list(map(str, input()))
for i in range(0, len(word), 1):
    if 65 <= ord(word[i]) <= 90:
        print( chr(ord(word[i]) + 32), end='' )
    else:
        print( chr(ord(word[i]) - 32), end='' )

