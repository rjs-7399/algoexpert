def jumps(nums):
    jump = 0
    maxReach = steps = nums[0]
    for i in range(1, len(nums)-1):
        maxReach = max(maxReach, nums[i]+i)
        steps -= 1
        if steps == 0:
            jump += 1
            steps = maxReach - 1
    return jump+1,maxReach

if __name__ == "__main__":
    nums = [3, 2, 1, 0, 4]
    jump,maxReach = jumps(nums)
    print(jump, maxReach)