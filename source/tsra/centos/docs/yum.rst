YUM配置管理
-------------
::

	cat /etc/yum.conf
	cat /etc/yum.repos.d/xx.repo
	cat /var/log/yum.log

	yum install -y xxx
	#只会删除指定包, 不会删除附加依赖包
	yum remove -y xxx

	#列出当前可以仓库
	yum repolist

	#@为已安装
	yum list | less

	yum search xxx
	#查看文件属于哪个包提供的
	yum provides /etc/yum.conf

	#查看包说明
	yum info httpd
	#查看已安装的包说明
	yum -qi httpd

	cat /var/cache/yum
	du -sh /var/cache/yum
	yum makecache
	yum clean all
	#可以撤销安装或重新安装
	yum history
	yum history info 5
	yum history undo 5

	yum history redo 5


	[root@cos7618-dev-gui ~]# yum grouplist
	Available Environment Groups:
	   Minimal Install
	   Compute Node
	   Infrastructure Server
	   File and Print Server
	   Basic Web Server
	   Virtualization Host
	   Server with GUI
	   GNOME Desktop
	   KDE Plasma Workspaces
	   Development and Creative Workstation
	Available Groups:
	   Compatibility Libraries
	   Console Internet Tools
	   Development Tools
	   Graphical Administration Tools
	   Legacy UNIX Compatibility
	   Scientific Support
	   Security Tools
	   Smart Card Support
	   System Administration Tools
	   System Management

	yum groupinstall "GNOME Desktop"
	yum groupinfo "GNOME Desktop"
	yum groupupdate "GNOME Desktop"
	yum groupremove "GNOME Desktop"


	RPM
	---------------
	rpm -ivh xxx
	rpm -qa|grep mysql
