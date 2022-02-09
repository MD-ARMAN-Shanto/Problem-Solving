class Solution:
    def calPoints(self, ops: List[str]) -> int:
        
        record = []
        
        for op in ops:
            if op not in {'C', 'D', '+'}:
                record.append(int(op))
            elif op == "C":
                record.pop()
            elif op == "D":
                record.append(record[-1] * 2)
            else:
                record.append(sum(record[-2:]))
            
        return sum(record)
        