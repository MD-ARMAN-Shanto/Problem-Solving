class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        files = defaultdict(list)
        
        for path in paths:
            directory = path.split(' ')[0]
            
            for file in path.split(' ')[1:]:
                start, end = file.find('('), file.find(')')
                content = file[start+1:end]
                
                files[content].append(f'{directory}/{file[:start]}')
                
        return [val for val in files.values() if len(val) > 1]