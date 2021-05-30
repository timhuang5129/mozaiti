1. 模型定义注意事项
-----------------------
::

	auto_now_add不是一个好的方法。避免使用它。最好的方法是使用设置默认值：
	date_created = models.DateTimeField(default=timezone.now)
	date_created = models.DateTimeField(default=datetime.now)
	注意timezone.now后面缺少()，这是因为我们正在向模型传递一个callable，每次保存一个新实例时都会调用它。
    定义模型时不应初始化datetime.now（）, 这会导致某种“缓存”, 应使用datetime.now.


2. MySQL存储时间
-------------------
::

	#Django 使用 MySQL 存储时间中遇到的问题(在数据库中记录插入时间、更新时间、删除时间)
	https://www.cnblogs.com/alan-babyblog/p/5739004.html
	https://www.cnblogs.com/catgatp/p/13178847.html
	https://blog.csdn.net/ichuzhen/article/details/38555645
	https://www.jb51.net/article/142037.htm

	import pytz
	from datetime import datetime
	from django.utils import timezone

	#Django的settings.py
	#建议设置USE_TZ=True来使用Django提供的时区机制
	TIME_ZONE = 'Asia/Shanghai'
	USE_TZ = True

	mac_obj = MAC.objects.first()
	logger.debug(mac_obj.m_time)
	logger.debug(datetime.now())
	logger.debug(datetime.now().replace(tzinfo=pytz.timezone('UTC')))
	logger.debug(datetime.now().replace(tzinfo=None))
	logger.debug(datetime.utcnow().astimezone()- mac_obj.m_time)
	logger.debug((datetime.utcnow().astimezone()- mac_obj.m_time).seconds)
	logger.debug(datetime.utcnow().astimezone())
	logger.debug(timezone.is_naive(mac_obj.m_time))  #判断是否为本地时间
	logger.debug(timezone.is_naive(datetime.now()))
	logger.debug(timezone.is_naive(timezone.now()))
	logger.debug(timezone.now())
	logger.debug((timezone.now() - mac_obj.m_time).seconds)
	#datetime.now().replace(tzinfo=pytz.timezone('UTC')) - mac_obj.m_time
	if mac_obj and (timezone.now() - mac_obj.m_time).total_seconds()<59:
	    return JsonResponse({"status": "Do not refresh frequently.})
