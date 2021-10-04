"""
@Author: Anil
@Date: 2021-10-02 04:55
@Last Modified by: Anil
@Last Modified time: 2021-10-02 05:00
@Title : The probability of drawing an ace after drawing a king on
the first draw
"""
cards=52
aces=4
kings=4
probability_king=kings/cards
probability_ace=aces/(cards-1)
probability_ace_after_king=probability_king*probability_ace
print("Probability Of Ace After drawing one King:",probability_ace_after_king)