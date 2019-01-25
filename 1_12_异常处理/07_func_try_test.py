

def test01():
    print('----test01---')
    print(num)
def test02():
    print('----test02---')
def test03():

    try:
        print('----test03---')
        test01()
    except Exception as e:
        print('捕获异常:%s'%e)
test03()