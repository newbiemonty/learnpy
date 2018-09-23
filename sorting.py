"""Bubble sort"""


# class SortingAlgorithms:
def bubble_sort(array):
    for elem in range(len(array)):
        for i in range(len(array) - elem - 1):
            if array[i] > array[i + 1]:
                array[i + 1], array[i] = array[i], array[i + 1]


def rec_bubble_sort(array, end_index):
    if end_index <= 0:
        return

    for elem in range(end_index - 1):
        if array[elem] > array[elem + 1]:
            array[elem + 1], array[elem] = array[elem], array[elem + 1]

    rec_bubble_sort(array, end_index - 1)


# array = [11, 2]#5, 6, 3, 1, 4]
# bubble_sort(array)
# rec_bubble_sort(array, len(array))
# print(array)


def insertion_sort(array):
    for i in range(1, len(array)):
        j = i - 1
        key = array[i]
        while j >= 0:
            if key < array[j]:
                array[j + 1] = array[j]
            else:
                break
            j -= 1
        array[j + 1] = key


def recursive_insertion_sort(array, i):
    if i >= len(array):
        return

    j = i - 1
    key = array[i]
    while j >= 0:
        if key < array[j]:
            array[j + 1] = array[j]
        else:
            break
        j -= 1
    array[j + 1] = key

    recursive_insertion_sort(array, i + 1)


# array = [11,2,3,5,7,4,9,0]
# insertion_sort(array)
# recursive_insertion_sort(array, 1)
# print(array)


def find_min_index(array, start_index):
    if start_index == len(array) - 1:
        return start_index

    min_index = start_index
    for i in range(start_index + 1, len(array)):
        if array[i] < array[min_index]:
            min_index = i

    return min_index


def selection_sort(array):
    for i in range(len(array)):
        for j in range(len(array)):
            min_index = find_min_index(array, i)
            array[i], array[min_index] = array[min_index], array[i]


# array = []#[11,2,3,5,7,4,9,0]
# selection_sort(array)
# print(array)


def merge_arrays(array, start_index, mid, end_index):
    i = start_index;
    j = mid + 1;
    k = start_index
    final_arr = [i for i in array]

    while i <= mid and j <= end_index:
        if array[i] < array[j]:
            final_arr[k] = array[i]
            k += 1;
            i += 1;
        else:
            final_arr[k] = array[j]
            k += 1;
            j += 1;

    while i <= mid:
        final_arr[k] = array[i]
        k += 1
        i += 1

    while j <= end_index:
        final_arr[k] = array[j]
        k += 1
        j += 1

    for i in range(start_index, end_index + 1):
        array[i] = final_arr[i]


def merge_sort_internal(array, start_index, end_index):
    if start_index >= end_index:
        return

    mid = start_index + int((end_index - start_index) / 2)
    merge_sort_internal(array, start_index, mid)
    merge_sort_internal(array, mid + 1, end_index)

    merge_arrays(array, start_index, mid, end_index)


def merge_sort(array):
    merge_sort_internal(array, 0, len(array) - 1)
    print(array)


# array = [11,2,3,5,7,4,9,0]
# merge_sort(array)

def partition(array, low, high):
    pivot_elem = array[low]

    i = low
    j = high

    while (1):
        while array[i] < pivot_elem:
            i += 1

        while array[j] > pivot_elem:
            j -= 1

        if i >= j:
            return j

        array[i], array[j] = array[j], array[i]


def quick_sort_internal(array, start_index, end_index):
    if start_index >= end_index:
        return

    pivot_index = partition(array, start_index, end_index)
    quick_sort_internal(array, start_index, pivot_index - 1)
    quick_sort_internal(array, pivot_index + 1, end_index)


def quick_sort(array):
    quick_sort_internal(array, 0, len(array) - 1)
    print(array)


# array = [11,2,35,5,7,4,9,0]
# print(array)
# quick_sort(array)


"""Dutch flag"""


def dutch_flag_sort(array):
    i = 0;
    j = 0;
    k = len(array) - 1

    while j < k:
        if array[j] == 0:
            array[i], array[j] = array[j], array[i]
            i += 1;
            j += 1

        if array[j] == 2:
            array[k], array[j] = array[j], array[k]
            k -= 1

        if array[j] == 1:
            j += 1


array = [1, 0, 2, 1, 1, 1, 2, 2, 2, 0, 0, 2]
dutch_flag_sort(array)
print(array)
array = [1, 0, 1, 1, 1, 0, 0, 1]
dutch_flag_sort(array)
print(array)
array = [2, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2]
dutch_flag_sort(array)
print(array)
array = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
dutch_flag_sort(array)
print(array)
array = [0] * 8
dutch_flag_sort(array)
print(array)
array = [1] * 8
dutch_flag_sort(array)
print(array)
