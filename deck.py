import random
from card import Card

class Deck:
  MARKS = [
    'ハート',
    'スペード',
    'ダイア',
    'クローバー'
  ]
  def __init__(self) -> None:
    deck = []
    for mark in self.MARKS:
      deck    = [*deck, *self.__makeCards(mark)]
    self.deck = random.sample(deck,len(deck))

  def __makeCards(self,mark):
    cards = []
    for num in range(13):
      cards.append(Card(mark,num + 1))
    return cards

  def drawCard(self):
    return self.deck.pop(0)