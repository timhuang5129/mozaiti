代码块折叠效果
===================

.. admonition:: mount_details
	:class: dropdown, toggle-shown

	* mount -o remount,rw /sysroot
	* 重新以可读可写的方式挂载为已经挂载 /sysroot
	* -o <选项> 指定挂载文件系统时的选项，有些也可写到在 /etc/fstab 中。常用的有：
	* defaults 使用所有选项的默认值（auto、nouser、rw、suid）
	* auto/noauto 允许/不允许以 –a选项进行安装
	* dev/nodev 对/不对文件系统上的特殊设备进行解释
	* exec/noexec 允许/不允许执行二进制代码
	* suid/nosuid 确认/不确认suid和sgid位
	* user/nouser 允许/不允许一般用户挂载
	* codepage=XXX 代码页
	* iocharset=XXX 字符集
	* ro 以只读方式挂载
	* rw 以读写方式挂载
	* remount 重新安装已经安装了的文件系统
	* loop 挂载“回旋设备”以及“ISO镜像文件”
	* 原来要 /etc/fstab 中的挂载生效并不用重启。 sudo mount -a
	* 示例::

		mount -o remount,rw /sysroot

		findmnt /sysroot/

	.. seealso::
		:class: dropdown, toggle-shown

		* `[Linux开机自动挂载NFS配置的一个误区] <https://www.cnblogs.com/qjfoidnh/p/13639585.html>`_
		* `[mount -a，mount挂载 ,/etc/fstab配置文件] <https://blog.csdn.net/lynnlycs/article/details/89136520>`_
		* `[/etc/fstab 参数详解及如何设置开机自动挂载] <http://blog.itpub.net/31397003/viewspace-2141695/>`_
		* `[修改完/etc/fstab后重新挂载方法] <https://blog.csdn.net/weixin_33937499/article/details/89772336>`_
		* `[Linux /etc/fstab中的_netdev挂载选项如何工作？] <http://www.szliwen.com/806.html>`_




.. hint::
	:class: dropdown, toggle-shown

	dfsdfsdfs::
	    ssssss

	.. hint::
		:class: dropdown, toggle-shown
		
		ssasdsadsadasdsa







容器
---------------
.. container:: toggle, toggle-hidden

	.. admonition:: Look at that, an image!

		.. image:: ../../../_static/imgs/logo.gif

.. raw:: html

	<hr width="700" size="20"/>

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

.. raw:: html

	<hr width="700" size="20"/>

.. hidden-code-block:: python
    :starthidden: False

    a = 10
    b = a + 5

	#放于conf.py相同位置
	D:\xxxxxx\Sphinx\source\hidden_code_block.py
	
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

	<hr width="700" size="20"/>

.. raw:: html

   <details>
   <summary><a>big code</a></summary>

.. code-block:: python

   lots_of_code = "this text block"

.. raw:: html

   </details>

.. raw:: html

	<hr width="700" size="20"/>
