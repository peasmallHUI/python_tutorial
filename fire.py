class Person(object):
    def __init__(self,person_name):
        self.name = person_name
        self.gun_flag = None
        self.hp = 100
    
    def __str__(self):
        if self.hp >0:
            return "人物名称：%s 血量：%d\n枪支信息：%s"%(self.name, self.hp, self.gun_flag)
        else:
            return "人物名称：%s 已死亡。。。"%self.name
    
    def fill(self,clip_temp,amo_temp):
        clip_temp.contain(amo_temp)
    
    def reload(self,gun_temp,clip_temp):
        gun_temp.pack(clip_temp)
    
    def hold_gun(self,gun_temp):
        self.gun_flag = gun_temp
    
    def fire(self,enemy_temp):
        self.gun_flag.shot(enemy_temp)
    
    def blood(self,damage):
        # if (self.hp-damage):
        self.hp -= damage
        # else :
        #     self.hp = 0
        #     print("人物已死亡")

class Gun(object):
    def __init__(self,gun_name):
        self.name = gun_name
        self.clip_flag = None
    
    def __str__(self):
        if self.clip_flag:
            return "枪支为%s\n%s"%(self.name,self.clip_flag)
        else:
            return "枪支为%s,无弹夹"%self.name
    
    def pack(self,clip_temp):
        if self.clip_flag:
            print ("已有弹夹，请勿重复装填")
        else:
            self.clip_flag = clip_temp
    
    def shot(self,enemy_temp):
        self.clip_flag.bpop(enemy_temp)

class Clip(object):

    def __init__(self,cap_num):
        self.cap_num = cap_num
        self.blist = []
    
    def contain(self, amo_temp):
        if len(self.blist) < self.cap_num:
            self.blist.append(amo_temp)
        else:
            #print("子弹已装满")
            pass

    def __str__(self):
        return "弹夹容量：%d/%d"%(len(self.blist),self.cap_num)

    def bpop(self,enemy_temp):
        amo_temp = self.blist.pop()
        if amo_temp:
            amo_temp.injure(enemy_temp)
        else:
            print("无子弹，不能射击")

class Amo(object):
    def __init__(self,damage):
        self.damage = damage
    
    def injure(self,enemy_temp):
        enemy_temp.blood(self.damage)

def main():
    #0.输入数据
    person_name = input("请输入人物名称：")
    gun_name = input("请输入枪支名称：")
    clip_cap = eval(input("请输入弹夹容量："))
    amo_damage = eval(input("请输入子弹伤害：")) 
    amo_num = eval(input("请输入子弹数目："))
    enemy_name = input("请输入敌人名称：")
    fire_num = eval(input("请输入开火次数："))

    #1.创建人物
    someone = Person(person_name)
    #test
    # print(someone)

    #2.创建枪支
    gun1 = Gun(gun_name)
    #test
    # print(gun1)

    #3.创建弹夹
    clip1 = Clip(clip_cap)

    #4.创建子弹
    amo1 = Amo(amo_damage)

    #5.安装子弹
    for i in range(amo_num):
        someone.fill(clip1,amo1)
    #print(clip1)

    #6.安装弹夹
    someone.reload(gun1,clip1)
    #print(gun1)

    #7.创建敌人
    enemy = Person(enemy_name)
    #print(enemy)

    #8.拿取枪支
    someone.hold_gun(gun1)
    #print(someone)

    #9.开火
    for i in range(fire_num):
        someone.fire(enemy)
    print("="*20)
    print(enemy)
    print("="*20)
    print(someone)

if __name__ == '__main__':
    main()