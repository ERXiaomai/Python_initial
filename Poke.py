# 一付扑克牌，去掉大小王，每个玩家发3张牌，最后比大小，看谁赢，
# 有以下几种牌
# 豹子: 三张一样的牌，如3张6.如红桃5、6、7同花顺: 即3张同样花色的顺子
# 顺子:又称拖拉机，花色不同，但是顺子，如红桃5、方片6、黑桃7，组成的顺子对子:2张牌一样单张: 单张最大的是A这几种牌的大小顺序为，豹子>同花顺>同花>顺子>对子>单张
# 需程序实现的点:
# 1.先生成一付完整的扑克牌
# 2.给5个玩家随机发牌
# 3.统一开牌，比大小，输出赢家是谁
import random
num_player = 5
poke = []
player = []
for i in range(1,14):
    for j in ("A","B","C","D"):   #A,B,C,D代表♥,♦,♠,♣
        poke.append(f"{j}{i}")
        print(f"{j}{i}",end=" ")  #1.先生成一付完整的扑克牌
print("\n发牌时间到") #2.给5个玩家随机发牌
for i in range(num_player):
    player_list = random.sample(poke,3)
    player.append(player_list)
print(player)
for x in range(5):
    print(player[x])