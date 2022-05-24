class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
                
        # sorted array
        # t_c & s_c: nlogn, n
        sorted_array = sorted(arr)
        
        # Hashmap, key, value: arrVal, index
        # t_c & s_c: n, n
        d = {}
        j = 0
        for i in range(len(sorted_array)):
            # handle the duplicate number
            if sorted_array[i] not in d:
                d[sorted_array[i]] = j + 1
                j += 1
                        
        # now compare with the original array and rank them using hashmap
        # t_c, s_c : n, n
        for i in range(len(arr)):
            arr[i] = d.get(arr[i])
                
        return arr