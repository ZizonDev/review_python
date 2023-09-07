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

