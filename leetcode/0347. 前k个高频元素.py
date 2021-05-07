import collections


class Solution:
    def topKFrequent(self, nums, k: int):
        freq = collections.Counter(nums)
        freq = list(freq.items())

        def shift_up(arr, index):
            parent = (index - 1) >> 1
            while parent >= 0 and arr[parent][1] > arr[index][1]:
                arr[parent], arr[index] = arr[index], arr[parent]
                index = parent
                parent = (index - 1) >> 1

        def shift_down(arr, index):
            n = len(arr)
            while index < n and (index << 1) + 1 < n:
                left = (index << 1) + 1
                right = left + 1
                if right < n:
                    mini = left if arr[left][1] < arr[right][1] else right
                elif left < n:
                    mini = left

                if arr[index][1] > arr[mini][1]:
                    arr[index], arr[mini] = arr[mini], arr[index]
                    index = mini
                else:
                    break

        top = freq[:k]
        for i in range(k):
            shift_up(top, i)
        for i in range(k, len(freq)):
            if freq[i][1] > top[0][1]:
                top[0] = freq[i]
                shift_down(top, 0)
        return [elem[0] for elem in top]
