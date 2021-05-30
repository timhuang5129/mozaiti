实时迁移
===========
.. hint:: 

 - Windows Server 2012 R2 Hyper-V
 - `[实时迁移问题疑难解答] <https://docs.microsoft.com/zh-CN/troubleshoot/windows-server/virtualization/troubleshoot-live-migration-issues>`_
 - `[Live Migration via Constrained Delegation with Kerberos in Windows Server 2016] <https://techcommunity.microsoft.com/t5/virtualization/live-migration-via-constrained-delegation-with-kerberos-in/ba-p/382334>`_
 - `[为无故障转移群集的实时迁移设置主机] <https://docs.microsoft.com/zh-cn/windows-server/virtualization/hyper-v/deploy/Set-up-hosts-for-live-migration-without-Failover-Clustering>`_
 - `[解决 Windows Server 2012 Hyper-V 实时迁移时遇到的 0x80090303] <http://goxia.maytide.net/read.php/1634.htm>`_

1. 通过PS实时迁移VM
----------------------
::

	Hyper-V管理员 -- 右键目标服务器 -- Hyper-V设定 -- 实时迁移(Live Migrations)
	-- 勾选"启用传入和传出的实时迁移(E)" -- 设定并行实时迁移的数量(默认即可) 
	-- 使用任何可用的网络进行实时迁移(或选另一个并指定IP) -- 其他默认即可
	
	在目标服务器上, 新建存放VM的文件夹(不提前创建, 默认没有主机名文件夹, 造成混乱)
	
	在源服务器上, admin运行Powershell, Get-VM查看VM信息
	PS C:\Windows\system32> Move-VM 要迁移的VM_Name 目标服务器名称SERVER_Name -IncludeStorage -DestinationCredential 存放路径D:\VMS\VM_NAME
	
2. 通过PM上的Hyper-V管理员迁移
---------------------------------
::

	除了1.中的设置, 还需在"高级功能"里选择协议, 在AD管理中找到PM右键属性设置约束委派, 权限不够没测试。。。。。。
	
3. 通过SCVMM迁移
-------------------
::

	SCVMM版本太低, 管理不了Windows Server 2019.........
