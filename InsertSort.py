"""
插入排序
"""

def insert_sort(array):

    for i in range(1, len(array)):
        j = i-1
        temp = array[i]

        while j>=0 and array[j]>temp:
            array[j+1] = array[j]
            j -= 1

        array[j+1] = temp


if __name__ == "__main__":

    a = [1, 10, 21, 4, 9, 11]
    insert_sort(a)

    print(a)