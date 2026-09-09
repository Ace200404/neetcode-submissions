class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        valueMap=Counter(hand)

        for num in hand:
            if valueMap[num]:
                for i in range(num,num+groupSize):
                    if not valueMap[i]:
                        return False
                    valueMap[i]-=1
        return True