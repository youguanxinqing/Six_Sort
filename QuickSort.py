"""
快速排序
"""

def quick_sort(array, low, high):

    if low>=high:
        return

    left = low
    right = high
    key = array[left]

    while left!=right:

        while left<right and array[right]>=key:
            right -= 1
        array[left] = array[right]

        while left<right and array[left]<=key:
            left += 1
        array[right] = array[left]

    array[left] = key

    quick_sort(array, low, left-1)
    quick_sort(array, left+1, high)

if __name__ == "__main__":

    a = [1, 10, 21, 4, 9, 11]
    quick_sort(a, 0, len(a)-1)

    print(a)
