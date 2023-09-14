# 회원 가입을 위한 아이디와 패스워드 입력 받기 (길이 판별의 2가지 방법)
"""
- string.find(찾을 문자)
- string.find(찾을 문자, 시작 Index)
- string.find(찾을 문자, 시작 Index, 끝 Index)
- 존재하지 않으면 -1을 리턴 합니다.
- 문자열의 길이를 구하는 방법은 2가지 입니다.( pw.__len__ 과 len(pw))
"""
user = input("아이디 입력 : ")
if len(user) >= 8:             # 입력받은 아이디의 길이(len)가 10과 같거나 크다면
    pw = input("비밀번호 입력 : ")
    # if pw.__len__() < 8 or pw.__len__() > 16:    # pw의 길이가 8보다 작거나 16보다 크면 (by 내부함수)
    if len(pw) < 8 or len(pw) > 16:                # by 외부함수
        print("비밀번호는 8자에서 16자 사이여야 합니다.")
    elif pw.find(user) >= 0:                       # 비밀번호에 아이디와 동일한 문자열이 있다면 (index 0부터 find 했을 때 있다면)
        print("비밀번호에 아이디를 포함시킬 수 없습니다.")
    else:
        print(f"아이디 : {user}")
        print(f"비밀번호 : {pw}")
else:
    print("아이디는 반드시 8자 이상이어야 합니다.")
