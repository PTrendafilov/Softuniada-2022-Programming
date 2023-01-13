def check_subarrays(arr):
    n = len(arr)
    if n < 3:
        return "No"
    total_sum = sum(arr)
    if total_sum % 3 != 0:
        return "No"
    sub_sum = total_sum // 3
    sub_arrays = [[] for _ in range(3)]
    sub_sums = [0, 0, 0]
    def backtracka(i):
        if i == n:
            return sub_sums[0] == sub_sums[1] == sub_sums[2]
        for j in range(3):
            if sub_sums[j] + arr[i] <= sub_sum:
                sub_arrays[j].append(arr[i])
                sub_sums[j] += arr[i]
                if backtracka(i+1):
                    return True
                sub_arrays[j].pop()
                sub_sums[j] -= arr[i]
        return False
    return "Yes" if backtracka(0) else "No"
n = int(input())
for i in range(n):
    arr = list(map(int, input().split()))
    print(check_subarrays(arr))
