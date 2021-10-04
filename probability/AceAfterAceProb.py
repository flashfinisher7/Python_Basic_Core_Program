"""
@Author: Anil
@Date: 2021-10-02 02:55
@Last Modified by: Anil
@Last Modified time: 2021-10-02 03:05
@Title : The probability of drawing an ace after drawing a ace on
the first draw
"""
cards=52
aces=4
probability_firstAce=aces/cards
probability_SecondAce=(aces-1)/(cards-1)
probability_ace=probability_firstAce*probability_SecondAce
print("Probability Of Ace After drawing one Ace:",probability_ace)