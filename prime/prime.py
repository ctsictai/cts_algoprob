import sys

sys.stdin = open("input.txt", "r")

num = int(input())


def prime_list(n):
    sieve = [True] * n
    m = int(n**0.5)  # 2,3,4 까지 확인 하면 나머지 소수에 대한 배수도 모두 확인가능
    print(m)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i + i, n, i):  # i 이후 i 배수 false 판정
                sieve[j] = False
    print(sieve)
    return [i for i in range(2, n) if sieve[i] == True]


a = prime_list(num)
print(a)


# 에라토스테네스의 체
# 자연수 N까지의 소수 개수 구하기

n = int(input())
ch = [0] * (n + 1)
cnt = 0

for i in range(2, n + 1):
    if ch[i] == 0:
        cnt += 1
        for j in range(i, n + 1, i):
            ch[j] = 1

print(cnt)
