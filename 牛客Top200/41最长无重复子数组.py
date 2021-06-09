class Solution:
    # 用队列：当前数字在队列中，则一直出队知道当前元素不在队中，然后将当前元素入队。
    # 每入队一个元素都要计算当前队长度，返回值即是队列长度的最大值。
    def maxLength(self , arr ):
        n = len(arr)
        if n < 2: return n
        queue = []
        ans = 0
        for number in arr:
            while number in queue:
                queue.pop(0)
            queue.append(number)
            ans = max(ans, len(queue))
        return ans