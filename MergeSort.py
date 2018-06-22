"""
归并排序
"""

def separate(array):

    if len(array)<=1:
        return array

    n = int(len(array)/2)

    left = separate(array[:n])
    right = separate(array[n:])

    return merge_sort(left, right)

def merge_sort(left, right):
    l, r = 0, 0
    result = []

    while l<len(left) and r<len(right):
        if left[l]>right[r]:
            result.append(right[r])
            r += 1
        else:
            result.append(left[l])
            l += 1

    result += left[l:]
    result += right[r:]
    return result

if __name__ == "__main__":

    a = [1, 10, 21, 4, 9, 11]

    newA = separate(a)

    print(newA)
