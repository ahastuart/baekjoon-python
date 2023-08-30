# 알파벳 대소문자로 된 단어 주어짐.
# 이 단어에서 가장 많이 사용된 알파벳 ? (대문자로)
# 단, 대문자와 소문자를 구분하지 않는다.
# 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력

word = input().lower() # 입력받은 알파벳을 모두 소문자로 받음. # ex) Mississipi
sort = list(set(word)) # 중복 없도록. # ['p', 'i', 'm', 's']
c_list = []

for i in range(len(sort)):
    c_list.append(word.count(sort[i])) # [p,i,m,s]를 갯수를 세서 저장-> [1,4,4,1]

if c_list.count(max(c_list)) >= 2: # 최댓값이 두개 이상이면, '?'를 출력
    print('?')
else :
    print(sort[c_list.index(max(c_list))].upper())






