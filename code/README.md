---
tags:
  - code
  - python基础
---
> `code/` 目录说明：存放 Python 基础示例脚本、脚本索引和参考资料。

# code

## 文档说明

- `README.md`: 说明 `code/` 目录的文件组成和运行方式。
- `guide.md`: 按 `pyN.py` 文件整理语法点索引，便于快速查找示例所在位置。

## 文件索引

| 文件 | 内容 |
| --- | --- |
| `py1.py` | 输入输出：`print()`、`input()`、f-string |
| `py2.py` | 数据类型、变量、常量和基础运算 |
| `py3.py` | 字符编码、`bytes`、字符串格式化 |
| `py4.py` | `list`、`tuple`、索引、增删改查 |
| `py5.py` | 条件判断、`match-case`、循环控制 |
| `py6.py` | `dict`、`set`、集合交集和并集 |
| `py7.py` | 函数定义、参数、返回值、递归 |
| `py8.py` | 切片、迭代、列表推导式、生成器、迭代器 |
| `py9.py` | 高阶函数、闭包、匿名函数、装饰器、偏函数 |
| `py10.py` | 模块、命令行参数、内部函数、入口判断 |
| `Python教程-廖雪峰-2025-06-16.pdf` | Python 教程参考资料 |

## 运行方式

在项目根目录运行示例：

```powershell
python .\code\py1.py
python .\code\py2.py
python .\code\py10.py
```

在 `code/` 目录内运行示例：

```powershell
python .\py1.py
python .\py2.py
python .\py10.py
```

## 注意事项

- `py1.py` 包含 `input()`，运行时需要在终端输入内容。
- `py5.py`、`py8.py`、`py9.py` 输出较多，适合作为语法演示脚本查看。
- `py10.py` 使用 `sys.argv`，可以额外传入命令行参数观察输出变化。
