搭建Git服务器
================

1. 系统环境
----------------
.. hint:: 

 - CentOS 7.6
 - git-v2.24.1.tar.gz
 - `[在Linux下搭建Git服务器步骤] <https://www.jb51.net/article/104155.htm>`_
 - `[从0开始学习GitHub系列] <https://www.pianshen.com/article/3055468005/>`_
 - `[GitHub与GitLab的区别以及GitLab的搭建与使用] <https://www.jianshu.com/p/947eaa90d6cf>`_
 - `[Linux下Git Server搭建] <https://zhuanlan.zhihu.com/p/22346531>`_
 - `[Linux实验 ssh配置详解] <https://www.cnblogs.com/dumpling-z/p/11434105.html>`_
 - `[在ssh-copy-id之后仍需输入密码的问题] <https://www.cnblogs.com/xzysaber/p/6589182.html>`_
 - `[Linux 下搭建Git 服务器详细步骤] <https://blog.csdn.net/a77687789/article/details/101331411>`_


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

3. 关闭防火墙
--------------------
.. code-block:: bash

	[root@server ~]# systemctl status firewalld
	[root@server ~]# systemctl stop firewalld
	[root@server ~]# systemctl disable firewalld
	[root@server ~]# systemctl status firewalld

4. 关闭SeLinux
-----------------
.. code-block:: bash

	[root@server ~]# cat /etc/selinux/config 
	    SELINUX=disabled
	[root@server ~]# setenforce 0

5. 查看系统是否安装git并卸载
-------------------------------
.. code-block:: bash

	[root@server ~]# git --version
	[root@server ~]# yum info git
	[root@server ~]# which git
	[root@server ~]# rpm -qa |grep git
	[root@server ~]# yum remove git -y

6. 安装git
-------------
.. code-block:: bash

	[root@server ~]# mkdir /usr/local/git
	[root@server git]# cd /usr/local/git
	[root@server git]# wget https://github.com/git/git/archive/v2.24.1.tar.gz
	[root@server git]# wget https://codeload.github.com/git/git/tar.gz/v2.24.1
	[root@server git]# tar -xzvf git-2.24.1.tar.gz -C /home/
	[root@server git]# cd /home/git-2.24.1/
	[root@server git-2.24.1]# make prefix=/usr/local/git all
	[root@server git-2.24.1]# make prefix=/usr/local/git install
	[root@server git-2.24.1]# git --version

7. 配置git
-------------
.. code-block:: bash

	#加入环境变量
	[root@server ~]# vi /etc/profile
	    export PATH="/usr/local/git/bin:$PATH"
	
	[root@server ~]# source /etc/profile
	[root@server ~]# git --version
	[root@server ~]# which git
	[root@server ~]# ln -s /usr/local/git/bin/git-upload-pack /usr/bin/git-upload-pack
	[root@server ~]# ln -s /usr/local/git/bin/git-receive-pack /usr/bin/git-receive-pack
	
	#创建用户及群组git
	[root@server ~]# groupadd git
	[root@server ~]# useradd git -g git
	[root@server ~]# passwd git
	
8. 服务器端启用RSA认证
------------------------
.. code-block:: bash

	[root@server ~]# vi /etc/ssh/sshd_config 
	    RSAAuthentication yes
	    PubkeyAuthentication yes
	    AuthorizedKeysFile /home/git/.ssh/authorized_keys  #默认位置.ssh/authorized_keys
	
	[root@server ~]# systemctl restart sshd
	
	[root@server ~]# mkdir -p /home/git/.ssh
	[root@server ~]# touch /home/git/.ssh/authorized_keys
	[root@server ~]# chown -R git:git /home/git/.ssh/
	[root@server ~]# systemctl restart sshd
	
	[root@server ~]# git config --global user.name 'username'
	[root@server ~]# git config --global user.email 'email@163.com'
	#期间会让你输入一个密码，这个密码在你提交代码到Github时会用到，可留空或自己使用可设置与Github密码一样不容易忘记
	
9. 客户端公钥上传到服务器
----------------------------
.. code-block:: bash

	[root@client ~]# ssh-keygen -t rsa -b 2048 -C '描述信息或直接写邮箱'
	
	[root@client ~]# ssh git@git_server_ip 'cat >> /home/git/.ssh/authorized_keys' < ~/.ssh/id_rsa.pub

10. 修改.ssh文件权限
----------------------
.. important::

 - [root@server ~]# chmod 700 /home/git/.ssh
 - [root@server ~]# chmod 600 /home/git/.ssh/authorized_keys

11. 使用git用户创建裸仓库
---------------------------
.. code-block:: bash

	#git未禁止SSH登陆
	[root@server ~]# cat /etc/passwd|grep git
	    git:x:1001:1001::/home/git:/bin/bash
		
	[root@server ~]# mkdir -p /mydev/gitprojects/
	
	[root@server ~]# ls -al /mydev/
	    drwxr-xr-x. 14 root root 12288 Apr  9 10:57 .
	    dr-xr-xr-x. 19 root root  4096 Dec  3  2019 ..
	    drwxr-xr-x   2 root root  4096 Apr  9 10:57 gitprojects
	
	[root@server ~]# chown -R git:git /mydev/gitprojects/
	
	[root@server ~]# ls -al /mydev/gitprojects/
	    drwxr-xr-x   2 git  git   4096 Apr  9 10:57 .
	    drwxr-xr-x. 14 root root 12288 Apr  9 10:57 ..
	    
	[root@server ~]# ls -al /mydev
	    drwxr-xr-x. 14 root root 12288 Apr  9 10:57 .
	    dr-xr-xr-x. 19 root root  4096 Dec  3  2019 ..
	    drwxr-xr-x   2 git  git   4096 Apr  9 10:57 gitprojects
	
	[root@server ~]# su git
	[git@server root]$ cd /mydev/gitprojects/
	
	[git@server gitprojects]$ git init --bare gitstudy.git
	    Initialized empty Git repository in /mydev/gitprojects/gitstudy.git/
		
	[git@server gitprojects]$ ls -al
	    drwxr-xr-x   3 git  git   4096 Apr  9 11:07 .
	    drwxr-xr-x. 14 root root 12288 Apr  9 10:57 ..
	    drwxrwxr-x   7 git  git   4096 Apr  9 11:07 gitstudy.git

12. 使用root用户创建裸仓库
----------------------------
.. code-block:: bash

	#git用户已禁用SSH登陆
	[root@server ~]# cat /etc/passwd|grep git
	    git:x:501:503::/home/git:/usr/bin/git-shell
		
	[root@server ~]# ls -al /mydev/
	    drwxr-xr-x.  6 root root     4096 Apr  9 10:49 .
	    dr-xr-xr-x. 23 root root     4096 Apr  5 17:34 ..
		
	[root@server ~]# mkdir -p /mydev/gitprojects
	[root@server ~]# cd /mydev/gitprojects
	
	[root@server gitprojects]# git init --bare gitstudy2.git
	    Initialized empty Git repository in /mydev/gitprojects/gitstudy2.git/
		
	[root@server gitprojects]# ls -al
	    drwxr-xr-x  3 root root 4096 Apr  9 11:15 .
	    drwxr-xr-x. 7 root root 4096 Apr  9 11:14 ..
	    drwxr-xr-x  7 root root 4096 Apr  9 11:15 gitstudy2.git
		
	[root@server gitprojects]# chown -R git:git gitstudy2.git/
	
	[root@server gitprojects]# ls -al
	    drwxr-xr-x  3 root root 4096 Apr  9 11:15 .
	    drwxr-xr-x. 7 root root 4096 Apr  9 11:14 ..
	    drwxr-xr-x  7 git  git  4096 Apr  9 11:15 gitstudy2.git

13. 禁止git用户使用shell登陆操作
----------------------------------
.. code-block:: bash

	#搭建git服务器后通常会建立一个git账户, 其它人共用这个账户来克隆或推送数据到git仓库中.
	#通常也只需要这个功能, 但是如果不加限制, 那么其它人可以通过这个git账户登录到主机, 那么这样是不安全的.
	#现在, git用户就只能进行push和pull操作, 而不能用ssh来连接服务器了.
	[root@server ~]# chsh git -s $(which git-shell)
	[root@server ~]# cat /etc/passwd|grep git
	    git:x:502:504::/home/git:/bin/git-shell

14. 客户端clone远程仓库
-------------------------
.. code-block:: bash

	[root@client ~]# git clone git@git_server_ip:/mydev/gitprojects/gitstudy2.git
