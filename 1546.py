# 세준이가 자기 점수 중에서 최대값 M
# 모든 점수를 점수/M*100으로 고침.
# 이렇게 계산했을 때, 새로운 평균 구하기

# 첫째 줄에 시험 본 과목의 개수 N
N = int(input())
# 둘째 줄에 세준이의 현재 성적
score_list = list(map(int,input().split())) # 리스트로 저장
M = max(score_list)
sum = 0

for i in range(N):
    score_list[i] = float(score_list[i]/M*100)
    sum += score_list[i]

print(sum/N)

