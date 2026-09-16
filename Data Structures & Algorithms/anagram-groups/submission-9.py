class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs: 
            letters = tuple(sorted(word))
            x = seen.get(letters)
            if x is not None:
                seen[letters].append(word)
            else:
                seen[letters]= [word]
        return list(seen.values())


