# -----------------------
# Date       : 22/10/2025
# Self Solved: False
# Topics     : 
# Big O      : O(n)
# -----------------------

class Solution:

    def encode(self, strs: list[str]) -> str:
        encoded_string = ""
        for string in strs:
            delimiter = str(len(string)) + "#"
            encoded_string += delimiter + string
        return encoded_string

    def decode(self, s: str) -> list[str]:
        c = 0
        decoded_string = []

        while c < len(s):
            size = ""

            while s[c] != "#":
                size += str(s[c])
                c += 1

            size = int(size)
            decoded_string.append(s[ c+1 : c+1+size ])
            c = c+1+size

        return decoded_string

solution = Solution()

print(solution.encode(["we","say",":","yes","!@#$%^&*()"]))
print(solution.decode(solution.encode(["we","say",":","yes","!@#$%^&*()"])))


