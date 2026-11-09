class Solution:
    def encode(self, strs: List[str]) -> str:
        answer = ""
        for str_ in strs:
            answer += str(len(str_)) +'#'+str_
        # print(answer)
        return answer


    def decode(self, s: str) -> List[str]:

        answer = []
        i = 0
        while i < len(s):
            j = i
            while s[j]!='#':
                j+=1

            length = int(s[i:j])
            if j+length == len(s)-1:
                str_ = str(s[j+1: j+length+1])
                answer.append(str_)
                break
            else:
                str_ = str(s[j+1: j+length+1])
                answer.append(str_)
                i = j+1+length

        return answer
