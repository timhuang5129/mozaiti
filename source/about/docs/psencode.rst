PS编码问题
=============
.. hint::

 - Win10+windows server+系统均为繁体字
 - python3+pywinrm

1. 查看系统编码
------------------
::

	#查看windows server编码
	PS C:\Users\S1111111> chcp
	    使用中的字碼頁: 950   #即big5编码

2. 不改源码方法
------------------
::

	#调用Protocol()中的open_shell(), 而open_shell()可以设置编码格式, 因此直接使用Protocol()不用改源码
	conn = winrm.protocol.Protocol(endpoint='http://'+host_tuple[0]+':'+host_tuple[1]+'/wsman', transport='ntlm', username=host_tuple[2], password=host_tuple[3])
	load_script = conn.open_shell(env_vars=dict(WINRM_PS_SCRIPT=_ps_script), codepage=950)

3. 改源码方法
----------------
::

	#源码中run_ps()本质上是调用run_cmd(), 而run_cmd()本质又是调用Protocol()中的open_shell(), 
	#而open_shell()可以设置编码格式, 因此直接使用Protocol()不用改源码,
	#如果非要使用Session(), 则修改源码
	conn = winrm.Session(ip, auth=(uid, pwd), transport='ntlm')
	res = conn.run_cmd(_ps_script)
	res = conn.run_ps(_ps_script)
	
	#修改pywinrm源码__init__.py
	#jumpserver路径vi /opt/py3/lib64/python3.6/site-packages/winrm/__init__.py
	
	def run_cmd(self, command, args=()):
	    # TODO optimize perf. Do not call open/close shell every time
	    # shell_id = self.protocol.open_shell()		        # 原代码, 默认codepage=437为英文编码
	    shell_id = self.protocol.open_shell(codepage=950)	# 修改后代码
	
4. 示例
----------
.. hidden-code-block:: bash
	:starthidden: False
	:linenos:
	:label: + get_win_sysinfo.ps1
	
	$a=Get-wmiobject Win32_ComputerSystemProduct
	return ($a|convertto-json -depth 99)

.. raw:: html

	<hr width="700" size="20"/>

.. hidden-code-block:: python
	:starthidden: False
	:linenos:
	:label: + winrm_test.py

	#!/usr/bin/env python3
	# -*- coding: utf-8 -*-
	#
	import os
	import sys
	import logging
	import winrm
	from base64 import b64encode
	from winrm.exceptions import WinRMTransportError
	
	logger = logging.getLogger("django")
	
	_ps_script = ""
	try:
	    with open(os.path.join(os.path.realpath(os.path.dirname(__file__)), 'get_win_sysinfo.ps1'), 'r', encoding='utf-8') as ps_file:
	        _ps_script = ps_file.read()
	        logger.info("Read get_win_sysinfo.ps1 success!!!")
	except Exception as e:
	    print(e)
	    logger.error("Read get_win_sysinfo.ps1 failed!!!")
	
	_ps_env_vars = """. ([ScriptBlock]::Create($Env:WINRM_PS_SCRIPT))"""
	
	try:
	    _encoded_ps = b64encode(_ps_env_vars.encode('utf_16_le')).decode('ascii')
	except Exception as e:
	    print('Coding exception: ', e)
	
	def winrm_session(host_tuple):
	    conn = winrm.Session(host_tuple[0], auth=(host_tuple[2], host_tuple[3]), transport='ntlm')
	    r = conn.run_ps(_ps_script)
	    print(str(r.std_out,'big5'))
	    print('51')
	
	def winrm_protocol(host_tuple):
	    """
	    :host_tuple: (ip,port,uname,upwd_aes)
	    :__encoded_ps: 
	    :__ps_script:
	    :WINRM_PS_SCRIPT: 环境变量,突破ps脚本太大
	    :return: res_list
	    """
        
	    conn = winrm.protocol.Protocol(
	        endpoint='http://'+host_tuple[0]+':'+host_tuple[1]+'/wsman', 
	        transport='ntlm', username=host_tuple[2], password=host_tuple[3])
            
	    load_script = conn.open_shell(env_vars=dict(WINRM_PS_SCRIPT=_ps_script), codepage=950)
	    exec_script = conn.run_command(load_script, "powershell -EncodedCommand {}".format(_encoded_ps))
	    res = winrm.Response(conn.get_command_output(load_script, exec_script))
	    conn.cleanup_command(load_script, exec_script)
	    print(str(res.std_out,'big5'))
	    print(res.std_out.decode('big5').replace('\n','').strip())

	if __name__ == '__main__':
	    import multiprocessing
	    multiprocessing.freeze_support()
	    print('test_start.....')
	    #'uid@domain' or 'domain\\uid'
	    test_host = (ip, '5985', domain\\uid, pwd)
	    winrm_protocol(test_host)
	    print('test_end......')
