---
tags:
  - readme
  - python
  - ros
  - hexapod
---
> 项目总览：记录 Python、ROS 与六足机器人开发相关的学习资料、代码目录和进度。

# rospy — Python & ROS 机器人学习笔记

## 📖 项目简介

本项目是个人学习仓库，用于记录从 **Python 基础 → ROS 核心 → 机器人算法 → 六足机器人实战** 的完整学习路径。内容涵盖理论笔记、练习代码、Jupyter 实验以及一个可运行的六足机器人最小系统。

**学习目标：**
- 掌握 Python 在机器人开发中的核心用法（OOP、装饰器、NumPy 矩阵运算）
- 理解 ROS 通信机制（话题、服务、动作、TF 坐标变换）
- 实现常用机器人算法（PID 控制、卡尔曼滤波、A\* 路径规划、正/逆运动学）
- 构建六足机器人仿真与控制系统

---

## 🛠 环境要求

| 工具/库 | 版本建议 | 用途 |
|---------|---------|------|
| Python | ≥ 3.8 | 主要编程语言 |
| NumPy | ≥ 1.21 | 矩阵运算、坐标变换 |
| SciPy | ≥ 1.7 | 科学计算、信号处理 |
| Jupyter | latest | 可视化实验 |
| Matplotlib | ≥ 3.4 | 数据绘图 |
| ROS | Noetic (Ubuntu 20.04) | 机器人框架 |

**推荐安装：**

```bash
# 基础依赖
pip install numpy scipy matplotlib jupyter

# ROS 相关（需要先安装 ROS）
sudo apt install ros-noetic-desktop-full
```

---

## 📁 项目结构

```
rospy/
├── README.md              # 项目说明 + 学习路线
├── .gitignore             # 忽略 pyc、build、devel 等
├── requirements.txt       # numpy, scipy, jupyter, rospy/rclpy 等
│
├── notes/                 # 学习笔记（个人草稿）
├── docs/                  # 正式文档（整理后可分享）
├── code/                  # 练习代码
├── notebooks/             # Jupyter（可视化/实验）
├── hexapod/               # 六足机器人最小运行环境
├── ros-ws/                # ROS 工作空间（大项目时用）
├── projects/              # 其他完整项目
└── resources/             # 速查表/资料
```

---

## 🗺 学习路线

```
阶段 1：Python 核心          阶段 2：数值计算          阶段 3：ROS 基础
┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐
│ OOP / 装饰器     │ ───► │ NumPy 矩阵运算   │ ───► │ 话题 / 服务      │
│ 生成器 / 上下文  │      │ 坐标变换 / 旋转  │      │ 动作 / TF 树     │
│ 类型提示         │      │ SciPy / 绘图     │      │ launch / 参数    │
└─────────────────┘      └─────────────────┘      └─────────────────┘
                                                          │
                                                          ▼
阶段 4：机器人算法          阶段 5：六足实战
┌─────────────────┐      ┌─────────────────┐
│ PID 控制         │      │ 步态规划         │
│ 卡尔曼滤波       │ ───► │ 逆运动学求解     │
│ A* / RRT 规划    │      │ Gazebo 仿真      │
│ 正/逆运动学      │      │ 实体部署         │
└─────────────────┘      └─────────────────┘
```

---

## 🚀 快速开始

```bash
# 1. 克隆仓库
git clone <repo-url> rospy && cd rospy

# 2. 安装依赖
pip install -r requirements.txt

# 3. 启动 Jupyter（可视化实验）
jupyter notebook notebooks/
```

---

## 📝 使用方式

| 目录           | 说明                      | 使用场景       |
| ------------ | ----------------------- | ---------- |
| `notes/`     | Markdown 学习笔记，按主题组织     | 理论学习、知识梳理  |
| `code/`      | 可运行的 Python 练习脚本        | 动手练习、算法实现  |
| `notebooks/` | Jupyter Notebook，含可视化输出 | 实验验证、数据可视化 |
| `docs/`      | 整理后的正式文档                | 查阅参考、分享交流  |
| `hexapod/`   | 六足机器人完整项目代码             | 项目开发、仿真运行  |
| `resources/` | 速查表、命令参考、论文笔记           | 快速查阅       |

## Markdown 文档格式约定

- 文档开头使用 `tags` 分类。
- `tags` 后使用引用块补充一句文档说明。
- 正文从一级标题开始，后续内容按标题层级组织。

---

## 📚 参考资料

- [ROS Wiki 官方教程](http://wiki.ros.org/ROS/Tutorials)
- [Python 官方文档](https://docs.python.org/zh-cn/3/)
- [NumPy 用户指南](https://numpy.org/doc/stable/user/index.html)
- 《Probabilistic Robotics》- Sebastian Thrun
- 《Introduction to Autonomous Mobile Robots》- Siegwart et al.

---

## 📊 学习进度

| 模块 | 状态 | 笔记 | 代码 |
|------|:----:|:----:|:----:|
| Python 核心 | 🔴 待开始 | `notes/` | `code/` |
| NumPy 数值计算 | 🔴 待开始 | `notes/` | `code/` |
| ROS 基础 | 🔴 待开始 | `notes/` | `code/` |
| 机器人算法 | 🔴 待开始 | `notes/` | `code/` |
| 六足机器人 | 🔴 待开始 | `notes/` | `hexapod/` |

> 🔴 待开始 &nbsp;&nbsp; 🟡 进行中 &nbsp;&nbsp; 🟢 已完成

---

*持续更新中...*
