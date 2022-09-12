class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        tokens.sort()
        
        if not tokens or tokens[0] > power:
            return 0
        
        left, right = 0, len(tokens) - 1
        max_score, curr_score = 0, 0
        
        while left <= right:
            
            if tokens[left] <= power:
                power -= tokens[left]
                curr_score += 1
                left += 1
            else:
                power += tokens[right]
                curr_score -= 1
                right -= 1
                
            max_score = max(max_score, curr_score)
                    
                    
        return max_score
        
        