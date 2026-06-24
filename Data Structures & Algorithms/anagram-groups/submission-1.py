class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sets = {}
        final = []
        for word in strs:
            frame = {}
            for letter in word:
                if letter in frame:
                    frame[letter] += 1
                else :
                    frame[letter] = 1
            frame = frozenset(frame.items())        
            if frame in sets.keys():
                sets[frame].append(word)
            else:
                sets[frame] = [word]
        for key in sets.keys():
            final.append(sets[key])

        return final