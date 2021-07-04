Docker安装
===============

.. important::

 - 安装应用容器如mysql, 注意时区问题, 加上 -e TZ=Asia/Shanghai
 - 避免/var/lib/docker撑爆根分区/, 应在分区时划分data, 并重定向
 - 或一开始就限制容器日志大小
 - [root@docker01 ~]# systemctl stop docker
 - [root@docker01 ~]# mkdir -pv /mydev/dockerlib
 - [root@docker01 ~]# cp -r /var/lib/docker  /mydev/dockerlib
 - [root@docker01 ~]# mv /var/lib/docker /var/lib/docker.bak
 - [root@docker01 ~]# ln -s /mydev/dockerlib /var/lib/docker
 - [root@docker01 ~]# ls -al /var/lib/
 - lrwxrwxrwx   1 root    root      18 May  3 19:55 docker -> /mydev/dockerlib/
 - [root@docker01 ~]# systemctl start docker
 - [root@docker01 ~]# docker info

1. 基本命令
----------------------
 - docker info                      #查看docker信息
 - docker images                    #查看所有镜像
 - docker images -q                 #查看所有镜像的ID
 - docker ps                        #列出正在运行的容器
 - docker ps -a                     #列出所有容器
 - docker ps -aq                    #列出所有容器的ID
 - docker stop $(docker ps -aq)     #停止所有容器
 - docker rm $(docker ps -aq)       #删除所有容器
 - docker rmi $(docker images -aq)  #删除所有镜像
 - docker run -d server_port1:docker_port2 image_name:image_version #启动一个WEB应用的容器,浏览器访问http://server_ip:server_port1
 - docker load -i /home/hello-world-docker.tar  #镜像导入
 - docker save -o /home/hello-world-docker.tar hello-world:latest  #镜像导出

2. 基本配置
----------------------
.. code-block:: bash

	#设置主机名
	[root@docker01 ~]# hostnamectl --static set-hostname  docker-test

	#查看系统版本
	[root@docker01 ~]# cat /etc/redhat-release
	    CentOS Linux release 7.5.1804 (Core) Mini Install

	#硬盘大小及分区
	60G[boot/swap//]

	#关闭SELinux, Firewalld及history命令保存数量
	[root@docker01 ~]# vi /etc/selinux/config
	    SELINUX=disabled
	[root@docker01 ~]# setenforce 0
	[root@docker01 ~]# sestatus
	    SELinux status:                 disabled

	[root@docker01 ~]# systemctl stop firewalld
	[root@docker01 ~]# systemctl status firewalld
	[root@docker01 ~]# systemctl disable firewalld

	[root@docker01 ~]# echo $HISTSIZE
	[root@docker01 ~]# sed -i 's/^HISTSIZE=1000/HISTSIZE=100000/' /etc/profile
	[root@docker01 ~]# source /etc/profile

	#保存yum在线安装下载的RPM包
	[root@docker01 ~]# find / -name yum.conf
	    /etc/yum.conf
	[root@docker01 ~]# vi /etc/yum.conf
	    cachedir=/var/cache/yum/$basearch/$releasever
	    keepcache=1
	    metadata_expire=1800m

3. 在线部署
-----------------------
.. code-block:: bash

	[root@docker01 ~]# yum install -y yum-utils device-mapper-persistent-data lvm2
	
	[root@docker01 ~]# yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
	
	[root@docker01 ~]# yum makecache fast
	
	[root@docker01 ~]# rpm --import  https://mirrors.aliyun.com/docker-ce/linux/centos/gpg
	[root@docker01 ~]# yum list docker-ce --showduplicates |sort -r
	[root@docker01 ~]# yum list docker-ce-cli --showduplicates |sort -r
	
	[root@docker01 ~]# yum -y install docker-ce-18.09.8 docker-ce-cli-18.09.8
	
	[root@docker01 ~]# rpm -qa|grep docker 或 yum list installed | grep docker
	    containerd.io.x86_64                 1.2.6-3.3.el7                  @docker-ce-stable
	    docker-ce.x86_64                     3:18.09.8-3.el7                @docker-ce-stable
	    docker-ce-cli.x86_64                 1:18.09.8-3.el7                @docker-ce-stable

	
	[root@docker01 ~]# systemctl enable docker
	    Created symlink from /etc/systemd/system/multi-user.target.wants/docker.service to /usr/lib/systemd/system/docker.service.
	
	[root@docker01 ~]# systemctl start docker

	[root@docker01 ~]# docker --version
		Docker version 18.09.8, build 0dd43dd87f

	#确保client和server版本一致
	[root@docker01 ~]# docker version
	    Client:
	     Version:           18.09.8
	     API version:       1.39
	     Go version:        go1.10.8
	     Git commit:        0dd43dd87f
	     Built:             Wed Jul 17 17:40:31 2019
	     OS/Arch:           linux/amd64
	     Experimental:      false
	
	    Server: Docker Engine - Community
	     Engine:
	     Version:          18.09.8
	     API version:      1.39 (minimum version 1.12)
	     Go version:       go1.10.8
	     Git commit:       0dd43dd
	     Built:            Wed Jul 17 17:10:42 2019
	     OS/Arch:          linux/amd64
	     Experimental:     false
	
	[root@docker01 ~]# docker info
	    Client:
	     Debug Mode: false

	    Server:
	     ......
	     Docker Root Dir: /var/lib/docker  #默认路径
	     ......

4. 离线部署
-----------------------
.. code-block:: bash

	#删除yum缓存
	[root@docker01 ~]# rm -rf /var/cache/yum/*

	#把在线安装完成的同类型系统版本/var/cache/yum/下的x86_64拷贝过来
	[root@docker01 ~]# ls /var/cache/yum/x86_64/7/
	    base  c7-media  docker-ce-stable  extras  timedhosts  timedhosts.txt  updates

	#配置本地YUM源,创建新的Docker.repo, 对应/var/cache/yum/x86_64/7的目录(base,updates...),且把gpgcheck设置为0
	[root@docker01 ~]# cp /etc/yum.repos.d/CentOS-Media.repo /etc/yum.repos.d/CentOS-Media.repo.bak
	[root@docker01 ~]# mv /etc/yum.repos.d/CentOS-Media.repo /etc/yum.repos.d/Docker.repo
	[root@docker01 ~]# vi /etc/yum.repos.d/Docker.repo
	    [c7-media]
	    name=CentOS-$releasever - Media
	    baseurl=file:///media/CentOS/
	    #       file:///media/cdrom/
	    #       file:///media/cdrecorder/
	    gpgcheck=1
	    enabled=1
	    gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
        
	    [base]
	    name=CentOS-$releasever - Base
	    baseurl=file:///media/CentOS/
	    gpgcheck=0
	    enabled=1
	    gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
        
	    [docker-ce-stable]
	    name=CentOS-$releasever - Media
	    baseurl=file:///media/CentOS/
	    gpgcheck=0
	    enabled=1
	    gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
	
	    [extras]
	    name=CentOS-$releasever - Extras
	    baseurl=file:///media/CentOS/
	    gpgcheck=0
	    enabled=1
	    gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
        
	    [updates]
	    name=CentOS-$releasever - Updates
	    baseurl=file:///media/CentOS/
	    gpgcheck=0
	    enabled=1
	    gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
	
	#刷新YUM缓存
	[root@docker01 ~]# yum makecache fast

	#安装不检查数字签名
	#sudo yum -y install 软件名 --nogpgcheck
	#-C指定从YUM缓存中安装/更新
	[root@docker01 ~]# yum -C  install -y yum-utils device-mapper-persistent-data lvm2
	[root@docker01 ~]# yum -C update device-mapper device-mapper-libs

	#确保client和server版本一致,亦可指定containerd.io版本
	[root@docker01 ~]# yum -C install -y docker-ce-18.09.8 docker-ce-cli-18.09.8

	#开机启动
	[root@docker01 ~]# systemctl enable docker
	[root@docker01 ~]# systemctl start docker

	[root@docker01 ~]# docker --version
	#确保client和server版本一致
	[root@docker01 ~]# docker version
	[root@docker01 ~]# docker info

5. 测试
-------------------
.. code-block:: bash

	#加载并测试Docker安装是否成功
	[root@docker01 ~]# docker load -i /home/hello-world-docker.tar
	[root@docker01 ~]# docker images
	[root@docker01 ~]# docker run hello-world

	#镜像导出为tar
	[root@docker01 ~]# docker save -o /home/hello-world-docker.tar hello-world:latest

6. 重装Docker
----------------------
.. code-block:: bash

	#先卸载旧版本
	[root@docker01 ~]# yum list installed | grep docker
	[root@docker01 ~]# yum remove -y docker-*
	[root@docker01 ~]# mv /var/lib/docker /tmp/

	#其他步骤同上

7. 在线安装
--------------
::

	[root@docker01 ~]# yum install -y yum-utils device-mapper-persistent-data lvm2
	
	[root@docker01 ~]# yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo

	[root@docker01 ~]# yum makecache fast

	[root@docker01 ~]# rpm --import  https://mirrors.aliyun.com/docker-ce/linux/centos/gpg

	[root@docker01 ~]# yum list docker-ce --showduplicates |sort -r

	[root@docker01 ~]# yum list docker-ce-cli --showduplicates |sort -r

	[root@docker01 ~]# yum -y install docker-ce-20.10.6 docker-ce-cli-20.10.6
	    Installed:
	      docker-ce.x86_64 3:20.10.6-3.el7                             docker-ce-cli.x86_64 1:20.10.6-3.el7                                                            
        
	    Dependency Installed:
	      audit-libs-python.x86_64 0:2.8.5-4.el7                       checkpolicy.x86_64 0:2.5-8.el7
	      container-selinux.noarch 2:2.119.2-1.911c772.el7_8           containerd.io.x86_64 0:1.4.4-3.1.el7       
	      docker-ce-rootless-extras.x86_64 0:20.10.6-3.el7             docker-scan-plugin.x86_64 0:0.7.0-3.el7  
	      fuse-overlayfs.x86_64 0:0.7.2-6.el7_8                        fuse3-libs.x86_64 0:3.6.1-4.el7            
	      libcgroup.x86_64 0:0.41-21.el7                               libseccomp.x86_64 0:2.3.1-4.el7          
	      libsemanage-python.x86_64 0:2.5-14.el7                       policycoreutils-python.x86_64 0:2.5-34.el7 
	      python-IPy.noarch 0:0.75-6.el7                               setools-libs.x86_64 0:3.3.8-4.el7        
	      slirp4netns.x86_64 0:0.4.3-4.el7_8                 
        
	    Complete!

	#cp -r /var/lib/docker /mydev/dockerlib
	#mv /var/lib/docker /var/lib/docker.bak
	[root@docker01 ~]# mv /var/lib/docker/* /mydev/dockerlib/
	[root@docker01 ~]# rm -rf /var/lib/docker
	[root@docker01 ~]# ln -s /mydev/dockerlib/ /var/lib/docker
	[root@docker01 ~]# ls -al /var/lib/
	    lrwxrwxrwx   1 root    root      18 May  3 19:55 docker -> /mydev/dockerlib/
	
	[root@docker01 ~]# systemctl enable docker
	    Created symlink from /etc/systemd/system/multi-user.target.wants/docker.service to /usr/lib/systemd/system/docker.service.
	
	[root@docker01 ~]# systemctl start docker
	[root@docker01 ~]# systemctl status docker
		
	[root@docker01 ~]# docker ps
	    CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
	
	[root@docker01 ~]# docker --version
	    Docker version 20.10.6, build 370c289
	
	[root@docker01 ~]# docker version
	    Client: Docker Engine - Community
	     Version:           20.10.6
	     API version:       1.41
	     Go version:        go1.13.15
	     Git commit:        370c289
	     Built:             Fri Apr  9 22:45:33 2021
	     OS/Arch:           linux/amd64
	     Context:           default
	     Experimental:      true
        
	    Server: Docker Engine - Community
	     Engine:
	      Version:          20.10.6
	      API version:      1.41 (minimum version 1.12)
	      Go version:       go1.13.15
	      Git commit:       8728dd2
	      Built:            Fri Apr  9 22:43:57 2021
	      OS/Arch:          linux/amd64
	      Experimental:     false
	     containerd:
	      Version:          1.4.4
	      GitCommit:        05f951a3781f4f2c1911b05e61c160e9c30eaa8e
	     runc:
	      Version:          1.0.0-rc93
	      GitCommit:        12644e614e25b05da6fd08a38ffa0cfe1903fdec
	     docker-init:
	      Version:          0.19.0
	      GitCommit:        de40ad0
	
	[root@docker01 ~]# docker info
	    Client:
	     Context:    default
	     Debug Mode: false
	     Plugins:
	      app: Docker App (Docker Inc., v0.9.1-beta3)
	      buildx: Build with BuildKit (Docker Inc., v0.5.1-docker)
	      scan: Docker Scan (Docker Inc.)
        
	    Server:
		 ......
	     Docker Root Dir: /mydev/dockerlib
	     ......
	
	[root@docker01 ~]# reboot
