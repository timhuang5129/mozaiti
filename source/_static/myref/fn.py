class Dogg(object):
    def __init__(self, name, age):
        self._name = name  #实例的私有属性
        self._age = age  #实例的私有属性
    
    @property
    def name(self):  #方法名必须与属性名一样
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
    @property
    def age(self):
        print('用户查询属性, 记录查询记录, 通知, 分析价格是否偏高, 查了100次, 只有1次购买')
        return self._name
    @age.setter
    def age(self, age):
        print('密码被修改, 确认是否为本人等通知')
        if age >0:
            self._age = age
        else:
            return 'age must be gt 0'
    @classmethod
    def test_ct(cls):
        print('这是一个类方法')
    
    def test_obj(self):
        print('这是一个实例方法')
    
    @staticmethod
    def test_sm():
        print('这是一个静态方法')
