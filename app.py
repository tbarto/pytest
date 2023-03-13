def runningSum(nums):
    sum = 0
    arr = []
    for i in nums:
        sum += i
        arr.append(sum)
    return arr

# def main():
#     nums = []
#     print(runningSum(nums))
