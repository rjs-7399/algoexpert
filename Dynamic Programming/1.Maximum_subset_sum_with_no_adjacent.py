def max_sum_naive(arr):
    result = [0]*len(arr)
    result[0] = arr[0]
    result[1] = max(arr[0], arr[1])

    for i in range(2, len(arr)):
        result[i] = max(result[i-1], result[i-2] + arr[i])

    return result[-1]


def max_sum_optimized(arr):
    first = arr[0]
    second = max(arr[0], arr[1])

    for i in range(2, len(arr)):
        current = max(second, first + arr[i])
        first = second
        second = current

    return second



if __name__ == "__main__":
    arr = [7, 10, 12, 7, 9, 14]

    #Naive Time complexity = O(N) | Space Complexity = O(N)
    ans_naive = max_sum_naive(arr)

    #Optimized Time complexity = O(N) | Space Complexity = O(1)
    ans_optimize = max_sum_optimized(arr)
    print(ans_naive)
    print(ans_optimize)