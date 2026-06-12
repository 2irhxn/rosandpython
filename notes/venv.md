---
tags:
  - python
  - venv
---
> Python 虚拟环境笔记：记录创建、激活虚拟环境，以及升级 pip 和安装依赖的常用命令。

# 虚拟环境搭建

## 创建虚拟环境

```shell
python -m venv .venv
```

## 激活虚拟环境

Windows:

```powershell
.venv\Scripts\activate
```

Linux / macOS:

```shell
source .venv/bin/activate
```

## 升级 pip

```shell
python.exe -m pip install --upgrade pip
```

## 安装项目依赖

```shell
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
```
