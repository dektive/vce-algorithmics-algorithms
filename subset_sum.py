def subset_sum(available: list, target):
    if target == 0:
        return [[]]

    if not available or target < 0:
        return []

    last_element = available[-1]
    with_last_element_removed = available[:-1]

    without_last_element = [[last_element] + subset for subset in subset_sum(with_last_element_removed, target - last_element)]
    with_last_element = subset_sum(with_last_element_removed, target)

    return with_last_element + without_last_element


if __name__ == '__main__':
    from pprint import pprint
    available = [1, 2, 3, 4, 5]
    target = 6
    result = subset_sum(available, 6)
    pprint(result)
