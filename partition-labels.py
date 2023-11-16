class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = {char: i for i, char in enumerate(s)}
        
        p = []
        f, l = 0, 0

        for i, char in enumerate(s):
            last_index = last_occurrence[char]  
            l = max(l, last_index)  
            
            if i == l:  
                p.append(i - f + 1)
                f = i + 1  

        return p