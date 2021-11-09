from deck import Deck
from player import Player
from npc import Npc

if __name__ == '__main__':
  deck   = Deck()
  player = Player(deck)
  npc    = Npc(deck)

while(True):
  print('カードを引くならdを、今の手札で勝負するならsを入力してEnterキーを押下してください')
  str = input()
  if(str == 'd'):
    player.draw(deck)
    player.checkPossessionCards()
    if(player.getAmount() >= 21):
      print('カードの合計値が21を越えました。あなたの負けです')
      quit()
  else:
    break

while(True):
  if(npc.getAmount() <= 12):
    npc.draw(deck)
  elif(npc.getAmount() >= 21):
    print('NPCの合計値が21を超えたためあなたの勝ちです')
    quit()
  else:
    break

print('あなたの合計値:{}'.format(player.getAmount()))
print('NPCの合計値:{}'.format(npc.getAmount()))
if(player.getAmount() > npc.getAmount()):
  print('あなたの勝ちです')
elif(player.getAmount() < npc.getAmount()):
  print('あなたの負けです')
elif(player.getAmount() == npc.getAmount()):
  print('引き分けです')
