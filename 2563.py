# 가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지에
# 가로, 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이를 붙일 때
# 색종이가 붙은 검은 영역의 넓이를 구하는 프로그램

N = int(input()) # 색종이의 수
# 2차원 배열을 이용하자 !
# 흰색 도화지가 1*1인 정사각형 100개로 이루어졌다고 생각.
white = [[0 for ww in range(100)] for w in range(100)]
# whilte = [[0]*100 for w in range(100)]

for i in range(N):
    x, y = map(int, input().split())
    for j in range(x,x+10):
        for k in range(y, y+10):
            white[j][k] = 1 # 입력받은 그 범위 만큼은 1로 바꾼다.

count = 0
# for c in white:
#     if 1 in c:
#         count +=1
for c in white:
    count += c.count(1)

print(count)
# 도화지의 영역을 처음에 어떻게 계산해야하지 막막했었는데
# 2차원 배열로 만들어서 모두 0으로 초기화 해놓고
# 해당 부분만 1로 만들어서 count한다는 아이디어가 좋은 것 같다.
# 앞으로 이런 좋은 아이디어를 생각할 수 있도록 노력 !!!


