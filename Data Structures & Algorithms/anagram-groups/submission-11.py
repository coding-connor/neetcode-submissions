class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs: 
            count = [0] * 26
            for letter in word:
                index = ord(letter) - ord('a')
                count[index] += 1
            count = tuple(count)
            x = seen.get(count)
            if x is not None:
                seen[count].append(word)
            else:
                seen[count]= [word]
        return list(seen.values())


