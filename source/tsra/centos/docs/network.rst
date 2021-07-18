HyperV给CentOS6/7添加网卡
---------------------------
.. hint::

 - `[Linux克隆虚拟机问题] <https://blog.csdn.net/qq_41966005/article/details/98777675>`_
 - `[网卡名称自定义] <https://blog.csdn.net/gpcsy/article/details/83010112>`_

	1. 关闭VM, 添加网卡
	
	2. ifconfig或ip addr 查看网卡信息, 看下新增网卡是否存在
	
	3. ls /etc/sysconfig/network-scripts/ 看下新增的网卡eth1配置文件是否存在
	
	4. 如果2存在, 3不存在, 则拷贝cp ifcfg-eth0  ifcfg-eth1
	
	5. vi ifcfg-eth1
	    HWADD=通过ip addr获取
	    UUID=xxx  没有就删掉
	    NAME=eth1
	    DEVICE=eth1
	    IPADDR=
	    PREFIX=23  #NETMASK=255.255.254.0
	    GATEWAY=   #我们使用默认路由
	
	6. systemctl restart network
	
	7. 另外
	    禁用/启用 ifdowm/ifup eth1
	    启用图形界面systemctl start NetworkManager
	
	8. 如果2都不存在, 先重启系统看看
	
	9. mv /etc/udev/rules.d/70-persistent-net.rules /etc/udev/rules.d/bak.70-persistent-net.rules, 重启
	
	10. 添加默认路由 route add xxxx
	    或直接新增vi /etc/sysconfig/network-scripts/route-eth1写入以下后保存重启网卡服务
	    172.0.0.0/8 via 172.x.x.1(当前IP的网关)