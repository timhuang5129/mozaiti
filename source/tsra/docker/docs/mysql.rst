MySQL_Docker
===============

.. important::

 - 安装应用容器如mysql, 注意时区问题, 加上 -e TZ=Asia/Shanghai
 - `[MySQL中的排序规则] <https://www.jb51.net/article/48775.htm>`_
 - `[MySQL中的utf8mb4、utf8mb4_unicode_ci、utf8mb4_general_ci] <https://www.cnblogs.com/amyzhu/p/9595665.html>`_
 - `[MySQL默认字符集] <https://www.jb51.net/article/186609.htm>`_
  - MySQL 8.0.1及更高版本中,将 utf8mb4_0900_ai_ci 作为默认排序规则
  - utf8mb4_unicode_ci
 - 默认使用utf8mb4_general_ci
 - 总结
  - utf8_unicode_ci和utf8_general_ci对中、英文来说没有实质的差别。
  - utf8mb4_general_ci在比较和排序的时候更快,
  - 但是utf8mb4_unicode_ci比utf8mb4_general_ci要来得精确, 能够处理特殊字符。
  - utf8_general_ci校对速度快, 但准确度稍差。
  - utf8_unicode_ci准确度高, 但校对速度稍慢。

1. 基本命令
--------------
::

	[root@docker01 ~]# mysql -uroot -p123456 -h127.0.0.1
	    mysql> status;
	    mysql> show variables like "%character%";
	    mysql> show variables like "%collation%";
	    mysql> show databases;
	    mysql> use mysql;
	    mysql> show tables;
	    mysql> desc user;  #显示表的字段
	    mysql> select host,user from user;
	    mysql> drop user root@'172.17.0.1';  #删除用户
	    mysql> quit;
		
	    mysql> SHOW VARIABLES WHERE Variable_name LIKE 'character%' OR Variable_name LIKE 'collation%';
	    #修改数据库字符集
	    mysql> ALTER DATABASE database_name CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
	    #修改表的字符集
	    mysql> ALTER TABLE table_name CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
	    #修改字段的字符集
	    mysql> ALTER TABLE table_name CHANGE column_1 column_2 VARCHAR(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

2. 安装配置
----------------------
.. code-block:: bash

	[root@docker01 ~]# docker search mysql             

	[root@docker01 ~]# docker pull mysql:latest

	[root@docker01 ~]# docker images
		REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
		mysql               5.7.27              e1e1680ac726        5 months ago        373MB

	[root@docker01 ~]# docker save -o mysql-5.7.27-docker.tar mysql:latest

	[root@docker01 ~]# docker rmi mysql:latest
	[root@docker01 ~]# docker load -i /jumpsdata/softwares/mysql-5.7.27-docker.tar

	[root@docker01 ~]# mkdir -p /etc/mysql/mysql.conf.d
	[root@docker01 ~]# vi /etc/mysql/mysql.conf.d/my.cnf
	    [client]
	    default-character-set = utf8mb4
	    
	    [mysql]
	    default-character-set = utf8mb4
	    
	    [mysqld]
	    pid-file = /var/run/mysqld/mysqld.pid
	    socket = /var/run/mysqld/mysqld.sock
	    datadir = /var/lib/mysql
	    #log-error = /var/log/mysql/error.log
	    # Disabling symbolic-links is recommended to prevent assorted security risks
	    symbolic-links=0
	    character-set-client-handshake = FALSE
	    character-set-server = utf8mb4
	    collation-server = utf8mb4_general_ci
	    init_connect='SET NAMES utf8mb4'

	[root@docker01 ~]# mkdir -p /etc/mysql/conf.d/

	[root@docker01 ~]# vi /etc/mysql/conf.d/my.cnf 
	    [client]
	    default-character-set = utf8mb4
	    
	    [mysql]
	    default-character-set = utf8mb4
	    
	    [mysqld]
	    character-set-client-handshake = FALSE
	    character-set-server = utf8mb4
	    collation-server = utf8mb4_general_ci
	    init_connect='SET NAMES utf8mb4'
	
	#docker run -it --name mysql_v5.7.27 -d -p 3306:3306 -v /etc/mysql/mysql.conf.d:/etc/mysql/mysql.conf.d -v /etc/mysql/conf.d:/etc/mysql/conf.d -v /jumpsdata/mysql:/var/lib/mysql -e MYSQL_ROOT_PASSWORD="123456" mysql:5.7.27
	[root@docker01 ~]# docker run -it -d --restart=always -p 3306:3306 \
	>     -v /etc/mysql/mysql.conf.d/my.cnf:/etc/mysql/mysql.conf.d/mysqld.cnf \
	>     -v /etc/mysql/conf.d/my.cnf:/etc/mysql/conf.d/mysql.cnf \
	>     -v /jumpsdata/mysql:/var/lib/mysql \
	>     -e MYSQL_ROOT_PASSWORD="123456" \
	>     -e TZ=Asia/Shanghai \
	>     mysql:5.7.27
	
	[root@docker01 ~]# mysql -uroot -p123456 -h127.0.0.1
	    mysql> show variables like "%character%";
	    +--------------------------+----------------------------+
	    | Variable_name            | Value                      |
	    +--------------------------+----------------------------+
	    | character_set_client     | utf8mb4                    |
	    | character_set_connection | utf8mb4                    |
	    | character_set_database   | utf8mb4                    |
	    | character_set_filesystem | binary                     |
	    | character_set_results    | utf8mb4                    |
	    | character_set_server     | utf8mb4                    |
	    | character_set_system     | utf8                       |
	    | character_sets_dir       | /usr/share/mysql/charsets/ |
	    +--------------------------+----------------------------+
	    8 rows in set (0.01 sec)
        
	    mysql> show variables like "%collation%";
	    +----------------------+--------------------+
	    | Variable_name        | Value              |
	    +----------------------+--------------------+
	    | collation_connection | utf8mb4_general_ci |
	    | collation_database   | utf8mb4_general_ci |
	    | collation_server     | utf8mb4_general_ci |
	    +----------------------+--------------------+
	    3 rows in set (0.01 sec)
	    
		#编码修改
	    mysql> set character_set_connection=utf8mb4;
	    mysql> set character_set_client=utf8mb4;
	    mysql> set character_set_database=utf8mb4;
	    mysql> set character_set_results=utf8mb4;
	    mysql> set character_set_server=utf8mb4;
	    
		#创建数据库并授权远程访问: 允许用户user01通过远程主机192.168.1.169使用密码'pwd@20110.'访问数据库mydev_project的所有表
	    mysql> CREATE DATABASE mydev_project CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_general_ci';
	    mysql> GRANT ALL PRIVILEGES ON mydev_project.* TO 'user01'@'192.168.1.169' IDENTIFIED BY 'pwd@20110.';
	    mysql> flush privileges;
		
	    mysql> quit;
	    Bye

	[root@docker01 ~]# docker ps
	    CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                               NAMES
	    c340c8752c4a        mysql:5.7.27        "docker-entrypoint.s"   About an hour ago   Up About an hour    0.0.0.0:3306->3306/tcp, 33060/tcp   mysql_v5.7.27
	[root@docker01 ~]# docker exec -it mysql_v5.7.27 /bin/bash
