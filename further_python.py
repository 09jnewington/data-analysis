import statistics as stat
import sys
def summary(filename: str):
    with open(filename) as f:
        nums = []
        for line in f:
            try:
                line.strip()

                nums.append(float(line))
            except ValueError: "not a float value"
    return sum(nums), stat.mean(nums), stat.stdev(nums)

def main():
    for filename in sys.argv[1:]:
        sums, means, stdevs = summary(filename)
    print(f"{sums:.6f}, {means:.6f}, {stdevs:.6f}")
            

if __name__ == "__main__":
    main()
