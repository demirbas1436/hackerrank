def findMedian(arr):
    # Write your code here
    new_arr = sorted(arr)
    return statistics.median(new_arr)

##################################################
# def findMedian(arr):
#     arr = sorted(arr)
#     arr_len = len(arr)
#     if arr_len % 2 == 1:
#         return arr[arr_len // 2]
#     else:
#         i = arr_len // 2
#         return (arr[i - 1] + arr[i]) / 2
##################################################