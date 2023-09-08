"""
[문제] 첫 번째는 성을 모두 쓰고, 이를 하이픈(-)으로 이어 붙인 것이다. 예를 들면, Knuth-Morris-Pratt이다. 이것을 긴 형태라고 부른다.
    두 번째로 짧은 형태는 만든 사람의 성의 첫 글자만 따서 부르는 것이다. 예를 들면, KMP이다.
[입력] 입력은 한 줄로 이루어져 있고, 최대 100글자의 영어 알파벳 대문자, 소문자, 그리고 하이픈 ('-', 아스키코드 45)로만 이루어져 있다.
    첫 번째 글자는 항상 대문자이다. 그리고, 하이픈 뒤에는 반드시 대문자이다. 그 외의 모든 문자는 모두 소문자이다.
[출력] 첫 줄에 짧은 형태 이름을 출력한다.
"""
long_name = input()
name_list = list(map(str, long_name.split('-')))
for i in range(len(name_list)):
    print(name_list[i][0], end='')

# 선생님 풀이
initial = ""
for e in input():           # 입력 받은 수 만큼 e가 자동 순회.
    if e.isupper():
        initial += e
print(initial)
