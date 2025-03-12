with open('sample.txt') as f:
    nums = []
    for line in f:
        nums.append(float(line.strip()))
    print(nums)