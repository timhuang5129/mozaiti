FQA
=======

1. git init 与 git init --bare 的区别
---------------------------------------

 - `[git init 与 git init --bare 的区别] <https://www.cnblogs.com/langren1992/p/10161538.html>`_

2. git commit和git push的区别
--------------------------------
::

  git commit操作的是本地库，git push操作的是远程库。
  
  git commit是将本地修改过的文件提交到本地库中。
  git push是将本地库中的最新信息发送给远程库。
  
  那有人就会问，为什么要分本地commit和服务器的push呢？
  
  因为如果本地不commit的话，修改的纪录可能会丢失。
  而有些修改当前是不需要同步至服务器的，所以什么时候同步过去由用户自己选择。什么时候需要同步再push到服务器.

3. git push origin和git push -u origin master区别
---------------------------------------------------

 - `[git push origin和git push -u origin master区别] <https://blog.csdn.net/chizhang1937/article/details/100800726>`_
