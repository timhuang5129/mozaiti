Sphinx手册
===============

1. 标签
---------------------
.. tip::

 - tip

.. attention::

 - attention

.. caution::

 - caution

.. danger::

 - danger

.. error::

 - error

.. hint::

 - hint

.. important::

 - important

.. note::

 - note

.. seealso::

 - seealso

.. tip::

 - tip

.. warning::

 - warning

 
 
2. 代码块折叠效果
---------------------
.. container:: toggle, toggle-hidden

	.. admonition:: Look at that, an image!

		.. image:: ../../_static/imgs/1.png
	
.. hint::
	:class: dropdown, toggle-shown

	This is my note.

.. admonition:: code
	:class: dropdown

		def some_function():
			interesting = False
			print 'This line is highlighted.'
			print 'This one is not...'
			print '...but this one is.'

请参考 `sphinx-togglebutton <https://pypi.org/project/sphinx-togglebutton/>`_。			

.. hidden-code-block:: python
	:starthidden: False

	a = 10
	b = a + 5

	#放于conf.py相同位置
	D:\PM21\Sphinx\source\hidden_code_block.py
	
	import os
	import sys
	sys.path.insert(0, os.path.abspath('.'))

	extensions = [
		'hidden_code_block'
	]

.. hidden-code-block:: python
	:linenos:
	:label: --- SHOW/HIDE ---

	x = 10
	y = x + 5

请参考 `hiddencode <https://github.com/scopatz/hiddencode/blob/master/index.rst>`_。


.. raw:: html

   <details>
   <summary><a>big code</a></summary>

.. code-block:: python

   lots_of_code = "this text block"

.. raw:: html

   </details>


3. 标题H1-H6
--------------
::

    H1
    =================
    	我的
    	
    H2
    --------------
    	你的
    	
    H3
    >>>>>>>>>>>>>
    	他的
    	
    H4
    ::::::::::::
    	第三方水电费
    
    H5
    .............
    	发光时代个梵蒂冈
    
    H6
    """"""""""""""
    	法规的身份固定固定


4. 内联标记
--------------
::

	Sphinx 使用文本解释角色在文档中插入语义标签. 这样写 :rolename:`content`.
	
	Note
	
	默认角色 (`content`) 并不特别. 可使用任何其他有效的名字来代替; 使用 :confval:`default_role` 设置.
	
	由主域添加的角色请参考 Sphinx Domains .
	
	交叉索引的语法
	多数文本解释角色都会产生交叉索引. 需要写一个 :role:`target`, 创建名为 target 的链接，类型由 role 指定. 链接文本与 target 一样.
	
	还有其他的功能，这使得交叉索引更通用:
	
	需要明确的标题及索引标签, 像reST 超链接: :role:`title <target>` ，会链接 target 标签, 但链接文本为 title.
	
	加前缀 !, 交叉索引/超链接不会被创建.
	
	前缀 ~, 链接文本仅是标签的最后成分. 例如, :py:meth:`~Queue.Queue.get` 会建立到 Queue.Queue.get 的链接，但是链接文本仅显示 get .
	
	HTML 文档, 链接的 title 属性 (显示为鼠标的tool-tip) 一直是完整的标签名.
	
	交叉索引的对象
	这些角色在不同主域里:
	
	Python
	C
	C++
	JavaScript
	ReST
	
	1.交叉索引的位置
	------------------
	:ref:
	
	在文档的任意位置都可以使用交叉索引, 像标准reST 标签一样使用. 对于文档条目这些标签名必须是唯一的.
	
	有两种方式可以链接到这些标签:
	
	#111111111
	标签直接放在章节标题前面, 可以通过 :ref:`my-ref-label` 引用.例如:
	需引用自身, 查看 :ref:`my-ref-label`.
	角色 :ref: 会产生这个章节的链接, 链接标题是 “Section to cross-reference”. 章节与索引可在不同的源文件.
	
	自动标签也可以使用 figures: given
	参考 :ref:`my-figure` 将在图例里插入引用索引，链接文本是 “Figure caption”.
	
	表格也可以使用，在表格标题上使用指令 :dudir:`table` .
	
	#222222222222
	标签不放在章节开头，需要给出明确的Link title，使用语法: :ref:`Link title <my-ref-label2>`.
	
	推荐使用角色 ref 而不是标准的reStructuredText 章节链接 (比如 `Section title`_) ，因为它可以在不同文件间使用，并且即使章节标题变化，所有的生成器仍支持这些索引.


.. _my-ref-label:
	
Section to cross-reference
----------------------------
	这里是我的章节内容.


.. _my-figure:
	
.. figure:: whatever.png
	
	Figure caption
	
.. _my-ref-label2:

	dsfsdgsdgsdgsdgddddddddddd

.. note::

	https://zh-sphinx-doc.readthedocs.io/en/latest/markup/inline.html#ref-role


信息框_按照严重程度排列
-------------------------
.. note::

	需要引起读者注意的文字，可使用信息框。本信息框为“注解 (note 标记)”。

.. hint::

	“提示 (hint 标记)”可以用来在正文之外补充少量信息。例如，提示：这些软件包在 OpenSUSE 和 Debian 中使用不同的名字。

.. tip::

	“小技巧 (tip 标记)”可以用来介绍一些额外的使用技巧，例如：“你可以为你习惯的文档设定制作一个模板”，或者“按下 M 可以水平翻转画布视图以便发现画面的问题”。

.. important::

	“重要 (important 标记)”可以用来强调一些需要留意的信息，但并不一定是负面的信息。

.. warning::

	“警告 (warning 标记)”一般在描述负面信息时使用。

.. attention::

	“注意 (attention 标记)”可以用来标注那些比“警告”更严重，但又不至于造成数据损失的事项时使用。

.. caution::

	“小心 (caution 标记，Sphinx 的中文翻译误作‘警告’)”信息用于标注可能会造成数据损失的情况，例如提示读者不要忘记保存文件，或者让读者当心 Python 插件进行的操作目前无法撤销等事项。

.. danger::

	“危险 (danger 标记)”信息用于标注那些危及计算机整体运行的情况，包括那些导致内存不足死机的操作等。

.. error::

	“错误 (error 标记)”信息与手册本身内容无关，Sphinx 在某些情况下会生成这种信息，但我们的配置文件默认没有开启这一功能。


自定义信息框
---------------
.. admonition:: 我的最爱

	这是我的自定义信息框

参见
--------
.. seealso::

	方便用于集中列出外部链接和参考资料。
	
.. todo::

	Use this directive like, for example, note.
	
	It will only show up in the output if todo_include_todos is True.

	New in version 1.3.2: This directive supports an class option that determines the class attribute for HTML output. If not given, the class defaults to admonition-todo.

.. todolist::

	This directive is replaced by a list of all todo directives in the whole documentation, if todo_include_todos is True. 



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
.. code-block:: ruby
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

.. _reference: http://192.168.1.100:8899/myref/reStructuredText(rst)_manual.pdf

链接2
------
这篇文章来自我的Github,请参考 `SeayXu <https://www.wenjiangs.com/doc/rmqlwdf4>`_。

.. _struct_NiO:

	long long very long caption ...


公式
-----------------
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