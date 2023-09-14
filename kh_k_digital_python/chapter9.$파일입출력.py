score_file = open("../score.txt", "w", encoding="utf-8")
# score_file = open("score.txt", "a", encoding="utf8") # append
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.write("과학 : 80" + "\n")
score_file.write("코딩 : 100" + "\n")
score_file.close()

# read() : 파일 내의 모든 내용을 읽어 하나의 문자열로 반환
score_file = open("../score.txt", "r", encoding="utf-8")
print(score_file.read())
score_file.close()

# readline() : 해당 파일의 내용을 한 라인씩 읽어 들여 문자열로 반환, 파일의 끝(EOF)에 도달하여 더 이상 가져올 라인이 없을 경우 None을 반환
score_file = open("../score.txt", "r", encoding="utf-8")
while True:
    line = score_file.readline()
    if not line: break
    print(line, end="")
score_file.close()

# readlines() : 해당 파일의 모든 라인을 순서대로 읽어 들여 각각의 라인을 하나의 요소로 저장하는 하나의 리스트를 반환
score_file = open("../score.txt", "r", encoding="utf8")
lines = score_file.readlines()
for line in lines:
    print(line, end="")
score_file.close()

# pickle : 파이썬 객체를 직렬화(serialize)하고 역직렬화(deserialize)하기 위한 모듈.
# 피클을 사용하면 파이썬 객체를 파일에 저장하거나 네트워크를 통해 전송할 수 있다.
# 피클은 객체를 이진 형식으로 변환하여 저장하며, 나중에 필요할 때 객체를 원래의 상태로 복원 가능.
import pickle

# 객체를 직렬화하여 파일에 저장하기
data = {'name': 'Alice', 'age': 30, 'city': 'New York'}
with open('../data.pickle', 'wb') as file:
    pickle.dump(data, file)

# 파일에서 객체를 역직렬화하여 복원하기
with open('../data.pickle', 'rb') as file:
    restored_data = pickle.load(file)

print(restored_data)  # {'name': 'Alice', 'age': 30, 'city': 'New York'}