from math import ceil

def merge(first_list, second_list):
    new_list = list()
    i = 0
    j = 0
    i_max = len(first_list) - 1
    j_max = len(second_list) -1
    while i <= i_max and j <= j_max:
        if first_list[i] < second_list[j]:
            new_list.append(first_list[i])
            i += 1
        elif first_list[i] > second_list[j]:
            new_list.append(second_list[j])
            j += 1
        else:
            new_list.append(first_list[i])
            new_list.append(second_list[j])
            i += 1
            j += 1
    if i > i_max:
        new_list += second_list[j:]
    if j > j_max:
        new_list += first_list[i:]
    return new_list

def mergeSort(li):
    if len(li) == 1:
        return li
    else:
        n = ceil(len(li) // 2)
        left_half = mergeSort(li[0:n])
        right_half = mergeSort(li[n:])
        return merge(left_half, right_half)

# examples
if __name__ == "__main__":
    # print(merge([1, 3, 5], [2, 3, 7]))
    # print(mergeSort([5, 3]))
    print(merge([2], [2]))
    print(merge([9], [1, 2]))
    print(mergeSort([5, 3, 2, 9]))