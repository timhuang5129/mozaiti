Jumpserver_docker
====================

1. 安装配置
--------------
::

	[root@Docker01 ~]# mysql -uroot -p123456 -h127.0.0.1
	    #create database jumpserver default charset 'utf8mb4';
	    mysql> CREATE DATABASE jumpserver CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_general_ci';
	    mysql> GRANT ALL PRIVILEGES ON jumpserver.* TO 'jumpser'@'192.168.1.17' IDENTIFIED BY 'db123456';
	    mysql> flush privileges;
	[root@Docker01 ~]# mkdir -p /mydev/mysql
	[root@Docker01 ~]# mkdir -p /mydev/jumpserver
	[root@Docker01 ~]# docker run --name jumpser_292 -it -d --restart=always -v /mydev/mysql:/var/lib/mysql -v /mydev/jumpserver:/opt/jumpserver/data/media -p 80:80 -p 2222:2222 -e SECRET_KEY=xxxxxxxxxxxx -e BOOTSTRAP_TOKEN=xxxxxx -e DB_HOST=192.168.1.17 -e DB_PORT=3306 -e DB_USER=jumpser -e DB_PASSWORD='db123456' -e DB_NAME=jumpserver -e REDIS_HOST=192.168.1.17 -e REDIS_PORT=6379 -e REDIS_PASSWORD=123456 jumpserver/jms_all:v2.9.2
	[root@Docker01 ~]# docker logs -f --tail=35 jumpser_292
	[root@Docker01 ~]# docker exec -it jumpser_292 /bin/bash
