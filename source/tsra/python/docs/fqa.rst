测试
================

1. is和==的区别
------------------
::

	==判断值是否相等, is判断地址是否一致
	
	Python中所有类型都通过引用存取, 即便是"基本类型"也不例外。
	Python中的对象包含三要素：id、type、value。
	其中: id用来唯一标识一个对象, type标识对象的类型, value是对象的值
	
	is判断的是a对象是否就是b对象（两个引用是否指向同一个对象）, 是通过id来判断的

	== 判断的是a对象的值是否和b对象的值相等, 是通过value来判断的
	
	#示例
	>>> a = ''
	>>> b = ''
	>>> if a==b:
	...
	KeyboardInterrupt
	>>> a==b
	True
	>>> a is b
	True
	>>> id(a)
	2400764590768
	>>> id(b)
	2400764590768
	因为str是不可变类型, 所以a和b指向了同一个对象, 所以a和b无论值还是引用都是相等的。而可变类型, 则不同, 虽然值是相同的, 但是两个引用指向的对象是不同的。
	>>> lst1 = []
	>>> lst2 = []
	>>> lst1==lst2
	True
	>>> lst1 is lst2
	False
	>>> id(lst1)
	2400799194824
	>>> id(lst2)
	2400799466568
	“is"的作用是判断是否是同一实例, ”==" 的作用是取值。 也能从另一角度看出来, 操作符"=="能通过方法__eq__()重载, 也就是允许去比较对象中我们感兴趣的东西。
