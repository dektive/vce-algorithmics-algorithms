def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            print(left[i])
            i += 1
        else:
            result.append(right[j])
            print(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result


def QuickSort(arr):
    elements = len(arr)

    # Base case
    if elements < 2:
        return arr

    current_position = 0  # Position of the partitioning element

    for i in range(1, elements):  # Partitioning loop
        if arr[i] <= arr[0]:
            current_position += 1
            temp = arr[i]
            arr[i] = arr[current_position]
            arr[current_position] = temp

    temp = arr[0]
    arr[0] = arr[current_position]
    arr[current_position] = temp  # Brings pivot to it's appropriate position

    left = QuickSort(arr[0:current_position])  # Sorts the elements to the left of pivot
    right = QuickSort(arr[current_position + 1:elements])  # sorts the elements to the right of pivot

    arr = left + [arr[current_position]] + right  # Merging everything together

    return arr


def mergeSort(sequence):
    length = len(sequence)
    middle = (length / 2).__floor__()
    if length == 1:
        return sequence

    else:
        return merge(mergeSort(sequence[middle:]), mergeSort(sequence[:middle]))


if __name__ == '__main__':
    yeehaw = [3.5, 34, 7, 1, 3, 2, 9, 5, 3, 1]
    print(mergeSort(yeehaw))
