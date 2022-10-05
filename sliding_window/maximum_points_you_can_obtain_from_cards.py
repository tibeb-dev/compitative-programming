class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        outPut = 0
        if k == len(cardPoints):
            for i in range(len(cardPoints)):
                outPut += cardPoints[i]
        else:
            for i in range(k):
                # print(cardPoints)
                # print(outPut)
                if cardPoints[0] == cardPoints[-1] :
                    outPut += cardPoints[0]
                    if cardPoints[1] > cardPoints[-2]:
                        cardPoints.pop(0)
                    elif cardPoints[1] < cardPoints[-2]:
                        cardPoints.pop()
                    else:
                        cardPoints.pop(0)
                    # elif cardPoints[1] < cardPoints[-2]:
                    #     cardPoints.pop(0)
                elif cardPoints[0] < cardPoints[-1]:
                    outPut += cardPoints[-1]
                    cardPoints.pop()
                elif cardPoints[0] > cardPoints[-1]:
                    outPut += cardPoints[0]
                    cardPoints.pop(0)
        return outPut