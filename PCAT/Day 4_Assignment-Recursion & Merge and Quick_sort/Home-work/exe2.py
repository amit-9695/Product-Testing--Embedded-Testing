# Merge Sort Implementation with Comparison Count
class MergeSorter:
    def __init__(self):
        self.comparisons = 0

    def _merge(self, a, start, mid, end):
        """Merge [start, mid) and [mid, end) in-place using a temp buffer."""
        left, right = start, mid
        temp = []
        while left < mid and right < end:
            self.comparisons += 1
            if a[left] <= a[right]:
                temp.append(a[left]); left += 1
            else:
                temp.append(a[right]); right += 1
        temp.extend(a[left:mid])
        temp.extend(a[right:end])

        # copy back
        for i, val in enumerate(temp):
            a[start + i] = val

    def _sort(self, a, start, end):
        if end - start > 1:
            mid = (start + end) // 2
            self._sort(a, start, mid)
            self._sort(a, mid, end)
            self._merge(a, start, mid, end)

    def sort(self, arr):
        a = list(arr)           # copy to avoid side-effects
        self.comparisons = 0
        self._sort(a, 0, len(a))
        return a, self.comparisons

if __name__ == "__main__":
    nums = [34, 7, 23, 32, 5, 62]
    sorter = MergeSorter()
    sorted_nums, cnt = sorter.sort(nums)
    print("Original :", nums)
    print("Sorted   :", sorted_nums)
    print("Comparisons:", cnt)