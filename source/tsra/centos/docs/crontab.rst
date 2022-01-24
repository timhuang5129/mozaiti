定时任务 - Crontab
======================

.. admonition:: 定时任务 - Crontab
	:class: dropdown, toggle-shown

	* 基本语法::

		*           *        *        *        *      user     command
		minute      hour    day       month   week    root   command
		分          时       天      月        星期   用户    命令

	* 语法示例::

		* * * * * root /bin/bash /root/test.sh   #每分钟执行1次, 默认
		*/1 * * * * root /bin/bash /root/test.sh   #每分钟执行1次
		1 0 * * * /root/bin/backup.sh    #在12:01AM运行
		59 11 * * 1,2,3,4,5 /root/bin/backup.sh    #每个工作日11:59p.m运行
		59 11 * * 1-5 /root/bin/backup.sh 
		#每5分钟运行一次命令 
		*/5 * * * * /root/bin/check-status.sh 
		#每个月的第一天1:10p.m运行 
		10 13 1 * * /root/bin/full-backup.sh 
		#每个工作日11p.m运行
		0 23 * * 1-5 /root/bin/incremental-backup.sh

	* 基本命令::

		crontab -l   #查看 
		crontab -r   #删除
		crontab -e   #创建
		vi /etc/crontab  #配置文件, 里面也可以创建任务

	* 注意事项::

		shell中使用绝对路径
		chmod a+x test.sh
		tail -f -n 10 /var/log/cron
		systemclt status crond

	.. seealso::
		:class: dropdown, toggle-shown

		::

			#!/bin/bash
			#########################################
			# Author:               xxx
			# Version:              1.0
			# Mail:                 xxx@xxx
			# Date:                 2022-01-23
			# Description:  /jumpsdata space recycle
			##########################################
			## del docker core_dump
			del_log="/home/prod-crontab/del_log.log"
			size_lg="-size +10M"
			counter=$(find /jumpsdata/docker/overlay2/12a97306a363c3aca3650560f08e65f7b37220b278dccd93e288fff7738d7c58/diff/core.* -type f -name "core.*" ${size_lg}|wc -l)
			if [ "${counter}" -ne 0 ]; then
				size_old=$(du -sm /jumpsdata/docker |awk '{print $1;}')
				find /jumpsdata/docker/overlay2/12a97306a363c3aca3650560f08e65f7b37220b278dccd93e288fff7738d7c58/diff/core.* -type f -name "core.*" ${size_lg} -exec rm -rf {} \;
				size_new=$(du -sm /jumpsdata/docker |awk '{print $1;}')
				echo "`date '+%Y-%m-%d %H:%M:%S'` This time delete ${counter} core.pids, recycle `expr ${size_old} - ${size_new}` MB" >> ${del_log}
			fi

			###########################################
			## media keep data for 55 days
			file_sys="xfs"
			media_mtime="-mtime +55"
			media_path="/jumpsdata/jumpserver/replay"
			check_partition="jumpsdata"

			function del_media(){
				hdisk_use=$(df -ht ${file_sys}|grep ${check_partition}|awk '{print $5}'|cut -f 1 -d '%')
				hdisk_avail_mb=$(df -hmt ${file_sys}|grep ${check_partition}|awk '{print $4}')
				if [ "${hdisk_use}" -gt 95 ];then
					echo "del replay_use"
					find ${media_path} -type d -name "202*" ${media_mtime}|xargs -i du -sh {}|xargs -i echo `date '+%Y-%m-%d %H:%M:%S'` {} >> ${del_log}
					find ${media_path} -type d -name "202*" ${media_mtime} -exec rm -rf {} \;
				elif [ ${hdisk_avail_mb} -lt 10240 ];then
					echo "del_replay_mb"
					find ${media_path} -type d -name "202*" ${media_mtime}|xargs -i du -sh {}|xargs -i echo `date '+%Y-%m-%d %H:%M:%S'` {} >> ${del_log}
					find ${media_path} -type d -name "202*" ${media_mtime} -exec rm -rf {} \;
				fi
			}
			del_media
