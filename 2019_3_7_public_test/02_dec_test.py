

def outer(func):# func == func1
    def inner(name):
        func(name)
        print('inner 中的 %s'%name)
    return inner
@outer  # 等同于func1 = outer(func1)
#todo : func1 = outer(func1)  func1 == inner
def func1(name):
    print('this is xuegod1')
    print('I am %s'%name)
    # print('I come from china')
if __name__ == '__main__':
    func1('for')# inner()#todo :func1() == inner()
    print(func1)