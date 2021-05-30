基础知识
================
	系统学习

1. 时区
----------
::

	#https://blog.csdn.net/solaraceboy/article/details/78831319
	#https://www.cnblogs.com/alen-liu-sz/p/12975590.html
	
	GMT(Greenwich Mean Time)：格林威治标准时间

	UTC：世界标准时间

	CST(China Standard Time)：中国标准时间

	GMT + 8 = UTC + 8 = CST


2. 修改系统时区
------------------
::

	[root@cos7618-dev-gui ~]# docker ps
	    CONTAINER ID        IMAGE                       COMMAND                  CREATED             STATUS              PORTS                                        NAMES
	    f631dd0c2392        mysql:5.7.27                "docker-entrypoint.s…"   11 days ago         Up 11 days          33060/tcp, 0.0.0.0:3311->3306/tcp            mysql_v5.7.27
	
	[root@cos7618-dev-gui ~]# docker exec -it mysql_v5.7.27 /bin/bash
	
	root@f631dd0c2392:/# cat /etc/hostname
	    f631dd0c2392
	
	root@f631dd0c2392:/# cat /etc/debian_version
	    9.9
	
	root@f631dd0c2392:/# date -R
	    Fri May 14 07:18:11 UTC 2021
	
	#方法1
	root@f631dd0c2392:/# timedatectl
	root@f631dd0c2392:/# timedatectl list-timezones
	root@f631dd0c2392:/# timedatectl set-timezone Asia/Shanghai
	
	#方法2
	root@f631dd0c2392:/# rm -rf /etc/localtime
	root@f631dd0c2392:/# ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
	
	root@f631dd0c2392:/# date -R
	    Fri May 14 15:30:02 CST 2021 +8:00


3. telnet
-----------------------
.. code-block:: bash

	[root@BJ-JUMPSER-T01 ~]# cat /etc/centos-release
	    CentOS Linux release 7.9.2009 (Core)
	
	#配置yum源
	[root@BJ-JUMPSER-T01 ~]# curl -sSLf 192.168.1.20/repo/bj-yum.sh |bash
	
	[root@BJ-JUMPSER-T01 ~]# yum -y install telnet
	    Installed:
	      telnet.x86_64 1:0.17-66.el7                                                                                                                                                                  
        
	    Complete!
	
	#不通
	[root@BJ-JUMPSER-T01 ~]# telnet 192.168.1.100 5900
	Trying 192.168.1.100...
	
	[root@BJ-JUMPSER-T01 ~]# ip route show
	    192.0.0.0/8 via 192.168.1.1 dev eth1 proto static metric 101
	
	[root@BJ-JUMPSER-T01 ~]# ping 192.168.1.100
	    PING 192.168.1.100 (192.168.1.100) 56(84) bytes of data.
	    64 bytes from 192.168.1.100: icmp_seq=1 ttl=125 time=0.789 ms
	
	#检查防火墙,本机到192段的网络权限是否有封锁端口或网段等
	[root@BJ-JUMPSER-T01 ~]# telnet 192.168.1.100 5900
	    Trying 192.168.1.100...
	    Connected to 192.168.1.100.
	    Escape character is '^]'.
	    RFB 005.000
	    Connection closed by foreign host.

4. 禁用root通过SSH登陆
-------------------------
.. code-block:: bash

	[root@BJ-JUMPSER-T01 ~]# sed -i 's/#PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config
	[root@BJ-JUMPSER-T01 ~]# cat /etc/ssh/sshd_config|grep PermitRootLogin
	    PermitRootLogin no
	[root@BJ-JUMPSER-T01 ~]# systemctl restart sshd

5. 授权
----------
::

	%sudo ALL=(ALL:ALL) NOPASSWD:ALL
	https://blog.csdn.net/anqixiang/article/details/105220403
	https://blog.csdn.net/gianttj/article/details/84877962

6. ssh代理
-------------
::

	https://blog.csdn.net/octansneu/article/details/53317369
