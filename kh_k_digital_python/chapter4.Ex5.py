# 영식 요금제 : 30초 당 10원
# 민식 요금제 : 60초 당 15원
# 선생님 풀이
n = int(input())                            # 통화 발생 건수
call = list(map(int, input().split()))      # 통화 발생 건별 통화 시간, 공백 기준으로 문자열 input을 받는다. -> 이를 공백 기준으로 나누어 정수형으로 변환.

y_pay = m_pay = 0
for i in range(n):                          # 입력 받은 통화 발생 건수 만큼 돌면서
    y_pay += (call[i] // 30) * 10 + 10      # 통화 시간을 30초로 나눈 몫마다 10원 부과 + 기본 10원
    m_pay += (call[i] // 60) * 15 + 15      # 통화 시간을 60초로 나눈 몫마다 15원 부과 + 기본 15원

if y_pay > m_pay:                           # 영식 요금제가 더 비싸면 민식 요금제 출력
    print("M", m_pay)
elif y_pay < m_pay:
    print("Y", y_pay)
else:                                       # 영식 요금제와 민식 요금제의 가격이 같으면 문제 조건에 따라 영식을 먼저 쓰고 민식을 쓴다.
    print("Y M", y_pay)