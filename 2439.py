# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개
# 별은 오른쪽 기준으로 정렬

star = int(input())

for i in range(1, star+1): # 일단 줄이 5줄 나와야함
    for j in range(star-i): # 공백은 4,3,2,1순
        print(end=' ')  # print가 끝나면 개행 한번 한다는 것을 생각!
    for k in range(i):
        print('*', end='')
    print('\n',end='') # 계속 end만 쓰기에는 너무 불편 ..

# 간단한 정답
# N = int(input())
# print('\n'.join(' '*(N-n) + '*'*n for n in range(1,N+1)))
# join안에 있는 것들을 \n으로 구분자로 사용해서 출력