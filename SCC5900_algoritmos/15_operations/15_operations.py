def reduce(num, div):
    if num == 0:
        return -1
    return reduce(num // div, div) + 1 + num % div

if __name__ == "__main__":
    cases = int(input())
    for i in range(cases):
        goal, step = map(int, input().split())
        print(reduce(goal, step))