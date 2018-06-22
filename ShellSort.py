"""
希尔排序
"""

def shell_sort(array):

    d = int(len(array)/2)

    while d>0:
        for i in range(d, len(array)):
            j = i
            while j>=d and array[j-d]>array[j]:
                array[j-d], array[j] = array[j], array[j-d]
                j -= d

        d = int(d/2)

if __name__ == "__main__":

    a = [1, 10, 21, 4, 9, 11]
    shell_sort(a)

    print(a)

