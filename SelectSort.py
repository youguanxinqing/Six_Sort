"""
选择排序
"""

def select_sort(array):

    for i in range(len(array)):

        min_index = i
        for j in range(i, len(array)):
            if array[min_index]>array[j]:
                min_index = j

        if min_index!=i:
            array[min_index], array[i] = array[i], array[min_index]


if __name__ == "__main__":

    a = [1, 10, 21, 4, 9, 11]
    select_sort(a)

    print(a)