class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words = words[::-1]

        index = 0
        sentence = ''
        while index <= len(words)-1:
            sentence += words[index] + ' '

            index += 1
        sentence = sentence.strip()

        return sentence
    
