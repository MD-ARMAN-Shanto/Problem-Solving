class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        queue = collections.deque(students)
        
        for sandwich in sandwiches:
            if sandwich in queue:
                while queue[0] != sandwich:
                    val = queue.popleft()
                    queue.append(val)
                queue.popleft()
            else:
                return len(queue)
            
        return 0
                
                    