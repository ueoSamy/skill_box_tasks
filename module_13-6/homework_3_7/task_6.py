def merge_sorted_lists(list1, list2):
    i = 0
    j = 0
    merged = []

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            if not merged or list1[i] != merged[-1]:
                merged.append(list1[i])
            i += 1
        elif list1[i] > list2[j]:
            if not merged or list2[j] != merged[-1]:
                merged.append(list2[j])
            j += 1
        else:
            if not merged or list1[i] != merged[-1]:
                merged.append(list1[i])
            i += 1
            j += 1

    while i < len(list1):
        if not merged or list1[i] != merged[-1]:
            merged.append(list1[i])
        i += 1

    while j < len(list2):
        if not merged or list2[j] != merged[-1]:
            merged.append(list2[j])
        j += 1

    return merged
