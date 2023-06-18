import random 
import statistics

coin = random.choice(["heads", "tails"])
print(coin)

number = random.randint(1, 10)
print(number)

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards: 
    print(card)

print(statistics.mean([100, 90]))
