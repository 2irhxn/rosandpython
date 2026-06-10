---
tags:
  - venv
---

# 虚拟环境搭建

创建虚拟
```shell
python -m venv .venv
```
---
激活虚拟环境

Windows
```shell
.venv\Scripts\activate
```
Linux
```shell
source .venv/bin/activate
```
---
```shell
python.exe -m pip install --upgrade pip
```
---
```shell
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
```
---
