搭建Gogs服务器
===============

1. 系统环境
----------------
.. hint:: 

 - CentOS 7.6
 - git-v2.24.1.tar.gz
 - `[基于docker搭建gogs] <https://www.cnblogs.com/yuexiaoyun/articles/11946103.html>`_
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



.. raw:: html

	<hr width="700" size="20"/>

.. hidden-code-block:: bash
        :starthidden: False
        :linenos:
        :label: + git clone test

	#Microsoft Windows 10 企业版 2016 LTS 10.0.14393
	#需要安装.net4.7.2或以上, 安装过程报错"1%不是Win32..."
	#未处理, 直接换高版本系统自带v4.7.2
	s2105282@client02 ~
	$ git --version
	git version 2.31.1.windows.1
	
	#gogs服务器docker部署
	#http://192.168.23.212:10086/gogs/gittest.git
	#ssh://git@192.168.23.212:22222/git/gittest2.git
	
	
	#使用git bash
	#Windows Server 2012 R2 Standard
	s2105281@client01 ~
	$ git --version
	git version 2.20.1.windows.1

	s2105281@client01 ~
	$ cd Desktop

	s2105281@client01 ~/Desktop
	$ mkdir mygit

	s2105281@client01 ~/Desktop
	$ cd mygit


	#使用HTTP方式克隆
	#gogs上有个名为gogs的用户, 创建了一个仓库gittest
	s2105281@client01 ~/Desktop/mygit
	$ git clone http://192.168.23.212:10086/gogs/gittest.git
	Cloning into 'gittest'...
	remote: Enumerating objects: 5, done.
	remote: Counting objects: 100% (5/5), done.
	remote: Compressing objects: 100% (4/4), done.
	remote: Total 5 (delta 0), reused 0 (delta 0)
	Unpacking objects: 100% (5/5), done.

	s2105281@client01 ~/Desktop/mygit
	$ cd gittest/

	s2105281@client01 ~/Desktop/mygit/gittest (master)
	$ ls
	LICENSE  README.md

	s2105281@client01 ~/Desktop/mygit/gittest (master)
	$ touch test.txt

	s2105281@client01 ~/Desktop/mygit/gittest (master)
	$ git add .

	s2105281@client01 ~/Desktop/mygit/gittest (master)
	$ git commit -m "test1111"
	[master c1382d8] test1111
	 1 file changed, 0 insertions(+), 0 deletions(-)
	 create mode 100644 test.txt

	#报错:原因是输入的用户不对
	s2105281@client01 ~/Desktop/mygit/gittest (master)
	$ git push origin  master
	Enumerating objects: 4, done.
	Counting objects: 100% (4/4), done.
	Delta compression using up to 8 threads
	Compressing objects: 100% (2/2), done.
	Writing objects: 100% (3/3), 251 bytes | 251.00 KiB/s, done.
	Total 3 (delta 1), reused 0 (delta 0)
	libpng warning: iCCP: cHRM chunk does not match sRGB
	error: RPC failed; HTTP 403 curl 22 The requested URL returned error: 403 Forbidden
	fatal: the remote end hung up unexpectedly
	fatal: the remote end hung up unexpectedly
	Everything up-to-date

	s2105281@client01 ~/Desktop/mygit/gittest (master)
	$ git push
	Enumerating objects: 4, done.
	Counting objects: 100% (4/4), done.
	Delta compression using up to 8 threads
	Compressing objects: 100% (2/2), done.
	Writing objects: 100% (3/3), 251 bytes | 251.00 KiB/s, done.
	Total 3 (delta 1), reused 0 (delta 0)
	Logon failed, use ctrl+c to cancel basic credential prompt.
	Username for 'http://192.168.23.212:10086': gogs   #gogs上有个名为gogs的用户, 创建了一个仓库gittest, 所以需要输入gogs的凭证
	error: unable to read askpass response from 'C:/Program Files/Git/mingw64/libexec/git-core/git-gui--askpass'
	Password for 'http://gogs@192.168.23.212:10086':
	To http://192.168.23.212:10086/gogs/gittest.git
	   56d23cd..c1382d8  master -> master

	s2105281@client01 ~/Desktop/mygit/gittest (master)
	$ cd ..

	#gogs上有个名为git的用户, 创建了一个仓库gittest2, 所以需要输入git的凭证
	s2105281@client01 ~/Desktop/mygit
	$ git clone http://192.168.23.212:10086/git/gittest2.git
	Cloning into 'gittest2'...
	Logon failed, use ctrl+c to cancel basic credential prompt.
	Username for 'http://192.168.23.212:10086': git 
	error: unable to read askpass response from 'C:/Program Files/Git/mingw64/libexec/git-core/git-gui--askpass'
	Password for 'http://git@192.168.23.212:10086':
	remote: Enumerating objects: 5, done.
	remote: Counting objects: 100% (5/5), done.
	remote: Compressing objects: 100% (4/4), done.
	remote: Total 5 (delta 0), reused 0 (delta 0)
	Unpacking objects: 100% (5/5), done.

	s2105281@client01 ~/Desktop/mygit
	$ ls
	gittest/  gittest2/

	s2105281@client01 ~/Desktop/mygit
	$ cd gittest2/

	s2105281@client01 ~/Desktop/mygit/gittest2 (master)
	$ ls
	LICENSE  README.md

	s2105281@client01 ~/Desktop/mygit/gittest2 (master)
	$ touch test2.txt

	s2105281@client01 ~/Desktop/mygit/gittest2 (master)
	$ git add .

	s2105281@client01 ~/Desktop/mygit/gittest2 (master)
	$ git commit -m "test2"
	[master 85dbe31] test2
	 1 file changed, 0 insertions(+), 0 deletions(-)
	 create mode 100644 test2.txt

	s2105281@client01 ~/Desktop/mygit/gittest2 (master)
	$ git push origin master
	Logon failed, use ctrl+c to cancel basic credential prompt.
	Username for 'http://192.168.23.212:10086': git
	error: unable to read askpass response from 'C:/Program Files/Git/mingw64/libexec/git-core/git-gui--askpass'
	Password for 'http://git@192.168.23.212:10086':
	Enumerating objects: 4, done.
	Counting objects: 100% (4/4), done.
	Delta compression using up to 8 threads
	Compressing objects: 100% (2/2), done.
	Writing objects: 100% (3/3), 250 bytes | 250.00 KiB/s, done.
	Total 3 (delta 1), reused 0 (delta 0)
	To http://192.168.23.212:10086/git/gittest2.git
	   b44b56c..85dbe31  master -> master



	#使用SSH方式克隆
	s2105281@client01 ~/Desktop/mygit/gittest2 (master)
	$ cd ..


	s2105281@client01 ~/Desktop/mygit
	$ ssh-keygen -t rsa -b 2048 -C "gogs@163.com"
	Generating public/private rsa key pair.
	Enter file in which to save the key (/c/Users/s2105281/.ssh/id_rsa):
	Enter passphrase (empty for no passphrase):
	Enter same passphrase again:
	Your identification has been saved in /c/Users/s2105281/.ssh/id_rsa.
	Your public key has been saved in /c/Users/s2105281/.ssh/id_rsa.pub.
	The key fingerprint is:
	SHA256:ZNR/vVNm6SBRSeSql/XXTcxte8cWzTN7EGkmaHdYgGA gogs@163.com
	The key's randomart image is:
	+---[RSA 2048]----+
	|        Eo .==o  |
	|       o  oo.+ . |
	|        o o.=.*..|
	|       o . oo*.*B|
	|        S  ..o+*@|
	|          . o .OO|
	|         . o   +@|
	|          .    .=|
	|                 |
	+----[SHA256]-----+


	#在/c/Users/s2105281/.ssh下新建conf文件
	#并且, 在gogs网站的git用户的用户设置添加ssh密钥id_rsa.pub
	s2105281@client01 ~
	$ cat .ssh/conf
	Host 192.168.23.212
		PreferredAuthentications publickey
		IdentityFile ~/.ssh/id_rsa.pub


	s2105281@client01 ~/Desktop/mygit
	$ ls
	gittest/  gittest2/

	s2105281@client01 ~/Desktop/mygit
	$ rm -rf gittest2/

	s2105281@client01 ~/Desktop/mygit
	$ git clone ssh://git@192.168.23.212:22222/git/gittest2.git
	Cloning into 'gittest2'...
	The authenticity of host '[192.168.23.212]:22222 ([192.168.23.212]:22222)' can't be established.
	ECDSA key fingerprint is SHA256:eiby+SnKeH3uexMZM1KVqonEpqwrOkjnuM6pg65VoCc.
	Are you sure you want to continue connecting (yes/no)? yes
	Warning: Permanently added '[192.168.23.212]:22222' (ECDSA) to the list of known hosts.
	remote: Enumerating objects: 8, done.
	remote: Counting objects: 100% (8/8), done.
	remote: Compressing objects: 100% (6/6), done.
	remote: Total 8 (delta 1), reused 0 (delta 0)
	Receiving objects: 100% (8/8), done.
	Resolving deltas: 100% (1/1), done.

	s2105281@client01 ~/Desktop/mygit
	$ ls
	gittest/  gittest2/

	s2105281@client01 ~/Desktop/mygit
	$ cd gittest2

	s2105281@client01 ~/Desktop/mygit/gittest2 (master)
	$ touch test22222.txt

	s2105281@client01 ~/Desktop/mygit/gittest2 (master)
	$ git add .

	s2105281@client01 ~/Desktop/mygit/gittest2 (master)
	$ git commit -m "test2222"
	[master 4238205] test2222
	 1 file changed, 0 insertions(+), 0 deletions(-)
	 create mode 100644 test22222.txt

	s2105281@client01 ~/Desktop/mygit/gittest2 (master)
	$ git push origin master
	Enumerating objects: 3, done.
	Counting objects: 100% (3/3), done.
	Delta compression using up to 8 threads
	Compressing objects: 100% (2/2), done.
	Writing objects: 100% (2/2), 246 bytes | 246.00 KiB/s, done.
	Total 2 (delta 1), reused 0 (delta 0)
	To ssh://192.168.23.212:22222/git/gittest2.git
	   85dbe31..4238205  master -> master

	s2105281@client01 ~/Desktop/mygit/gittest2 (master)
	$ ls
	LICENSE  README.md  test2.txt  test22222.txt

	s2105281@client01 ~/Desktop/mygit/gittest2 (master)
	$ cd ..

	s2105281@client01 ~/Desktop/mygit
	$ ls
	gittest/  gittest2/

	s2105281@client01 ~/Desktop/mygit
	$ rm -rf gittest

	s2105281@client01 ~/Desktop/mygit
	$ ls
	gittest2/

	#在同一台电脑下执行, 获取gogs用户的仓库, 可以clone执行成功, 不知为毛
	s2105281@client01 ~/Desktop/mygit
	$ git clone ssh://git@192.168.23.212:22222/gogs/gittest.git
	Cloning into 'gittest'...
	remote: Enumerating objects: 8, done.
	remote: Counting objects: 100% (8/8), done.
	remote: Compressing objects: 100% (6/6), done.
	remote: Total 8 (delta 1), reused 0 (delta 0)
	Receiving objects: 100% (8/8), done.
	Resolving deltas: 100% (1/1), done.

	s2105281@client01 MINGW64 ~/Desktop/mygit
	$ ls
	gittest/  gittest2/

	s2105281@client01 MINGW64 ~/Desktop/mygit
	$ cd gittest

	s2105281@client01 MINGW64 ~/Desktop/mygit/gittest (master)
	$ ls
	LICENSE  README.md  test.txt

	s2105281@client01 MINGW64 ~/Desktop/mygit/gittest (master)
	$ touch test111.txt

	s2105281@client01 MINGW64 ~/Desktop/mygit/gittest (master)
	$ git add .

	s2105281@client01 MINGW64 ~/Desktop/mygit/gittest (master)
	$ git commit -m "test1111"
	[master 0155bda] test1111
	 1 file changed, 0 insertions(+), 0 deletions(-)
	 create mode 100644 test111.txt

	#但是不能提交
	s2105281@client01 MINGW64 ~/Desktop/mygit/gittest (master)
	$ git push origin master
	Gogs: You do not have sufficient authorization for this action
	fatal: Could not read from remote repository.

	Please make sure you have the correct access rights
	and the repository exists.

	s2105281@client01 MINGW64 ~/Desktop/mygit/gittest (master)
	$
