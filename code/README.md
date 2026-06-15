---
tags:
  - code
  - python基础
---
> `code/` 目录说明：存放 Python 学习 notebook、语法索引和参考资料。

# code

## 文档说明

- `README.md`: 说明 `code/` 目录的文件组成和 notebook 使用方式。
- `guide.md`: 按 `pyN.ipynb` 文件整理语法点索引，便于快速查找示例所在位置。

## 文件索引

| 文件 | 内容 |
| --- | --- |
| `py1.ipynb` | 输入输出：`print()`、`input()`、f-string |
| `py2.ipynb` | 数据类型、变量、常量和基础运算 |
| `py3.ipynb` | 字符编码、`bytes`、字符串格式化 |
| `py4.ipynb` | `list`、`tuple`、索引、增删改查 |
| `py5.ipynb` | 条件判断、`match-case`、循环控制 |
| `py6.ipynb` | `dict`、`set`、集合交集和并集 |
| `py7.ipynb` | 函数定义、参数、返回值、递归 |
| `py8.ipynb` | 切片、迭代、列表推导式、生成器、迭代器 |
| `py9.ipynb` | 高阶函数、闭包、匿名函数、装饰器、偏函数 |
| `py10.ipynb` | 模块、命令行参数、内部函数、入口判断 |
| `py11.ipynb` | NumPy 数组、dtype 与形状 |
| `py12.ipynb` | NumPy 常用数组创建函数 |
| `py13.ipynb` | NumPy 切片和索引 |
| `py14.ipynb` | NumPy 数组操作（reshape/flip/连接/分割/添加删除） |
| `py15.ipynb` | NumPy 字符串操作 (np.char) |
| `py16.ipynb` | NumPy 数学、算术、统计与排序函数 |
| `py17.ipynb` | NumPy 字节交换、副本和视图 |
| `py18.ipynb` | NumPy 广播机制与迭代数组 |
| `py19.ipynb` | NumPy 矩阵库与线性代数 |
| `py20.ipynb` | NumPy IO 与 Matplotlib 基础 |
| `Python教程-廖雪峰-2025-06-16.pdf` | Python 教程参考资料 |

## 使用方式

在 VS Code 或 Jupyter Notebook 中打开对应 `.ipynb` 文件，按单元格顺序执行即可。

推荐使用项目虚拟环境作为 notebook 内核：

```powershell
.\.venv\Scripts\python.exe -m ipykernel install --user --name rosandpython-venv --display-name "Python (.venv rosandpython)"
```

然后在 notebook 右上角选择 `Python (.venv rosandpython)`。

## 注意事项

- `py1.ipynb` 包含 `input()`，运行对应代码单元时需要输入内容。
- `py5.ipynb`、`py8.ipynb`、`py9.ipynb` 输出较多，适合作为语法演示 notebook 查看。
- `py10.ipynb` 中的 `sys.argv` 示例在 notebook 环境下和命令行脚本运行略有不同。
- `py13-py20.ipynb` 为 NumPy 系列，建议按顺序学习。
