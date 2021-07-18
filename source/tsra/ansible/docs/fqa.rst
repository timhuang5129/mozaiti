1. playbook执行异常
-----------------------
::

	(ansible287) [root@cos7618-dev-gui playbook]# ansible prosudo -m ping
	    192.168.23.205 | UNREACHABLE! => {
	    "changed": false,
	    "msg": "Invalid/incorrect password: Permission denied, please try again.",
	    "unreachable": true
	    }

	#其他设置正常, 原因为/etc/ansible/hosts里在群组prosudo前的群组kvm中有相同IP, 先删除即可, 不知为何, 按理说不同群组应该不会干扰. 实际原因为定义了2种ansible_password(新, 推荐)和ansible_ssh_pass(旧), 造成加载时无法覆盖.

	#https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html#intro-inventory
