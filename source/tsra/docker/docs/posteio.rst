Posteio_docker
=================
.. hint::

 - CentOS 7.6.1810 min
 - Docker 19.0.3
 - analogic/poste.io:latest

1. 时间同步
---------------
::

	xxxxxxxxxxxx

2. 关闭防火墙
-----------------
::

	[root@mx ~]# vi /etc/selinux/config 
	    SELINUX=disabled
	[root@mx ~]# setenforce 0
	
	[root@mx ~]# systemctl stop firewalld
	[root@mx ~]# systemctl disable firewalld
	
3. 配置IP
------------
::

	[root@mail ~]# vi /etc/sysconfig/network-scripts/ifcfg-eth0 
	    TYPE=Ethernet
	    PROXY_METHOD=none
	    BROWSER_ONLY=no
	    BOOTPROTO=static
	    DEFROUTE=yes
	    IPV4_FAILURE_FATAL=no
	    IPV6INIT=no
	    IPV6_AUTOCONF=yes
	    IPV6_DEFROUTE=yes
	    IPV6_FAILURE_FATAL=no
	    IPV6_ADDR_GEN_MODE=stable-privacy
	    NAME=eth0
	    UUID=xxxxx-58ed-xxx-xxxx-0xxxxx
	    DEVICE=eth0
	    ONBOOT=yes
	    IPADDR=192.168.1.119
	    PREFIX=24
	    GATEWAY=192.168.1.1
	    
	[root@mail ~]# systemctl restart network
    
4. 配置host及更改主机名
------ -------------------
::
  
	[root@mail ~]# vi /etc/hosts
	    127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
	    ::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
	    192.168.1.119 mx.tim.com
	
	[root@mail ~]# hostnamectl  set-hostname mx.tim.com
	[root@mail ~]# reboot
	
5. 下载并运行Poste.io容器
----------------------------
::

	[root@mx ~]# docker pull analogic/poste.io
	[root@mx ~]# docker save -o /home/poste.io.tar analogic/poste.io:latest
	[root@mx ~]# docker load -i /home/poste.io.tar
	[root@mx ~]# mkdir -pv /home/poste-mail/data
	
	#docker run -itd --restart=always --name "mailserver" -p 25:25 -p 80:80 -p 110:110 -p 143:143 -p 443:443 -p 465:465 -p 587:587 -p 993:993 -p 995:995 -v /etc/localtime:/etc/localtime:ro -v /allmails/data:/data –name "mx.tim.com" -h “mx.tim.com” -t analogic/poste.io
	[root@mx ~]# docker run -itd --restart=always --net=host -v /etc/localtime:/etc/localtime:ro -v /home/poste_mail/data:/data --name "mailserver" -h "mx.tim.com" -t analogic/poste.io
	
	    Poste.io administration available at https://192.168.1.119:443 or http://192.168.1.119:80  
	
	[root@mx ~]# docker logs -f mailserver

6. 访问
----------
::

	客户端PC添加hosts:  192.168.1.119 mx.tim.com
	首次访问https://192.168.1.119会进行基本设置
	浏览器访问https://192.168.1.119/admin/login
	https://192.168.1.119/webmail/
