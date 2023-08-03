# N * M 크기의 두 행렬 A와 B을 더해라
# 첫째 줄에 (N개의 줄, 원소 M개)N과 M 입력
# 둘째 줄에 각 원소 차례대로

N,M = map(int, input().split())
A_list = []
B_list = []

for i in range(N):
    A_list.append(list(map(int, input().split())))

for j in range(N):
    B_list.append(list(map(int, input().split())))

for n in range(N):
    for m in range(M):
        print(A_list[n][m] + B_list[n][m], end=' ')
    print()


