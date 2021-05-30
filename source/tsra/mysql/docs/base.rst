1. 何时使用commit
--------------------
::

	SQL语言分为五大类：
	    DDL(数据定义语言) - Create、Alter、Drop 这些语句自动提交，无需用Commit提交。
	    DQL(数据查询语言) - Select 查询语句不存在提交问题。
	    DML(数据操纵语言) - Insert、Update、Delete 这些语句需要Commit才能提交。
	    DTL(事务控制语言) - Commit、Rollback 事务提交与回滚语句。
	    DCL(数据控制语言) - Grant、Revoke 授予权限与回收权限语句。

2. MySQL时区
---------------
::

	#涉及两个参数：system_time_zone和time_zone。

	#全局参数system_time_zone
	系统时区，在MySQL启动时会检查当前系统的时区并根据系统时区设置全局参数system_time_zone的值。

	#全局参数time_zone
	用来设置每个连接会话的时区，默认为system时，使用全局参数system_time_zone的值。

	#参数log_timestamps
	用于设置Error Log/Genaral Log/Slow Log这三种日志的时间信息。
	有效值为UTC(默认)和SYSTEM(本地系统时区)，当设置为system时，会使用参数system_time_zone的值。

3. 常用命令
--------------
::

	#登录
	mysql -uroot -p

	#查看mysql系统时间。和当前时间做对比
	select now();
	select curtime();

	#查看系统时区
	show variables like '%time_zone%';

	#设置时区，更改为东八区，MySQL重启后失效，如不加global只在当前回话有效
	set global time_zone = '+8:00';

	#刷新权限
	flush privileges;

	#配置文件my.cnf修改时区，永久有效
	[mysqld]
	default-time_zone = '+8:00'

	#修改my.cnf需要重启MySQL
	sudo service mysql restart
