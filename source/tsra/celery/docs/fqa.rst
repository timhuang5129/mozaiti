1. Celery时区问题
--------------------
.. hint::

 - `[celery在django的USE_TZ为False时不停的执行任务调度] <https://www.codeleading.com/article/8970428909/>`_
 - `[celery 4.1.0 版本定时任务执行时间 bug] <http://www.axiaoxin.com/article/228/>`_
 - `[celery中的时区陷阱] <https://www.dazhuanlan.com/2020/04/16/5e984f5d029ef/>`_
 - `[为什么Django设置时区为TIME_ZONE = 'Asia/Shanghai' USE_TZ = True后，存入mysql中的时间只能是UTC时间] <https://www.codeleading.com/article/75121548350/>`_

	# -*- coding: utf-8 -*-

	import os

	from kombu import Exchange, Queue
	from celery import Celery
	from django.conf import settings
	from django.utils import timezone
	import datetime

	app = Celery('myapp')

	app.namespace = 'CELERY'
	#app.now = datetime.datetime.now
	#app.now = timezone.now
	app.conf.update(configs)
	app.autodiscover_tasks('xxxxxxxxxxxxxxx')


	TIME_ZONE = 'Asia/Shanghai'

	USE_I18N = True

	USE_L10N = True

	USE_TZ = True

	# 不使用国际标准时间
	#CELERY_ENABLE_UTC = False

	# 使用亚洲/上海时区
	CELERY_TIMEZONE = TIME_ZONE

	# 解决时区问题
	#DJANGO_CELERY_BEAT_TZ_AWARE = False


	Package                   Version
	
	------------------------- ---------
	
	aioredis                  1.3.1
	
	asgiref                   3.2.3
	
	celery                    4.4.7
	
	Django                    2.1.11
	
	django-celery-beat        1.4.0
	
	django-celery-results     1.0.4
	
	django-redis              4.11.0
	
	django-redis-cache        2.1.1
	
	django-redis-sessions     0.6.1
	
	django-rest-swagger       2.1.2
	
	django-timezone-field     3.1
	
	flower                    0.9.3
	
	kombu                     4.6.11
	
	paramiko                  2.4.2
	
	python-crontab            2.4.0
	
	pytz                      2018.3
	
	redis                     3.5.3
