基础知识
================
	系统学习

1. 类型判断
--------------
::

	isinstance(object, class-or-type-or-tuple)
	return True/False
	class,int,str,float,list,bool,complex,...,(int,str)

2. 简繁转换
--------------
::

	from zhconv import convert
	>>> convert('计算机软件', 'zh-tw')
	'計算機軟體'
	>>> convert('計算機軟體', 'zh-hans') # zh-hans只是逐字转换
	'计算机软体'
	>>> convert('計算機軟體', 'zh-cn')
	'计算机软件'

	支持 MediaWiki 人工转换语法
	>>> from zhconv import convert_for_mw

	当然对于复杂高精度的转换需求, 还是建议用专业的OpenCC 开源库

3. 检测文本编码
------------------
::

	codepage=936 简体中文GBK

	codepage=950 繁体中文BIG5

	codepage=437 美国/加拿大英语

	codepage=932 日文

	codepage=949 韩文

	codepage=866 俄文

	codepage=65001 UTF-8


	import chardet
	f_io = open('file','r')
	code_type =chardet.detect(f_io.read())

	os_name = b'\r\n    "Caption":  "\xb9q\xb8\xa3\xa8t\xb2\xce\xb2\xa3\xab~"'
	>>> import chardet
	>>> chardet.detect(a)
	{'encoding': 'Big5', 'confidence': 0.99, 'language': 'Chinese'}

	#系统编码
	>>> import locale
	>>> dir(locale)
	>>> locale.getdefaultlocale()
	('zh_TW', 'cp950')


4. Python中编码的转换
------------------------
::

	Python3中字符串在内存中是以unicode编码存在的，

	从网上下载，或者读文件，都是字节流，需要decode进行转换：

	utf-8 -> unicode 　　str.decode('utf-8')

	gbk -> unicode 　　str.decode('gbk')

	保存文件(把内容写到文件中)或者向网上发送数据，需要转换为字节流,即encode一下：

	unicode -> utf-8 　　 unicode.encode('utf-8')

	unicode -> gbk 　　 unicode.encode('gbk')

	utf-8 -> gbk ：首先把 utf-8 -> unicode ，再把unicode -> gbk：str.decode('utf-8','ignore').encode('gbk')

	gbk -> utf-8 ： gbk -> unicode，unicode -> utf-8 ： str.decode('gbk','ignore').encode('utf-8')

	def gbk2unicode(s):
	    return s.decode('gbk', 'ignore')
	def utf82unicode(s):
	    return s.decode('utf-8', 'ignore')
	def unicode2gbk(s):
	    return s.encode('gbk')
	def unicode2utf8(s):
	    return s.encode('utf-8') 
	def gbk2utf8(s):
	    return s.decode('gbk', 'ignore').encode('utf-8') 
	def utf82gbk(s):
	    return s.decode('utf-8', 'ignore').encode('gbk')
