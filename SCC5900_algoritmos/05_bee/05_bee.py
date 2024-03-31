
if __name__ == "__main__":
    n_bee = int(input())
    bees = input()
    bees = bees.split()
    sums = set()
    
    for i in range(n_bee):
        bee = int(bees[i])
        current_sums = list(sums)
        for sum in current_sums:
            sums.add(sum+bee)
        sums.add(bee)
    print(len(sums))
