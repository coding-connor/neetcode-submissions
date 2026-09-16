class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        outcome = []
        for word in strs: 
            letters = str(sorted(word))
            x = seen.get(letters)
            if x is not None:
                outcome[x].append(word)
            else:
                outcome.append([word])
                index = len(outcome) - 1
                seen[letters] = index 
        return outcome


