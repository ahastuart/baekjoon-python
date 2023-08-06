# N개의 정수 중에서 최댓값과 최솟값 찾기

N = int(input()) # 정수의 개수
n_list = list(map(int, input().split()))
print(min(n_list), max(n_list))
