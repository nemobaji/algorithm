class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = []
        cnt = []

        for word in re.findall(r'\w+', paragraph.lower()):
            if word in banned:
                continue
            if word in words:
                cnt[words.index(word)] += 1
            else:
                words.append(word)
                cnt.append(1)
        
        return words[cnt.index(max(cnt))]
