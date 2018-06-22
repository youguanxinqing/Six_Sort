"""
冒泡排序
"""

def bubble_sort(array):

    n = len(array)
    for i in range(n):

        count = 0
        for j in range(1, n-i):
            if array[j-1]>array[j]:
                array[j-1], array[j] = array[j], array[j-1]
                count += 1

        if count == 0:
            break


if __name__ == "__main__":

    a = [1, 10, 21, 4, 9, 11]
    bubble_sort(a)

    print(a)
