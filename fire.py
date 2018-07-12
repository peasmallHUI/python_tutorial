class Person(object):
    def __init__(self,person_name):
        self.name = person_name
    
    def __str__(self):
        return self.name

class Gun(object):
    def __init__(self,gun_name):
        self.name = gun_name

class Clip(object):
    def __init__(self,cap_num):
        self.cap_num = cap_num

class Amo(object):
    def __init__(self,damage):
        self.damage = damage

def main():
    #1.创建人物
    someone = Person("无敌的你")

    #test
    # print(someone)

    #2.创建枪支
    

    #3.创建弹夹

    #4.创建子弹

    #5.安装子弹

    #6.安装弹夹

    #7.创建敌人

    #8.拿取枪支

    #9.开火

if __name__ == '__main__':
    main()