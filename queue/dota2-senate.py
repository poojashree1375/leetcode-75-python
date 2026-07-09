# Problem : Dota2 Senate
# Topic : Queue

from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque()
        dire = deque()

        for i in range(len(senate)):
            if senate[i] == "R":
                radiant.append(i)
            else:
                dire.append(i)
        while radiant and dire:
            if radiant[0] < dire[0]:
                winner = radiant.popleft()
                dire.popleft()
                radiant.append(winner + len(senate))
            else:
                winner = dire.popleft()
                radiant.popleft()
                dire.append(winner + len(senate))

        if len(radiant) > 0:
            return "Radiant"
        else:
            return "Dire"
