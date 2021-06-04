安装方式
----------
 - 在线安装Docker
 - 利用yum缓存离线部署Docker

1. 硬/软链接
--------------
.. code-block:: bash

	ln -s 是创建软链接, 不会占用磁盘空间
	ln 是创建硬链接
	相当于windows下创建的快捷方式
	ln -s /usr/lib/pf(真实文件路径) /data/vf(需要快捷方式的路径)
	vf就是快捷方式, 点击它就能执行pf
	
	比如/var/lib/docker会占用很多空间, 我们可以把它移到/data/docker, 但是Docker程序默认需要/var/lib/docker, 因此可创建快捷方式, 把数据真正存到/data/docker中
	ln -s /data/docker /var/lib/docker

2. 修改用户shell
------------------
.. code-block:: bash

	查看/etc/passwd 发现用户的shell 为false! 所以需要修改用户shell, 命令如下：

	usermod -s /bin/bash username
