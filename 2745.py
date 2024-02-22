# 2745
# 진법변환

num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" # A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35

N,B = input().split() # B진법수 N 입력
B = int(B)
sum = 0

for i,num in enumerate(N[::-1]): # N을 거꾸로 뒤집다
    sum += num_list.index(num) * (B ** i)

print(sum)

# ?진법 -> 10진법
# 각 자리 숫자에 진법의 거듭제곱을 곱해주고 이를 모두 더한다.
# ex) ZZZZZ 36 -> 35*36^4 + 35*36^3 + ..... + 35*35^0

# ****************또다른방법********************
# n,b = input().split()
# print(int(n,int(b)))
# 문법: int(x, radix) -> radix 진수로 표현된 문자열 X를 10진수로 변환하여 리턴한다.