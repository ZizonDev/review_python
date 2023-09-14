# 모듈 : 변수, 함수, 클래스를 포함하는 코드가 저장된 파일.
# 모듈은 다른 모듈에서도 불러서 실행할 수 있고 콘솔이나 주피터 노트북에서 불러서 실행할 수도 있다.

# import module
import math

print(math.sin(1))
print(math.cos(1))
print(math.tan(1))
print(math.floor(2.5))
print(math.ceil(2.5))

# from 구문 : 필요한 모듈만 포함하고 싶을 때 사용.
from math import sin, cos, tan, floor, ceil

print(sin(1))
print(cos(1))
print(tan(1))
print(floor(2.5))
print(ceil(2.5))

# as 구문 : 모듈을 가져올 때 이름 충돌이 발생하는 경우, 긴 이름을 간결하게 사용하고 싶을 때 사용.
import math as m

print(m.sin(1))
print(m.cos(1))
print(m.tan(1))
print(m.floor(2.5))
print(m.ceil(2.5))

# sys module : 시스템과 관련된 정보를 가지고 있는 모듈. 명령 매개변수를 받을 때 많이 사용.
import sys
# 명령줄 인수 출력
print("명령줄 인수:", sys.argv)
# 스크립트 실행 경로
print("실행 경로:", sys.path[0])
# 표준 출력
sys.stdout.write("Hello, World!\n")
# 표준 에러 출력
sys.stderr.write("Error occurred!\n")
# 프로그램 종료
sys.exit(0)

# os module : 파이썬의 표준 라이브러리로, 운영체제와 상호작용하기 위한 기능을 제공.
# 파일 시스템 접근, 환경 변수 제어, 프로세스 관리 등 다양한 운영체제 관련 작업을 수행 가능.
import os
# 현재 작업 디렉토리
cwd = os.getcwd()
print("현재 작업 디렉토리:", cwd)
# 디렉토리 생성
os.mkdir("mydir")
# 파일 또는 디렉토리 존재 여부 확인
is_file = os.path.isfile("myfile.txt")
is_dir = os.path.isdir("mydir")
print("myfile.txt는 파일인가?", is_file)
print("mydir은 디렉토리인가?", is_dir)
# 시스템 명령 실행
os.system("ls -l")

# 패키지 : 패키지는 모듈들의 집합이며, 여러 모듈들을 하나의 디렉토리에 구성하여 관련 기능을 그룹화한 것.
# 패키지는 코드의 구조화, 재사용성 및 네임스페이스 관리를 위해 사용.
# 프로젝트의 규모가 커질 때 모듈을 조직화하고 명확한 계층 구조를 가질 수 있도록 도와준다.