---
tags:
  - run
---
有同学问，能不能像.exe文件那样直接运行`.py`文件呢？在Windows上是不行的，但是，在Mac和Linux上是可以的，方法是在`.py`文件的第一行加上一个特殊的注释：

```python
#!/usr/bin/env python3

print('hello, world')
```

然后，通过命令给`hello.py`以执行权限：

```shell
$ chmod a+x hello.py
```

就可以直接运行`hello.py`了，比如在Linux下运行：

```shell
$ ./hello.py
hello, world
```
---

