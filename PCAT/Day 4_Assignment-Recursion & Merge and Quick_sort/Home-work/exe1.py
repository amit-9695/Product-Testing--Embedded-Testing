# Merge Sort Implementation
def merge_sort(arr):
    """Classic top-down merge sort (returns a new sorted list)."""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left  = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # merge two sorted halves
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

if __name__ == "__main__":
    raw = input("Enter integers separated by spaces: ")
    nums = list(map(int, raw.split()))
    print("Sorted:", *merge_sort(nums))