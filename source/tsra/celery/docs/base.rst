1. Celery时区问题
--------------------
.. hint::

 - `[celery在django的USE_TZ为False时不停的执行任务调度] <https://www.codeleading.com/article/8970428909/>`_
 - `[celery 定时任务不执行的问题解决] <https://blog.csdn.net/Kwoky/article/details/104562735>`_

	CELERY_TIMEZONE = 'Asia/Shanghai'
	
	CELERY_ENABLE_UTC=True
	
	DJANGO_CELERY_BEAT_TZ_AWARE = False
	
	app.conf.enable_utc = True
	
	app.conf.timezone = "Asia/Shanghai"
