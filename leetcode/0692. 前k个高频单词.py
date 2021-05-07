import collections


class Solution:
    # 法一: 排序
    def topKFrequent(self, words, k: int):
        freq = collections.Counter(words)
        freq = list(freq.items())
        freq = sorted(freq, key=lambda x: (-x[1], x[0]))
        return [item[0] for item in freq[:k]]

    # 法二: 最小堆
    def topKFrequent2(self, words, k: int):
        freq = collections.Counter(words)
        freq = list(freq.items())

        def shift_up(arr, index):
            parent = (index - 1) >> 1
            while parent >= 0 and cmp(top, index, parent):
                arr[parent], arr[index] = arr[index], arr[parent]
                index = parent
                parent = (index - 1) >> 1

        def shift_down(arr, index):
            n = len(arr)
            while index < n and (index << 1) + 1 < n:
                left = (index << 1) + 1
                right = left + 1
                if right < n:
                    mini = left if cmp(top, left, right) else right
                elif left < n:
                    mini = left

                if cmp(top, mini, index):
                    arr[index], arr[mini] = arr[mini], arr[index]
                    index = mini
                else:
                    break

        def cmp(arr, index1, index2):
            return arr[index1][1] < arr[index2][1] or (arr[index1][1] == arr[index2][1] and arr[index1][0] > arr[index2][0])

        top = freq[:k]
        for i in range(k):
            shift_up(top, i)
        for i in range(k, len(freq)):
            if freq[i][1] > top[0][1] or (freq[i][1] == top[0][1] and freq[i][0] < top[0][0]):
                top[0] = freq[i]
                shift_down(top, 0)
        ans = []
        for i in range(k):
            top[0], top[-1] = top[-1], top[0]
            ans.append(top[-1][0])
            top.pop(-1)
            shift_down(top, 0)
        return ans[::-1]
