SSH
=======

SSH配置
----------
::

	[root@mx ~]# cat /etc/ssh/sshd_config 
	    #Port 22
	    PermitRootLogin yes
	    #PasswordAuthentication yes
	    #PermitEmptyPasswords no
	    PasswordAuthentication yes

SSH重启
----------
::

	[root@mx ~]# systemctl restart sshd
