搭建Git服务器
===============

1. 系统环境
----------------
.. hint:: 

 - CentOS 7.6
 - git-v2.24.1.tar.gz
 - `[申请Let's Encrypt永久免费SSL证书] <https://www.cnblogs.com/sage-blog/p/10302934.html>`_
 - `[一步搞定私有Git服务器部署(Gogs)] <https://www.jianshu.com/p/424627516ef6>`_
 - `[从0开始学习GitHub系列] <https://www.jianshu.com/p/424627516ef6>`_
 - `[Gogs搭建自己的代码服务器] <https://zhuanlan.zhihu.com/p/142802571>`_
 - `[Docker+Mysql5.7+gogs搭建私服] <https://www.cnblogs.com/fuzongle/p/12781828.html>`_

2. 管理大量用户使用git权限: gitosis
-------------------------------------
 - 开发者较少

  * 在/home/git/.ssh文件中有authorized_keys文件, 这个文件里边存放了需要使用git项目的用户的公钥, 也就是允许谁可以git你的项目.
  * 不安全, 用户对所有在/home/git下的git项目都拥有读写权限.
  * 每次增加或删除用户时都必须登录到服务器上去操作.

 - 开发者上百

  * 使用gitosis, 它是用来管理authorized_keys文件和简单连接限制的脚本.
  * 添加、删除用户或设定权限这些工作是通过管理一个特殊的git仓库来实现的;
  * 你只需要在这个仓库做好相应的设置, 然后推送到服务器上, gitosis就会随之改变策略.

3. ssh PK安全
------------
::

	对于用户较少的团队大家可以直接用git账户来拖代码或者推代码，但是这样的做法是不安全的，同时也很难区分作者。
	最好的办法可以是让大家都上传自己的公钥，由管理员添加进允许列表，具体是这样做的。
	首先需要修改ssh配置，在/etc/ssh/目录下有一个sshd_config的文件。
	找到里面有关AuthorizedKeysFile的一行，取消注释，并将后面的路径修改为/home/git/.ssh/authorized_keys
	保存后重启ssh服务。

4. Docker安装gogs
--------------------
.. code-block:: bash

	[root@BJ-JUMPSER-T01 ~]# mkdir -v /mydev/gogsworkspace
	
	[root@BJ-JUMPSER-T01 ~]# docker load -i /mydev/docker_images/gogs-docker-git.tar 
	
	[root@BJ-JUMPSER-T01 ~]# docker run -d --name=gogs -p 10022:22 -p 10080:3000 -e TZ=Asia/Shanghai -v /mydev/gogsworkspace:/data gogs/gogs
	
	[root@BJ-JUMPSER-T01 ~]# docker ps
	
	[root@BJ-JUMPSER-T01 ~]# docker ps -a
	    CONTAINER ID        IMAGE                       COMMAND                  CREATED             STATUS                      PORTS                                        NAMES
	    deb3d105adcd        gogs/gogs                   "/app/gogs/docker/stxx"   4 minutes ago       Exited (0) 19 seconds ago                                                gogs
	
	[root@BJ-JUMPSER-T01 ~]# docker start deb3d105adcd
	    deb3d105adcd
	
	[root@BJ-JUMPSER-T01 ~]# chown -R git:git /mydev/gogsworkspace/
	
	[root@BJ-JUMPSER-T01 ~]# docker ps
	    CONTAINER ID        IMAGE                       COMMAND                  CREATED             STATUS              PORTS                                            NAMES
	    deb3d105adcd        gogs/gogs                   "/app/gogs/docker/stxx"   23 minutes ago      Up 18 minutes       0.0.0.0:10022->22/tcp, 0.0.0.0:10080->3000/tcp   gogs
	
	[root@BJ-JUMPSER-T01 ~]# docker exec -it gogs /bin/bash
	    bash-5.0# ls
	    data    docker  gogs    log
	    
	    bash-5.0# cat  /etc/passwd|grep git                                                                                                                                                           
	    git:x:1000:1000:Gogs Git User:/data/git:/bin/bash
	  	 																																				 
	    bash-5.0# chown -R git:git /data/
	    
	[root@BJ-JUMPSER-T02 ~]# mysql -uroot -p
	    mysql> mysql> use mysql;
	    mysql> select host,user from user;
	    +--------------+-----------+
	    | host         | user      |
	    +--------------+-----------+
	    | %            | root      |
	    | localhost    | mysql.sys |
	    | localhost    | root      |
	    +--------------+-----------+
	    3 rows in set (0.02 sec)
	    
	    mysql> CREATE DATABASE gogs CHARACTER SET 'utf8' COLLATE 'utf8_general_ci';
	    Query OK, 1 row affected (0.01 sec)
	    
	    mysql> GRANT ALL PRIVILEGES ON gogs.* TO 'gogs'@'192.168.1.10' IDENTIFIED BY 'Gogs.xxxxxxxxxx';
	    Query OK, 0 rows affected, 1 warning (0.04 sec)
	    
	    mysql> select host,user from user;
	    +--------------+-----------+
	    | host         | user      |
	    +--------------+-----------+
	    | %            | root      |
	    | 192.168.1.10 | gogs      |
	    | localhost    | mysql.sys |
	    | localhost    | root      |
	    +--------------+-----------+
	    4 rows in set (0.02 sec)
