代码块折叠效果
===================

容器
---------------
.. container:: toggle, toggle-hidden

	.. admonition:: Look at that, an image!

		.. image:: ../../_static/imgs/1.png

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

   </details>

.. raw:: html

	<hr width="700" size="20"/>
