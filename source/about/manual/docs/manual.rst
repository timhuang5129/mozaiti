参考
--------
::

  https://www.yuque.com/xunwukong/ktdky4/off3dd


分隔线
---------
.. raw:: html

  <hr width="700" size="20"/>


代码块4
--------
::

    for i in [1,2,3,4,5]:
        print i
    # 代码块测试

很简单的代码块测试。

安装
------------
.. code-block:: python

    pip install sandglass

代码块1
--------
.. code-block:: bash
   :linenos:

   Some more Ruby code.
   pip install sandglass
	
代码块2
--------
.. code-block:: ruby
   :lineno-start: 10

   Some more Ruby code, with line numbering starting at 10.
	
代码块3
--------
.. code-block:: python
   :emphasize-lines: 3,5

   def some_function():
       interesting = False
       print 'This line is highlighted.'
       print 'This one is not...'
       print '...but this one is.'

文字块
--------
 | 得得得得得得多
 | 得得得得得得多
   反反复复付付付付付付付付付付付付付付付付付付付付付付付付
 
概览
--------
 
**sandglass(沙漏)** 是一个增强的、友好的时间处理库，目的是为了解放程序员的生产力。
在python中有太多处理时间的库，datetime/date/time/calendar等等。需要记的细节太多，选择困难。
而sandglass就是解决这个的青霉素。从各种麻烦的转换中解脱出来。
只需记住 **Sandglass对象** 和 **ben()** 、 **tslice()** 、 **cronwalk()** 这几个主要的api即可。
 
特性
----------
 + api简洁，开箱即用
 + 增强接管datetime
 + (此次略去xx字)
 
快速上手
---------
在sandglass中，核心对象是 **Sandglass对象** 。通过这个对象，可以方便的获取各个时间属性和操作::
    
    #获取属性
    >>>sg = ben('2013,1,1 13:14:15')
    >>>sg.year,sg.month,sg.day,sg.hour,sg.minute,sg.second,sg.microsecond
    (2013, 1, 1, 13, 14, 15, 0)
    (此次略去xx字)
 
API文档
-----------------
 
.. toctree::
   :maxdepth: 2
 
   api
 
Todo
---------
* Add timezone support
 
Changelog
---------
**0.0.1**
 
* Initial release

链接1
------
这篇文章来自我的Github,请参考 reference_。

.. _reference: http://10.76.219.169:8899/myref/reStructuredText(rst)_manual.pdf

链接2
------
这篇文章来自我的Github,请参考 `SeayXu <https://www.wenjiangs.com/doc/rmqlwdf4>`_。

.. _struct_NiO:

	long long very long caption ...


数学公式
-----------
.. math::

  (a + b)^2 = a^2 + 2ab + b^2

  (a - b)^2 = a^2 - 2ab + b^2
   
字体控制
---------
.. Strong Emphasis

This is **Strong Text**. HTML tag is strong.粗体

.. Italic, Emphasis

This is *Emphasis* Text.这个HTML使用em， 斜体

.. Interpreted Text

This is `Interpreted Text`. 注意，这个HTML一般用<cite>表示

.. Inline Literals

This is ``Inline Literals``. HTML tag is <tt>. 等宽字体.

链接本地文件2
--------------
请把本地文件/图片/js等放在source/_static里

这篇文章来自我的Github,请参考 reference3_。

.. _reference3: ../../_static/myref/reStructuredText(rst)_manual.pdf

链接图片
-----------
.. image:: ../../_static/imgs/sphinxcontrib-osexample.png

链接图片2
------------
.. image:: ../../_static/imgs/1.png
   :width: 300
   :height: 300
   
格言
-----
    Practice is the first productive force




- 人类
- 男人

 + 有胡子
 
 - 短发
 
 * 短裤
 * 人字拖
 
- 女人

+ 小孩


ssddsd
-----------
	1. ddsdfsd
	#. dsfdsf
	
sssssss
-------------
.. confval:: sticky_navigation


代码主题颜色
-----------------
https://pygments.org/demo/#try



标题与章节
#################
Book Title
#################

*******************
Chapter 1
*******************

1.2 Section
=====================

1.2.3 Subsection
^^^^^^^^^^^^^^^^^^^^^^

1.2.3.4 Paragraph
""""""""""""""""""""""

粗体
**Bold**

斜体
*Italic*

内联代码
``inline code``


.. _Jinkan: https://jinkan.org/
 
脚注
 
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Pellentesque dignissim libero quis ipsum sagittis, vel dapibus justo dignissim [1]_.
Quisque scelerisque dictum sapien sit amet blandit.
Maecenas scelerisque feugiat urna in egestas. 
 
.. [1] this is a footnote
 
代码块
.. code-block:: python
 
    import antigravity
	

	
Grid table:
 
+------------+------------+-----------+
| Header 1   | Header 2   | Header 3  |
+============+============+===========+
| body row 1 | column 2   | column 3  |
+------------+------------+-----------+
| body row 2 | Cells may span columns.|
+------------+------------+-----------+
| body row 3 | Cells may  | - Cells   |
+------------+ span rows. | - contain |
| body row 4 |            | - blocks. |
+------------+------------+-----------+

	
	
	
Simple table:
 
=====  =====  ======
   Inputs     Output
------------  ------
  A      B    A or B
=====  =====  ======
False  False  False
True   False  True
False  True   True
True   True   True
=====  =====  ======



下面是引用的内容：
 
    “真的猛士，敢于直面惨淡的人生，敢于正视淋漓的鲜血。”
    --- 鲁迅

..

      “人生的意志和劳动将创造奇迹般的奇迹。”
      — 涅克拉索

用法介绍
----------------
https://blog.csdn.net/liuskyter/article/details/86570790


See figure :ref:`Link title <struct_NiO>`




.. code-block:: html
	:linenos:

	<h1>code block example</h1>

.. literalinclude:: ../../../_static/myref/fn.py
	:lines: 1,3,5-10,20-


六,引用和脚注
--------------------
::

	1, 在语句之中 使用 '[文字]_' 可以使用 '..[文字]' 为文字添加修饰 
	2, #f1 以 # 开头显示的是数字 数字实现自动增长

It is methioned by [Ref]_ that python is good.

.. [Ref] 《talk is good》

orem ipsum [#f1]_  dolor sit amet ... [#f2]_

Footnotes

.. [#f1] Text of the first footnote.
.. [#f2] Text of the second footnote.


七,替换
--------------
::

	1,在正文中使用'|文字|'这样标签，然后可以设定使用其他文本或者图片来代替'文字'这个占位符

I like eat |apple| very much.

.. |apple| replace:: orange


八, 生成类的文档:
-----------------------
    1, 可以按照以下格式定义 你可以紧挨着也可以 另起一行对齐
    2, ' py:decorator:: ' 指的是装饰器 另起一行 对一个类之中的装饰器进行说明

.. py:class:: Foo(object):
   .. py:method:: quux()
   .. py:attribute:: name
   .. py:staticmethod:: name(signature)
   .. py:classmethod:: name(signature)

.. py:decorator:: removename

   Remove name of the decorated function.

.. py:decorator:: setnewname(name)

   Set name of the decorated function to *name*.
 

九,通常将有用的命令或者代码 进行阴影化
-------------------------------------------

Code emphasis ::

   # ls -l
   # find . -perm -7 -print | xargs chmod o-w
   # ls -l
