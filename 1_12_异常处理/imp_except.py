
class MyException(Exception):
    '''这是我是某某异常'''
    def __init__(self,num,atleast):
        super().__init__()
        self.num = num
        self.atleast = atleast