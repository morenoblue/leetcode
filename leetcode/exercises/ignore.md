Put the cursor where the "|" character is and watch how this shit behaves. Absolutely heinous behaviour.

```py
class Solution:
    def topkfrequent(self, nums: list[int], k: int) -> list[int]:
        map = {}
        for i in nums:
            map[i] = map.get(i, 0) + 1

        result = []
        map = sorted(map.items(), key=lambda x: x[1], reverses=True)
        for i range(len(map)):
            if i == 0:
                result.append(map[0][0])
            elif map[i-1][1] == map[i][1]:
                result.append(map[i][0])
            |
```
            


