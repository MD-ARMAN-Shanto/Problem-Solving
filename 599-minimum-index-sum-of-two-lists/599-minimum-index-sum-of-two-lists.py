class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        d1 = {restaurant:i for i, restaurant in enumerate(list1)}
        d2 = {restaurant:d1[restaurant]+i for i, restaurant in enumerate(list2) if restaurant in d1}

        MIN = float('inf')
        res = []

        for key, val in d2.items():
            if val < MIN:
                res = [key]
                MIN = val
            elif val == MIN:
                res.append(key)

        return res