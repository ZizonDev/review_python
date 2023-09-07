n = int(input())
call = list(map(int, input().split()))

y_pay = m_pay = 0
for i in range(n):
    y_pay += (call[i] // 30) * 10 + 10
    m_pay += (call[i] // 60) * 15 + 15

if y_pay > m_pay:
    print("M", m_pay)
elif y_pay < m_pay:
    print("Y", y_pay)
else:
    print("Y M", y_pay)