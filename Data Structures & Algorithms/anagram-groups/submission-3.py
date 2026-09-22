class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        anagram is str that has same chars but differnt ordering
        we have an input of a list and we want an output of a list inside a list


        """
        groups = {}

        for word in strs:
            count = [0] * 26

            for char in word:
                index = ord(char) - ord('a')
                count[index] +=1

            key = tuple(count)
            
            if key not in groups:
                groups[key] = []
            
            groups[key].append(word)

        return list(groups.values())
