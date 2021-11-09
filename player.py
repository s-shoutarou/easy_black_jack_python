from card import Card

class Player:
  __amount = 0
  __cards = []

  def __init__(self,deck) -> None:
    self.__setInitCards(deck)
    self.checkPossessionCards()

  def __setInitCards(self,deck):
    for num in range(2):
      self.draw(deck)

  def getAmount(self):
    return self.__amount

  def draw(self,deck):
      self.__cards.append(deck.drawCard())

  def checkPossessionCards(self):
    amount = 0

    for card in self.__cards:

      #絵札はいずれも10扱い
      amount += card.num if(card.num <= 10) else 10
      print('{}の{}を持っています'.format(card.mark, card.num))

    self.__amount = amount
    print ('現在の合計値は{}です'.format(self.__amount))

