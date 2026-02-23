class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:

        map = defaultdict(set)


        for a,b in similarPairs:
            map[a].add(b)
            map[b].add(a)
        
        print(map)

        if len(sentence1) != len(sentence2):
            return False
        

        for i in range(len(sentence1)):
            if sentence1[i] == sentence2[i]:
                continue
            else:
                if (sentence1[i] not in map) or (sentence2[i] not in map[sentence1[i]]):
                    return False


        return True
        