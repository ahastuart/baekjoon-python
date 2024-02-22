# 1316
# 그룹단어체커

n = int(input()) # 몇개 받을건지 숫자 입력
group_word = n

for i in range(n): # n개의 단어 입력 받음
     word = input()
     for j in range(len(word)-1): # 그 단어의 길이 만큼 반복
         if word[j] == word[j+1]:
             continue
         elif word[j] in word[j+1:]: # 여기서는 ==이 아니라 in을 써서 간단하게 해결 !!!
             group_word -= 1 # group_word 대신에 n을 쓰게 되면 런타임 에러 !
             break

print(group_word)
