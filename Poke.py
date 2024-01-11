# 一付扑克牌，去掉大小王，每个玩家发3张牌，最后比大小，看谁赢，
# 有以下几种牌
# 豹子: 三张一样的牌，如3张6.如红桃5、6、7同花顺: 即3张同样花色的顺子
# 顺子:又称拖拉机，花色不同，但是顺子，如红桃5、方片6、黑桃7，组成的顺子对子:2张牌一样单张: 单张最大的是A这几种牌的大小顺序为，豹子>同花顺>同花>顺子>对子>单张
# 需程序实现的点:
# 1.先生成一付完整的扑克牌
# 2.给5个玩家随机发牌
# 3.统一开牌，比大小，输出赢家是谁
import random
import re
num_player = 5 #玩家人数
signal = [0,0,0,0,0]
poke = []
player = []
new_split = []
new_split2 = []
max_num = []
winner_max = []
winner = 0
for i in range(1,14):
    for j in ("A","B","C","D"):   #A,B,C,D代表♥,♦,♠,♣
        poke.append(f"{j}{i}")
        print(f"{j}{i}",end=" ")  #1.先生成一付完整的扑克牌
print("\n发牌时间到")
for i in range(num_player):  #2.给5个玩家随机发牌
    player_list = random.sample(poke,3)
    player.append(player_list)
print(player)
for x in range(5):
    for y in range(0,3):

        new_split.append(int(re.split("[A-D]",player[x][y])[1]))#分割出玩家抽出牌的数字位置,并且转化为整型便于下列排序

        new_split2.append(re.split("[0-9]", player[x][y])[0])  # 分割出玩家抽出牌的字母位置
        #print(new_split2)
    new_split.sort()#排序，以便于计算是否是顺子
    #print(new_split)
    if new_split[0] == new_split[1] == new_split[2]:#对子：两张一样的牌
        signal[x] = 5
    elif (new_split2[0] == new_split2[1] == new_split2[2]) and (new_split[0] == new_split[2] -2):
        signal[x] = 4
    elif new_split[0] == new_split[2] -2:
        signal[x] = 3
    elif new_split[0] == new_split[1] or new_split[0] == new_split[2] or new_split[1] == new_split[2]:#豹子: 三张一样的牌
        signal[x] = 2
    else:
        signal[x] = 1
    # elif new_split.sort():
    # print(new_split)
    max_num.append(max(new_split))
    print(max_num[x])
    print(new_split)
    print(new_split2)
    new_split = [] #清空字母和数字列表
    new_split2 = []
#print(max_num[x])
#查看五位玩家的记录数
print(signal)
if(len(list(set(signal))) == 1):
    print(f"获胜者是{max_num}")
else:
    for i in range(5):
        if (signal[i] == max(signal)):
            winner_max.append(i)




