安装及配置
================

1. 虚拟环境及venv和virtualenv的区别说明
------------------------------------------
::

  #Python 2.x时，创建虚拟环境需要安装第三方的virtualenv，但Python 3.3之后，标准库里内置了venv模块，可以用来创建虚拟环境。
  1. 进入项目文件夹mypro:  cd e:\mypro
  2. 创建项目独有的虚拟环境: python3 -m venv py3   #虚拟环境的常用目录位置是 .venv
  3. 注意：需要把mypro的虚拟环境文件夹名称加入 .gitignore文件以便让Git忽略
  4. 激活虚拟环境: 
      Windows（CMD.exe）：$ mypro\Scripts\activate.bat
      Linux和macOS（bash/zsh）：$ source mypro/bin/activat
  5. 退出虚拟环境：deactivate
