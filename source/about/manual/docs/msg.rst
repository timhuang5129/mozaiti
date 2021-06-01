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
