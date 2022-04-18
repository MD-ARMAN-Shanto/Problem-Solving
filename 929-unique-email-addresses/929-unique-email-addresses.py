class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        D = set()
        for x in emails:
            a,b = x.split('@')
            a   = a.split('+')[0]
            a   = a.replace('.','')
            D.add( (a,b) )
        return len(D)