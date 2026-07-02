# Problem : String Compression
# Topic : Array / String

class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        count = 1
        for i in range(1,len(chars)):
            if chars[i] == chars[i - 1]:
                count += 1
            else:
                if count == 1:
                    s += chars[i-1]
                else:
                    s += chars[i - 1] + str(count)
                count = 1

        s += chars[-1]
        if count > 1:
            s += str(count)
        chars[:] = list(s)
        return len(chars)    
