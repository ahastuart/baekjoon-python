# 9x9 격자판에 쓰여진 81개의 자연수 또는 0
# 이 중 최댓값을 찾고 몇 행 몇 열인지 구하기

# 보통 input()으로 문자열 값을 입력받지만
# 반복문으로 여러 줄을 입력받아야 할 때는 시간 초과 문제가 발생할 수 있음.

import sys
input = sys.stdin.readline

A = []
max,r,c = 0,0,0

for i in range(9):
    A.append(list(map(int,input().split())))
    # [[8, 9, 7], [7, 8, 9], [8, 9, 6]] 이런 식으로 저장.

# print(max(map(max, A))) #이것으로는 2차원 배열에서 최댓값을 찾을 수 있으나 몇행몇열인지는 알 수 없다.

# 푸는 아이디어 : max를 0으로 두고, 9x9행렬을 차례대로 살펴보면서 큰값일 때마다 계속 업데이트 !
for j in range(9): # 행
    for k in range(9): # 열
        if A[j][k] > max:
            max = A[j][k] # 업데이트
            r = j
            c = k

print(max)
print(r+1,c+1)







