if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    arr.reverse()
    result=' '.join(map(str,arr))
    print(result)