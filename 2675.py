# 문자열 s를 입력 받음
# 각 문자를 R번 반복해서 새 문자열 P를 만듦

# 테스트 케이스의 개수 T
T = int(input())

for i in range(T):
    R, S = input().split() # 반복횟수 R, 문자열 S
    for j in S:
        print(j*int(R), end="") # 문자열을 옆으로 붙이면서 출력
    print(" ") # 줄넘김

# 문자열은 내용을 변경하는 방법이나 메소드를 제공하지 않습니다.
# print(j*R)이 안됐던 이유 : R는 int형이 아닌 str형이다. 즉, int형으로 바꿔야지 가능
# 줄 넘김하는 이유 : print에서 end파라미터를 이용하지 않으면 줄 넘김 기능이 기본값