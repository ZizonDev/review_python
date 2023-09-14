"""
***행사 안내 메일 내용 자동 작성 하기***

- 이름 : 백이진
- 행사내용 : 현대 자동차 신차 발표회
- 일시 : 20220301 (연속해서 입력)
- 시간 :  14
"""
# 한파의 연속인 1월 입니다.
# 봄을 기다리는 2월 입니다.
# 봄의 기운이 느껴지는 3월 입니다.
# 새싹이 피어나는 4월 입니다.
# 계절의 여왕 5월 입니다.
# 활동하기 좋은 6월 입니다.
# 휴가가 기다려지는 7월 입니다.
# 무더운 8월 입니다.
# 선선한 9월 입니다.
# 천고마비의 계절 10월 입니다.
# 쓸쓸한 늦가을 11월 입니다.
# 올 한해의 마무리 12월 입니다.

# 1. 월별 안내 문구를 자동으로 변경 해보기

name = input("이름 : ")
event = input("행사내용 : ")
date = input("일시 : ")
time = input("시간 : ")

month = date[4:6]
if month == "01":
    greeting = "한파의 연속인 1월 입니다."
elif month == "02":
    greeting = "봄을 기다리는 2월 입니다."
elif month == "03":
    greeting = "봄의 기운이 느껴지는 3월 입니다."
elif month == "04":
    greeting = "새싹이 피어나는 4월 입니다."
elif month == "05":
    greeting = "계절의 여왕 5월 입니다."
elif month == "06":
    greeting = "활동하기 좋은 6월 입니다."
elif month == "07":
    greeting = "휴가가 기다려지는 7월 입니다."
elif month == "08":
    greeting = "무더운 8월 입니다."
elif month == "09":
    greeting = "무더운 8월 입니다."
elif month == "10":
    greeting = "천고마비의 계절 10월 입니다."
elif month == "11":
    greeting = "쓸쓸한 늦가을 11월 입니다."
else :
    greeting = "올 한해의 마무리 12월 입니다."

# 2. 시간을 14로 입력 받으면 오후 2시로 출력 해보기

trans_time = int(time)
if(trans_time > 12):
    trans_time = trans_time - 12
    time = "오후" + str(trans_time)
else:
    time = "오전" + str(trans_time)

print(f"{name}님.")
print(greeting)
print(f"아래와 일정으로 {event}를 진행 하고자 하오니 오셔서 \
자리를 빛내 주시기 바랍니다.\n")
print("="*5, "행사 안내", "="*5)
print("행사 안내 : " + event)
# print("일시 : " + date[:4] + "년 " + date[4:6]+"월 " + date[6:8] + "일")
print(f"일시 : {date[:4]}년 {date[4:6]}월 {date[6:8]}일")
print("시간 : " + time + "시")

# 3. 파일로 저장해 보기

# 4. 파일에서 발송 명단 가져오기