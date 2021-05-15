安装Sphinx
===============

1. Python及env安装
---------------------
.. tip::

 - python-3.6.8-amd64.exe
 - pip-19.3.1.tar
 - virtualenv-20.3.1.tar
 - virtualenvwrapper-win-1.2.6.tar

.. code-block:: bash
	
	C:\Users\Tim>pip install pip==19.3.1
	C:\Users\Tim>pip install virtualenv==20.3.1
	C:\Users\Tim>pip install virtualenvwrapper-win==1.2.6
	
	C:\Users\Tim>pip list
	    Package               Version
	    --------------------- -------
	    appdirs               1.4.4
	    distlib               0.3.1
	    filelock              3.0.12
	    importlib-metadata    4.0.1
	    importlib-resources   5.1.2
	    pip                   19.3.1
	    setuptools            40.6.2
	    six                   1.15.0
	    typing-extensions     3.7.4.3
	    virtualenv            20.3.1
	    virtualenvwrapper-win 1.2.6
	    zipp                  3.4.1
	
	#配置环境变量
	#修改workon的默认目录
	#系统环境变量，->新建系统变量 -> 变量名：WORKON_HOME ->指定路径：C:\Tim626\Python368\pyenvs

2. 创建虚拟环境
------------------
.. code-block:: bash

	C:\Users\Tim>workon
	
	    Pass a name to activate one of the following virtualenvs:
	    ==============================================================================
	    mozaiti

	C:\Users\Tim>workon env_name

	C:\Users\Tim>mkvirtualenv mozaiti
	
	(mozaiti) C:\Users\Tim>pip list
	    pip                           20.3.3
	    setuptools                    51.1.2
	    wheel                         0.36.2
	
	
	
3. 安装Sphinx及插件
----------------------
.. code-block:: bash

	(mozaiti) C:\Users\Tim>pip install sphinx sphinx-autobuild sphinx_rtd_theme sphinx-ansible-theme dask-sphinx-theme sphinx-togglebutton recommonmark sphinx-markdown-tables sphinxemoji
	
	(mozaiti) C:\Users\Tim>pip list
	    Package                       Version
	    ----------------------------- ---------
	    alabaster                     0.7.12
	    Babel                         2.9.1
	    certifi                       2020.12.5
	    chardet                       4.0.0
	    colorama                      0.4.4
	    commonmark                    0.9.1
	    dask-sphinx-theme             1.3.5
	    docutils                      0.16
	    idna                          2.10
	    imagesize                     1.2.0
	    importlib-metadata            4.0.1
	    Jinja2                        2.11.3
	    livereload                    2.6.3
	    Markdown                      3.3.4
	    MarkupSafe                    1.1.1
	    packaging                     20.9
	    pip                           20.3.3
	    Pygments                      2.8.1
	    pyparsing                     2.4.7
	    pytz                          2021.1
	    recommonmark                  0.7.1
	    requests                      2.25.1
	    setuptools                    51.1.2
	    six                           1.15.0
	    snowballstemmer               2.1.0
	    Sphinx                        3.5.4
	    sphinx-ansible-theme          0.4.1
	    sphinx-autobuild              2021.3.14
	    sphinx-markdown-tables        0.0.15
	    sphinx-notfound-page          0.6
	    sphinx-rtd-theme              0.5.2
	    sphinx-togglebutton           0.2.3
	    sphinxcontrib-applehelp       1.0.2
	    sphinxcontrib-devhelp         1.0.2
	    sphinxcontrib-htmlhelp        1.0.3
	    sphinxcontrib-jsmath          1.0.1
	    sphinxcontrib-qthelp          1.0.3
	    sphinxcontrib-serializinghtml 1.1.4
	    sphinxemoji                   0.1.8
	    tornado                       6.1
	    typing-extensions             3.7.4.3
	    urllib3                       1.26.4
	    wheel                         0.36.2
	    zipp                          3.4.1
	
	#创建存放项目的文件夹e:\timdevops\mozaiti
	
	(mozaiti) C:\Users\Tim>cd e:\Timdevops\mozaiti
	
	(mozaiti) C:\Users\Tim>>e:\
	
	#在此目录下生成文档
	(mozaiti) e:\timdevops\mozaiti>sphinx-quickstart
	    Welcome to the Sphinx 3.5.4 quickstart utility.
	    
	    Please enter values for the following settings (just press Enter to
	    accept a default value, if one is given in brackets).
	    
	    Selected root path: .
	    
	    You have two options for placing the build directory for Sphinx output.
	    Either, you use a directory "_build" within the root path, or you separate
	    "source" and "build" directories within the root path.
        > Separate source and build directories (y/n) [n]: y
        
        The project name will occur in several places in the built documentation.
        > Project name: Mozaiti    ------项目名称
        > Author name(s): mozaiti  ------作者
        > Project release []: v1   ------版本
        
        If the documents are to be written in a language other than English,
        you can select a language here by its language code. Sphinx will then
        translate text that it generates into that language.
        
        For a list of supported codes, see
        https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language.
        > Project language [en]:
        
        Creating file e:\timdevops\mozaiti\source\conf.py.
        Creating file e:\timdevops\mozaiti\source\index.rst.
        Creating file e:\timdevops\mozaiti\Makefile.
        Creating file e:\timdevops\mozaiti\make.bat.
        
        Finished: An initial directory structure has been created.
        
        You should now populate your master file e:\timdevops\mozaiti\source\index.rst a
        nd create other documentation
        source files. Use the Makefile to build the docs, like so:
           make builder
        where "builder" is one of the supported builders, e.g. html, latex or linkcheck.
	
	#编译前先删除
	(mozaiti) e:\timdevops\mozaiti>make clean
	    Removing everything under 'build'...
	    
	(mozaiti) e:\timdevops\mozaiti>make html
	    Running Sphinx v3.5.4
	    making output directory... done
	    building [mo]: targets for 0 po files that are out of date
	    building [html]: targets for 1 source files that are out of date
	    updating environment: [new config] 1 added, 0 changed, 0 removed
	    reading sources... [100%] index
	    looking for now-outdated files... none found
	    pickling environment... done
	    checking consistency... done
	    preparing documents... done
	    writing output... [100%] index
	    generating indices... genindex done
	    writing additional pages... search done
	    copying static files... done
	    copying extra files... done
	    dumping search index in English (code: en)... done
	    dumping object inventory... done
	    build succeeded.
	    
	    The HTML pages are in build\html.
	
	#直接打开在build\html里的index.html查看, 或通过web服务浏览#
	(mozaiti) e:\timdevops\mozaiti>C:\xxxxxx\Python36\Scripts\sphinx-autobuild.exe source build\html  #http://127.0.0.1:8000
	
	(mozaiti) e:\timdevops\mozaiti>C:\xxxxxx\Python36\Scripts\sphinx-autobuild.exe source build\html --host 192.168.1.100 --port 8888