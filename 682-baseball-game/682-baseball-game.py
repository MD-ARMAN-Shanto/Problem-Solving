class Solution:
    def calPoints(self, ops: List[str]) -> int:
        
        record = []
        
        for op in ops:
            if op not in {'C', 'D', '+'}:
                record.append(int(op))
            if op == "C":
                record.pop()
            if op == "D":
                record.append(record[-1] * 2)
            if op == "+":
                record.append(sum(record[-2:]))
            
        return sum(record)
        