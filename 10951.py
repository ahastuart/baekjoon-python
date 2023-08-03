# 두 정수 A와 B를 입력, A+B를 출력
# 입력은 여러 개의 테스트 케이스
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에는 A와 B가 주어진다.

while True: # 무한 반복
    try:
        A, B = map(int,input().split()) # map(function, iterable)
        print(A+B)
    except: # 오류가 발생하면 break
        break