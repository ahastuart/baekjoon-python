# 학생은 30명, 출석부 번호 1~30
# 입력은 28명만 받음 . 28명을 제외한 나머지 사람의 번호를 구하기
# stud= []
# for i in range(1,11):
#     stud.append(i)
stud = [i for i in range(1,31)]
for u in range(28):
    num = int(input()) # 입력 받아서 stud에 있는 리스트 빼버리기
    stud.remove(num)

print(min(stud))
print(max(stud))