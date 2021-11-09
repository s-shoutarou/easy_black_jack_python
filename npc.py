from card import Card

class Npc:
  __amount = 0
  __cards = []

  def __init__(self,deck) -> None:
    self.__getInitCards(deck)
    self.checkPossessionCards()

  def __getInitCards(self,deck):
    for num in range(2):
      self.draw(deck)

  def draw(self, deck):
      self.__cards.append(deck.drawCard())
      self.checkPossessionCards()

  def getAmount(self):
    return self.__amount

  def checkPossessionCards(self):
    amount = 0
    for card in self.__cards:
      amount += card.num if(card.num <= 10) else 10
    self.__amount = amount