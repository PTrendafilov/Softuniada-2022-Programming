def sort_array(arr):
    for i in range(len(arr)-1):
        if i % 2 == 0:
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        else:
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr
n = int(input())
arr = list(map(int, input().split()))
sorted_arr = sort_array(arr)
for el in sorted_arr:
    print(el, end=' ')
