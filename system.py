from system_people import zfzr
class manage_system(object):
    __type='管理系统界面'
    def __init__(self):
        self.zfzr=zfzr()

    def tkinter(self):
        while True:
            print(manage_system.__type)
            print("-----------------------------")
            print('0.总管')
            print('1.管理员')
            print('2.普通成员')
            print('-----------------------------')


    def function(self):
        pass

    def boot_main(self):
        pass


if __name__ == '__main__':
    system=manage_system()
    system.tkinter()

