class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cnt = defaultdict(int)

        for w in words[0]:
            cnt[w] += 1

        for i in range(1, len(words)):
            cur_count = defaultdict(int)
            for w in words[i]:
                cur_count[w] += 1
            for c in cnt:
               cnt[c]= min(cnt[c], cur_count[c])

        res = []
        for c in cnt:
            for i in range(cnt[c]):
                res.append(c)
        return res
            

