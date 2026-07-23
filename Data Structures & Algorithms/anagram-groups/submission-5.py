class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash=defaultdict(list)

        for word in strs:
            anagram=''.join(sorted(word))
            hash[anagram].append(word)
        
        return list(hash.values())
