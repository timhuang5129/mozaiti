Redis_Docker
===============

1. 安装配置
---------------
::

	[root@docker01 ~]# docker run -it --name redis_507 -d --restart=always -p 6379:6379 redis:latest --requirepass "123456"
		
	[root@docker01 ~]# docker ps
	    CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                               NAMES
	    5dd61167545b        redis:latest        "docker-entrypoint.s"   3 seconds ago       Up 1 second         0.0.0.0:6379->6379/tcp              redis_507
		
	[root@docker01 ~]# docker exec -it redis_507 /bin/bash
	    root@5dd61167545b:/data# redis-cli
	    127.0.0.1:6379> set test 1
	    OK
	    127.0.0.1:6379> exit
	    root@5dd61167545b:/data# exit
	    exit
