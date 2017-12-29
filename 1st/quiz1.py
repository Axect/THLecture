# a_n = 2*n - 1 이 수열의 20번째항 까지의 합을 구하세요.

def main():
    print(sumList(20))

def sumList(n):
    a = [2*i - 1 for i in range(1, n+1)]
    return sum(a)

if __name__ == "__main__":
    main()
