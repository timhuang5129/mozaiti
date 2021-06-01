内联标记
=================
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
::

	定义格式为   :ref:`引用的标签的名称`
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
