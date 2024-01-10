import random
count = 1
staff = [] #员工列表
for i in range(1,30):
    staff.append(i)            # 不能用staff[i] = i  staff是一个空列表，进行staff[0]就会报错 只能用append装入列表
print(f"路飞科技员工名单{staff}\n")
squence = [10,3,1]
gift = ["苹果三斤!","安分守己!","泰国5日游+手术费报销!"]
for i in range(len(squence)): #循环此次保持在抽奖次数的数组长度上
    print(f"第{count}次抽奖中奖名单(第{4-count}名):")
    count += 1
    lottery = random.sample(staff,squence[i])  #random.randint()有可能重复
    print(f"{lottery}\n恭喜你们获得{gift[i]}")
    #删除抽到的
    # for lottery in staff: 此处如果使用这种写法导致lottery重新定义为员工列表的某个元素,导致结果出现问题
    #     staff.remove(lottery)
    for current_lottery in lottery:
        staff.remove(current_lottery)
    print(f"此次未中奖员工名单{staff}\n")
