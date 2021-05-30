基础知识
================

1. OOP三大特征
----------------
.. important::

 - 封装
    隐藏类的内部实现机制, 确保对象中数据的安全, 即隐藏对象中一些不希望被外部访问到的属性和方法, 或者就算可以访问也要可以对数据进行必要的检查或自定义
 - 继承
    确保对象的可扩展(OCP开闭原则: 对扩展开放, 对修改关闭)
 - 多态
    确保程序的灵活性

1. 类型判断
----------------
::

	可检查一个对象是否为一个类的实例
	isinstance(object, class-or-type-or-tuple)
	return True/False
	class,int,str,float,list,dict,bool,complex,...,(int,str)

2. 类与对象
----------------
.. confval:: 类的组成

  + 属 性: 对应类中的成员变量(描述事物的特征)
  + 行 为: 对应类中的成员方法(描述事物的行为)

.. confval:: 类的理解

  + 理解为: 类 = 汽车设计图；对象 = 实实在在的汽车
  + 面向对象程序设计的重点是类的设计
  + 定义类其实是定义类中的成员(成员变量和成员方法)
  + 所以类就是对现实世界事物的抽象定义, 这个抽象定义就可以基本把某事物描述清楚. 
  + 要想描述清楚事物, 必须要知道事物有哪些特征(数据, 用变量保存), 有哪些行为(用方法描述).
  + 当某事物的特征和行为都描述清楚后, 我们就认为对这个事物有一个大概的把握.

.. confval:: 对象的概念

  + 对象就是一个类的实实在在的实体, 也称为实例, 所以对象(object)也称为实例(instance), 实例就是对象, 对象就是实例.
  + 比如 “学生” 可以是一个类, 因为它描述了学生这一群体事物, 而具体的”3年级的小明” 就是一个对象, 相同的 “4年级的小花” 也是一个学生对象.

.. confval:: 类和对象的关系

  + 类是描述事物的, 一旦描述清楚, 就可以代表一类事物了.
  + 但是类只是概念, 要想使用实体, 必须要有对象, 但是从时间的先后顺序来讲, 是先有类, 才有的对象, 
  + 因为类就像是一个模板, 而对象就像是用这个模板制造出来的产品, 
  + 如前面图示所描述的, 汽车设计图是一个模板, 一旦有了这个模板, 就可以使用设计图, 无限制地制造汽车了.
  + 在这个过程中, 类的设计是更重要的, 就像现实中也是汽车设计师的工资通常比实施工人要高.

3. 属性和方法
---------------
.. confval:: 属性的概念

  + 通常是要隶属于某个对象来使用的, 也就是说要想使用属性, 必须要先创建对象

.. confval:: 方法的概念

  + 方法是类或对象行为特征的抽象，也称为函数。
  + 方法也可以描述为是某个功能的执行体, 一个方法通常对应一个功能.
  + 比如要想完成某种功能, 需要执行10行代码, 我们在程序中需要这个功能时,就把这10行代码写出来就可以了, 
  + 但是如果要多次使用这个功能, 虽然可以通过复制这10行代码的方式来完成功能, 但是效率低, 并且不利于维护. 
  + 所以我们通常把具有特定独立功能的一些代码封装到一个方法中, 这样, 只需在需要的地方简单地调用这个方法就可以自动完成功能了.

.. confval:: 方法和属性的关系

  + Java里的方法不能独立存在，所有的方法必须定义在类里, 而属性也是定义在类里的, 所以方法和属性都是隶属于类的, 方法和属性是平等的关系.
  + 属性用于描述事物的特征数据.
  + 方法用于描述事物的功能行为.

.. confval:: 属性和方法查找流程

  + 先在当前对象中查找, 有则返回, 无则去当前对象的类对象中查找, 有则返回, 无则报错
  

2. 类的5要素
--------------
.. confval:: 类中定义的属性和方法都是公共的, 任何该类的实例都可以访问

  + 如果这个属性(方法)是所有实例共享的, 则应该将其保存(写)到类对象中
  + 如果这个属性(方法)是某个实例独有的, 则应该将其保存(写)到实例对象中

.. confval:: 类属性

  + 直接在类中定义的属性为类属性
  + 可通过类或类的实例访问
  + 只能通过类对象来修改, 无法通过实例对象修改

.. confval:: 实例属性
 
  + 通过实例对象添加的属性为实例属性
  + 只能通过实例对象来访问和修改, 类对象无法访问和修改
  
.. confval:: 类方法

  + 在类内部使用@classmethod 来修饰的方法为类方法
  + 类方法的第一个参数必须为cls, 也会被自动传递, cls就是当前的类对象
  + 可通过实例和类去调用, 没有区别; 实例方法调用有区别

.. confval:: 实例方法

  + 在类中定义, 以self为第一个参数的方法都是实例方法
  + 实例方法在调用时, python会自动将调用对象作为self传入
  + 可通过实例和类去调用: 实例去调用不用传self; 类去调用必须传self

.. confval:: 静态方法

  + 在类内部使用@staticmethod 来修饰的方法为类方法
  + 静态方法的不需要指定默认参数, 可通过实例和类去调用, 没有区别
  + 一般都是一些工具类

2. 对象的3要素
----------------
::

	Id：唯一标识一个对象
	Type：标识对象的类型
	Value：对象的值
	
	

4. 类的定义
---------------
::

	类其实是type类型的对象, 定义类实际上是定义了一个type类型的对象
	
	两种风格的类: 一个是经典类, 另一个是新式类(把 object 作为基类). 

	#经典类
	>>> class ClassicSpam: # no base class
	
	... pass
	
	>>> ClassicSpam.__bases__
	
	()
	
	#新式类
	>>> class NewSpam(object): # directly inherit from object
	
	... pass
	
	>>> NewSpam.__bases__
	
	(,)

	#python2.x经典类
	>>> class A:
	
	... pass
	
	>>> dir(A)
	
	['__doc__', '__module__']
	
	#python2.x新式类
	>>> class B(object):
	
	... pass
	
	...
	
	>>> dir(B)
	
	['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
	
	如果我们继承了object, 会获得非常多的魔术方法, 这些方法包括诸如静态方法和类方法的构造, 类属性的快速访问, 定制类实例的实现方式等等

	显然, 大多数人会毫不犹豫的选择使用新式类, 毕竟功能强大.

	#python3.x经典类
	>>> class A:
	...     pass
	...
	>>> dir(A)
	['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
	>>> class B():
	...     pass
	...
	>>> dir(B)
	['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']

	#python3.x新式类
	>>> class C(object):
	...     pass
	...
	>>> dir(C)
	['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
	>>>

	#总结
	python2.x: 尽量继承object，这么好的东西不用白不用
	python3.x: 如果你的代码需要兼容python2, 那么就在代码里显示的继承object, 否则按照组内的编码规范或者个人习惯来就可以了
	
	在python3.x中只有新式类(哪种都一样), 在python2.x中还存在经典类;
	如果你的开发环境是2.x, 那就要注意继承object.
	如果你的开发环境是3.x, 可以不继承object, 但是如果你希望你的代码兼容性高一点,
	最好在3.x的环境下也显式继承object, 这样在2.x环境下跑也不会出问题.


See figure :ref:`Link title <struct_NiO>`

4. 封装_私有属性及方法
------------------------
.. hint::

 - 因为Python没有真正的私有属性(官方约定为: __双下划线开头), 所以在此可以以一个_开头表示, 
 - 虽然可以直接使用 "对象._属性名" 访问, 但请视为私有变量, 不要随意访问.
 - 这种方法不能有效的保护数据, 看人品, 以及不能对数据的操作进行验证或自定义

::

	class Person(object):
	    def __init__(self, name):
	        self.name = name  #实例的普通属性
	        self.__age = 21  #实例的私有属性, 改为外部不知道的名字
	
	p_obj = Person("laowang")
	print(p_obj.name)
	
	Python中没有真正的私有属性, 官方约定为: __双下划线开头的属性为私有属性, 实质上是系统自动给它起了一个别名:_类名__私有属性, 即_Person__age
	使用P_obj._Person__age访问
	使用dir(p_obj)可查看实例的所有属性, 所以没有秘密, 所以只要遵循团队风格即可
	
4. 封装_getter及setter
------------------------
.. hint::

 - 通过提供的公有方法(getter及setter)访问或修改私有属性
 - getter 获取对象中的指定属性(get_属性名())
 - setter 用来设置对象的私有属性(set_属性名(需要设置的属性))
 - 可以只写getter方法(只读属性); 但不能只写setter, 必须有getter. 
 - 这种方法可有效的保护数据(隐藏属性名), 以及可对数据的操作进行验证或自定义(防止随意修改, 确保数据正确), 虽然增加了复杂性

::

	class Dog(object):
	    def __init__(self, name, age):
	        self._name = name  #实例的私有属性
	        self._age = age  #实例的私有属性
	    def get_name(self):
	        return self._name
	    def set_name(self, name):
	        self._name = name
	    def get_age(self):
	        print('用户查询属性, 记录查询记录, 通知, 分析价格是否偏高, 查了100次, 只有1次购买')
	        print('比如计算矩形的面积, 只需提高长和宽, 如求面积可以通过计算得到')
	        return self._name
	    def set_age(self, age):
	        print('密码被修改, 确认是否为本人等通知')
	        if age >0:
	            self._age = age
	        else:
	            return 'age must be gt 0'
	
	d = Dog('A', 2)
	d.get_name()
	d.set_name('B')
	
5. 封装_getter及setter的装饰器@property
-----------------------------------------
.. hint::

 - @property 用来将一个get方法, 转换为对象的属性, 此时定义get方法的方法名必须与属性名一样
 - 在调用时, 把方法当属性一样操作, 省了写括号的麻烦, 还可错误提示
 - 即dog.get_age() ---> dog.age
 - setter方法的装饰器: @属性名.setter

::

	class Dog():
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
	d = Dog('A', 2)
	d.name
	d.name = 'B'

5. super()
----------
::

	super()可动态获取当前类的父类, 降低耦合, 且不需要提供self
	super().__init__(name)等价于父类.__init__(self, name)
	实例调用类方法, 不需要传self
	类直接调用类方法, 需要传self

6. 多重继承及查找顺序(不同父类, 存在相同方法时, 子类该执行哪个)
-----------------------------------------------------------------
::

	返回当前类的所有父类, A类.__bases__
	
	class D(C,B,A):
		pass
	
	查找顺序: 从左往右, 就近原则. 
		先从自己D找, 没有就从其父类找, 先从C找
		C没有, 从C的父类里找, ... ,直到object
		还是没有, 则从B找, 若B没有, 从B的父类里找, ... ,直到object. 但是为了提高性能, 如果前面C找过的相同父类里没有的, B就不会再找, 比如object
		......直到找到为止
		因此, 如果D,C,B,A中存在一个相同的方法, 只会调用D的方法, 实际上后面的被D覆盖了(重写), 后面相同的方法根本不会执行。
		尽量避免使用多重继承, 虽然子类功能强大, 但大大增加复杂性。

6. 继承
---------
	在继承中我们知道子类是父类的扩展，它可以提供比父类更加强大的功能.
		
7. 枚举类
-----------
	dssscdsd

9. 迭代器
----------
    xcascasc

9. 生成器
----------
    xcascasc
	
8. 装饰器
-----------
    csdsds
	
9. mixin
----------
    xcascasc

10. 浅拷贝
------------

	可变对象如list
	lst = [1,2,3]
	lst.copy()
	lst[:]
	
	def test(a):
	    a[0]=30
		
	test(lst)
