class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            sort = "".join(sorted(word))
            if sort not in groups:
                groups[sort] = []
            groups[sort].append(word)
        return list(groups.values())