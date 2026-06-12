---
tags:
  - python
  - run
---
> Python 脚本运行说明：记录 `.py` 文件在不同系统中的直接运行方式。

# Python 脚本直接运行

## Windows 说明

在 Windows 上，通常通过 Python 解释器运行 `.py` 文件：

```powershell
python hello.py
```

## macOS / Linux 说明

在 macOS 和 Linux 上，可以在 `.py` 文件第一行添加 shebang：

```python
#!/usr/bin/env python3

print('hello, world')
```

然后给文件添加执行权限：

```shell
chmod a+x hello.py
```

之后可以直接运行：

```shell
./hello.py
```
