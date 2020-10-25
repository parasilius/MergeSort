from math import ceil
import sys
import time

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        # 0.25 is so slow..so I changed it to 0.15
        time.sleep(0.1)

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
    delay_print(f"\nOhhh, wait...\nI have to sort {li}!")
    time.sleep(1)
    if len(li) == 1:
        delay_print("\nBut this has only one item...")
        delay_print("\nWhich means it's already sorted...!!!")
        time.sleep(0.4)
        delay_print("\nLet's get back to where I came...")
        time.sleep(1)
        return li
    else:
        n = ceil(len(li) // 2)
        left_half = li[0:n]
        right_half = li[n:]
        delay_print(f"\nI will divide it into two halves!...")
        time.sleep(0.5)
        delay_print(f"\nThe left half is {left_half}")
        delay_print(f"\nAnd the right half is {right_half}")
        time.sleep(0.4)
        delay_print("\nNow I have to sort the left half...")
        time.sleep(0.5)
        delay_print("\nBut how??!!")
        time.sleep(0.5)
        delay_print("\nLet's start over...")
        time.sleep(1)
        left_half = mergeSort(left_half)
        delay_print("\nOK...Now that the left half is sorted...")
        delay_print(f"\nLet's sort the right half...which is {right_half}...")
        time.sleep(0.5)
        delay_print("\nBut how??!!")
        time.sleep(0.5)
        delay_print("\nLet's start over...")
        time.sleep(1)
        right_half = mergeSort(right_half)
        delay_print(f"\nOK...Now that {left_half} and {right_half} are both sorted...")
        delay_print("\nIt's time to merge them!!!")
        time.sleep(0.5)
        delay_print(f"\nHere we gooo...!\n{merge(left_half, right_half)}\n")
        time.sleep(1)
        return merge(left_half, right_half)

if __name__ == "__main__":
    # A good list is [5, 3, 2, 9]
    s = input("Give me some numbers and I will sort them for you: ")
    try:
        list_to_sort = [int(i) for i in s.split()]
        print(mergeSort(list_to_sort))
    except:
        print("Give me a valid list!!!")
