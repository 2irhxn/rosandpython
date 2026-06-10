# Study Guide

本文面向纯机械背景、0 编程基础的新手，目标不是把 Python 全部学完，而是建立一条能服务机器人项目的学习路线：先能读懂 Python 代码，再能用 NumPy 做运动学计算，再理解 ROS 通信机制，最后把这些能力落到六足机器人步态控制、仿真调试和代码重构中。

本学习路径不是按“编程教材目录”展开，而是按机器人项目需要推进。核心任务仍然是逐步读懂并修改六足机器人项目中的代码调用链：

```text
send.py -> gait.py -> hex.py -> leg.py / servo.py -> config.py
```

含义是：

```text
命令入口 -> 生成步态足端轨迹 -> 六条腿整机 IK -> 单腿运动学 / 舵机换算 -> 硬件参数
```

学习时不要从第一行硬看到最后一行，而要围绕“输入是什么、输出是什么、调用了谁、和机器人哪一部分对应”来读。

## 使用资料的原则

本文只推荐文字教程、官方文档和可查阅网页，不把视频教程作为主学习资料。每个链接只服务对应阶段，不需要从头到尾全部学完。

| 类型                | 推荐链接                                                   | 使用方法                                                   |
| ------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| Python 入门主线     | <https://liaoxuefeng.com/books/python/index.html>          | 建立变量、判断、循环、函数、模块、类的基本概念             |
| Python 语法速查     | <https://www.runoob.com/python3/python3-tutorial.html>     | 遇到 `list`、`dict`、`for`、`if`、`def` 等语法时快速查例子 |
| Python 官方中文文档 | <https://docs.python.org/zh-cn/3/>                         | 查标准库、语法细节、类型提示和权威说明                     |
| VS Code Python 文档 | <https://vscode.github.net.cn/docs/python/python-tutorial> | 学会在 VS Code 中运行、调试 Python 项目                    |
| PowerShell 中文文档 | <https://learn.microsoft.com/zh-cn/powershell/>            | 理解 Windows 终端、路径、命令和脚本执行                    |

不建议现在投入大量时间学习网页开发、数据库、爬虫、异步框架和大型后端工程。这些内容和当前六足机器人代码主线关系不大。

## 0. 项目基础概念

### 你需要知道的项目目录

```text
sdk/       开发版源码，包含 viewer、安全检查、日志和绘图工具
sdk_pi/    树莓派真机最小运行版，只放运行步态和发送所需文件
docs/      项目说明文档
docs/sdk_md/ 每个 sdk/*.py 文件的简短说明
ref/       参考论文、LaTeX 和资料
.venv/     当前项目的 Python 虚拟环境
requirements.txt  这个项目需要安装的第三方 Python 包
```

如果后续按照本文建议重新整理学习代码，可以新增以下目录：

```text
code/
  python-core/        Python 核心语法练习
  numpy-practice/     NumPy、矩阵和运动学练习
  ros-nodes/          ROS 节点、话题、服务、TF 练习
  algorithms/         PID、滤波、A*、IK 等算法练习

notebooks/
  transforms.ipynb    坐标变换验证
  kinematics.ipynb    正逆运动学验证

notes/
  01-python-core.md
  02-numpy.md
  03-ros-basics.md
  04-robot-algos.md
  05-hexapod-notes.md
  daily/              每日学习记录

docs/
  faq.md              遇到的问题和解决方法
  hexapod-architecture.md

hexapod/              六足机器人正式实战代码
```

### 你需要知道的机器人词汇

```text
q       公开几何关节角，单位 deg，是代码里做 FK/IK/步态时使用的角度
pwd     发给总线舵机的位置值，通常在 0..1000 之间
FK      Forward Kinematics，正运动学：已知关节角，算脚在哪里
IK      Inverse Kinematics，逆运动学：已知脚要去哪里，算关节角
pose    六条腿足端位置
frame   一帧舵机命令
gait    步态，例如 wave、ripple、tripod
dry-run 只打印命令和检查结果，不打开串口，不控制真机
execute 真正发送到硬件
```

本项目有一个重要分层原则：

```text
FK/IK 和 gait.py 只看 q
servo.py 才负责 q <-> pwd
config.py 保存硬件事实、舵机方向、默认姿态和零偏
```

如果实际舵机方向反了，不要在 `gait.py` 里随便改正负号。优先理解 `sdk/config.py` 和 `sdk/servo.py`。

---

# 阶段一：Python 核心（2 周）

## 目标

能用 Python 面向对象方式描述机器人中的基本对象，例如关节、连杆、传感器、舵机、步态配置和一帧控制命令。完成这一阶段后，应能读懂 `config.py`、`servo.py`、`send.py` 中的大部分非数学代码。

## 对应目录

```text
code/python-core/
notes/01-python-core.md
notes/daily/
```

## 1.1 运行 Python、终端和虚拟环境

### 要学什么

先学会这些概念：

```text
终端 / PowerShell
当前目录
.py 文件
Python 解释器
虚拟环境 .venv
命令行参数
```

本项目中的典型命令：

```text
python .\sdk\send.py --mode wave --stride-x 2 --lift 2.5 --frames 18 --cycles 1 --duration 0.9
```

树莓派端推荐模块方式：

```text
python3 -m sdk_pi.send --mode wave --stride-x 2 --lift 2.5 --frames 18 --cycles 1 --duration 0.9
```

两者区别：

```text
python .\sdk\send.py      直接运行某个文件
python3 -m sdk_pi.send    按 Python 包模块运行，适合 sdk_pi 这种包结构
```

不加 `--execute` 时是 dry-run，只打印和检查，不控制真机。

### 推荐教程

| 内容                | 链接                                                       | 使用方式                                               |
| ------------------- | ---------------------------------------------------------- | ------------------------------------------------------ |
| VS Code 运行 Python | <https://vscode.github.net.cn/docs/python/python-tutorial> | 看“创建 Python 文件、运行、调试、选择解释器、虚拟环境” |
| PowerShell 基础     | <https://learn.microsoft.com/zh-cn/powershell/>            | 理解 `cd`、路径、命令执行、脚本运行                    |
| Python 官方教程     | <https://docs.python.org/zh-cn/3/tutorial/>                | 查 Python 基本运行方式和语言概念                       |

### 项目小练习

```text
1. 打开 docs/USAGE.md，找到 send.py CLI 示例。
2. 找出哪些参数控制步幅、抬脚高度、帧数和每帧时间。
3. 找出哪一个参数表示真正发送到硬件。
4. 在不接真机的情况下运行 dry-run 命令。
```

## 1.2 基础语法

### 要学什么

必须掌握：

```text
变量
数字
字符串
布尔值 True / False
缩进
注释
if / else
for
while
return
```

Python 靠缩进表示代码块。例如：

```python
if execute:
    send_frames(frames)
else:
    dry_run(frames)
```

缩进去的代码属于 `if` 或 `else`。缩进错了，程序含义就变了。

### 推荐教程

| 内容               | 链接                                                   | 使用方式                                |
| ------------------ | ------------------------------------------------------ | --------------------------------------- |
| 廖雪峰 Python 教程 | <https://liaoxuefeng.com/books/python/index.html>      | 看基础语法、函数、模块和面向对象部分    |
| 菜鸟教程 Python3   | <https://www.runoob.com/python3/python3-tutorial.html> | 用来速查 `if`、`for`、`while`、函数写法 |
| Python 官方教程    | <https://docs.python.org/zh-cn/3/tutorial/>            | 查权威语法说明                          |

### 本项目里怎么看

先看 `sdk/send.py` 里的这些函数：

```text
validate_args()
_validate_gait_args()
run()
main()
```

你会看到很多判断：

```text
如果 mode 是 stand，就生成站姿帧
如果 mode 是 wave/ripple/tripod，就生成步态帧
如果 execute=False，就 dry-run
如果 execute=True，就发送到真机
```

### 项目小练习

纸面练习：

```python
execute = False

if execute:
    result = "send to hardware"
else:
    result = "dry-run only"
```

回答：最后 `result` 是什么？如果把 `execute` 改成 `True` 呢？

## 1.3 常用数据结构

### 要学什么

本项目最常见的是：

```text
list   列表，用 []，适合保存一串东西
tuple  元组，用 ()，适合保存固定长度的数据
dict   字典，用 {}，适合用名字查数据
set    集合，用 set/frozenset，适合保存不重复元素
```

### 本项目里的核心数据形状

舵机命令：

```python
ServoCmd = [[1, 500], [2, 396], [3, 271]]
```

含义：

```text
[舵机 ID, pwd 位置]
```

单腿关节角：

```python
LegQ = (0.0, 25.0, -100.0)
```

含义：

```text
(hip, thigh, calf)
```

六腿足端姿态：

```python
LegPose = {
    "lf": (4.0, 18.0, -8.0),
    "rf": (4.0, -18.0, -8.0),
}
```

含义：

```text
腿名 -> 足端坐标 (x, y, z)
```

六条腿的名字固定是：

```text
lh, lm, lf, rh, rm, rf
```

### 推荐教程

| 内容                      | 链接                                                           | 使用方式                 |
| ------------------------- | -------------------------------------------------------------- | ------------------------ |
| Python 数据结构官方教程   | <https://docs.python.org/zh-cn/3/tutorial/datastructures.html> | 重点看 list、tuple、dict |
| 菜鸟教程 Python3 数据结构 | <https://www.runoob.com/python3/python3-data-structure.html>   | 查例子，适合新手快速理解 |

### 项目小练习

手写并解释：

```python
leg_q = (0.0, 25.0, -100.0)
hip = leg_q[0]
thigh = leg_q[1]
calf = leg_q[2]
```

再手写一个简化的六腿姿态：

```python
pose = {
    "lf": (10.0, 12.0, -8.0),
    "rf": (10.0, -12.0, -8.0),
}
```

说明 `"lf"` 和 `(10.0, 12.0, -8.0)` 分别是什么。

## 1.4 函数、模块和包

### 要学什么

必须掌握：

```text
def 如何定义函数
参数
默认参数
关键字参数
返回值
函数调用函数
import
from ... import ...
包 package
__init__.py
相对导入 from .config import ...
```

简单函数例子：

```python
def add(a, b=1):
    return a + b

value = add(2, b=3)
```

`sdk/` 是一个 Python 包，因为里面有：

```text
sdk/__init__.py
```

所以可以写：

```python
from sdk import hex
```

模块内部常见：

```python
from .config import LEG_ORDER
```

这里的 `.` 表示当前包，也就是 `sdk`。

### 推荐教程

| 内容                    | 链接                                                                           | 使用方式                         |
| ----------------------- | ------------------------------------------------------------------------------ | -------------------------------- |
| Python 函数官方教程     | <https://docs.python.org/zh-cn/3/tutorial/controlflow.html#defining-functions> | 看函数定义、默认参数、关键字参数 |
| Python 模块官方教程     | <https://docs.python.org/zh-cn/3/tutorial/modules.html>                        | 看 `import`、模块、包            |
| Python 模块和包中文教程 | <https://pythonhowto.readthedocs.io/zh_CN/latest/module.html>                  | 辅助理解包结构和导入关系         |

### 本项目最重要的函数

先读这些：

```text
sdk/leg.py
  fk(q)
  ik(target)

sdk/hex.py
  stand()
  ik(pose)
  to_cmd(qs)

sdk/gait.py
  build_config(...)
  cycle(...)
  commands(...)

sdk/send.py
  gait_command_frames(...)
  dry_run(...)
  send_frames(...)
```

理解路径：

```text
gait_command_frames() 调 gait.commands()
gait.commands() 生成每一帧足端 pose
gait.pose_to_cmd() 调 hex.ik()
hex.ik() 调 leg.ik()
hex.to_cmd() 调 servo.q_to_pwd()
```

## 1.5 类、继承、dataclass 和类型提示

### 要学什么

这一部分是阶段一的重点，因为你最终要能用 Python 面向对象方式描述机器人。

必须掌握：

```text
class
对象
属性
方法
继承
dataclass
frozen=True
类型提示
```

简单例子：

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Joint:
    name: str
    servo_id: int
    direction_sign: int

joint = Joint(name="lf_hip", servo_id=7, direction_sign=-1)
```

这里 `joint.name` 是关节名，`joint.servo_id` 是舵机编号，`direction_sign` 表示舵机方向系数。

### 推荐教程

| 内容                 | 链接                                                       | 使用方式                                                           |
| -------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------ |
| Python 类官方教程    | <https://docs.python.org/zh-cn/3/tutorial/classes.html>    | 看 class、对象、继承的基本概念                                     |
| dataclasses 官方文档 | <https://docs.python.org/zh-cn/3/library/dataclasses.html> | 看 `@dataclass`、`frozen=True`                                     |
| typing 官方文档      | <https://docs.python.org/zh-cn/3/library/typing.html>      | 看 `tuple[float, float, float]`、`Mapping[str, Point3]` 等类型提示 |

### 本项目优先理解的 dataclass

在 `sdk/config.py`：

```text
ServoCalibration  总线舵机统一换算参数
ServoSpec         单个舵机的 ID、方向、零偏、关节名
LegLinks          腿部连杆长度
LegSpec           一条腿的安装事实
ArmLinks          机械臂连杆长度
```

在 `sdk/gait.py`：

```text
GaitFrame         一帧步态，包含 pose 和腿状态
TripodGaitConfig  tripod 参数
RippleGaitConfig  ripple 参数
WaveGaitConfig    wave 参数
```

在 `sdk/imu.py`：

```text
ImuSample            一帧 IMU 原始数据
OrientationEstimate  roll/pitch 估计结果
ImuFilterConfig      滤波参数
```

### 项目小练习

在 `code/python-core/` 中写一个简化版文件：

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class ServoSpec:
    servo_id: int
    joint_name: str
    direction_sign: int
    zero_offset_pwd: int = 0

lf_hip = ServoSpec(servo_id=7, joint_name="lf_hip", direction_sign=-1)
print(lf_hip)
```

然后回到 `sdk/config.py`，找真实项目里的 `ServoSpec`，比较它比这个练习多了哪些字段。

## 1.6 装饰器和多线程基础

### 要学什么

装饰器和多线程不是第一天就要精通，但在机器人软件中经常会遇到。

装饰器可以先理解为“给函数外面包一层功能”。常见用途包括日志、计时、权限检查、注册回调等。ROS 节点中虽然不一定大量手写装饰器，但你会在 Python 工程和测试工具中遇到类似写法。

多线程可以先理解为“多个任务看起来同时进行”。机器人中可能一边读 IMU，一边接收控制命令，一边发送舵机帧。但新手阶段不要急着把真机控制改成多线程，先用练习理解概念。

### 推荐教程

| 内容                      | 链接                                                           | 使用方式                             |
| ------------------------- | -------------------------------------------------------------- | ------------------------------------ |
| Python 装饰器概念         | <https://docs.python.org/zh-cn/3/glossary.html#term-decorator> | 先看官方对 decorator 的定义          |
| Python threading 官方文档 | <https://docs.python.org/zh-cn/3/library/threading.html>       | 只看线程、Lock、Thread 的基本概念    |
| 菜鸟教程多线程            | <https://www.runoob.com/python3/python3-multithreading.html>   | 用简单例子理解，不直接照搬到真机控制 |

### 项目小练习

```text
1. 写一个装饰器，打印函数开始和结束。
2. 写两个线程，一个每 0.5 秒打印 IMU，一个每 1 秒打印 servo。
3. 明确说明：这只是练习，不直接用于真机发送层。
```

## 1.7 错误处理和安全检查

### 要学什么

必须掌握：

```text
raise
ValueError
TypeError
try / except
输入校验
```

机器人项目和普通小程序不同，错误参数可能导致真机动作危险。所以这个项目有很多“先检查，不对就报错”的代码。

### 推荐教程

| 内容                      | 链接                                                      | 使用方式                            |
| ------------------------- | --------------------------------------------------------- | ----------------------------------- |
| Python 错误和异常官方教程 | <https://docs.python.org/zh-cn/3/tutorial/errors.html>    | 看 `try/except`、`raise`、异常类型  |
| Python 内置异常           | <https://docs.python.org/zh-cn/3/library/exceptions.html> | 查 `ValueError`、`TypeError` 等含义 |

### 本项目重点看

`sdk/servo.py`：

```text
_validate_pwd()
_validate_servo_id()
_validate_angle()
q_to_pwd()
pwd_to_q()
```

`sdk/send.py`：

```text
validate_command()
validate_frames()
find_speed_violations()
validate_frame_speeds()
_validate_duration()
```

`sdk/leg.py`：

```text
ik()
_is_planar_reach_possible()
```

### 安全逻辑

```text
1. pwd 必须在 0..1000。
2. 舵机 ID 必须是支持的 ID。
3. 一帧命令必须包含合法的腿部舵机命令。
4. 相邻帧之间不能让同一个舵机运动太快。
5. IK 不可达时不能硬算一个假结果。
```

---

# 阶段二：NumPy 与机器人数学（3 周）

## 目标

能用矩阵做运动学和轨迹计算。完成这一阶段后，应能在 notebook 中验证坐标变换、齐次变换、正逆运动学和多项式轨迹插值，再把验证过的算法移植到正式代码中。

## 对应目录

```text
code/numpy-practice/
notebooks/transforms.ipynb
notebooks/kinematics.ipynb
notes/02-numpy.md
```

## 2.1 NumPy 基础：向量和矩阵

### 要学什么

```text
array
向量
矩阵
矩阵乘法 @
转置
求逆
范数
广播
```

### 推荐教程

| 内容           | 链接                                                        | 使用方式                   |
| -------------- | ----------------------------------------------------------- | -------------------------- |
| NumPy 官方入门 | <https://numpy.org/doc/stable/user/absolute_beginners.html> | 学 `array`、矩阵运算、索引 |
| NumPy 中文文档 | <https://www.numpy.org.cn/>                                 | 中文速查 NumPy 常用函数    |
| 菜鸟教程 NumPy | <https://www.runoob.com/numpy/numpy-tutorial.html>          | 新手查例子                 |

### 项目小练习

在 `notebooks/transforms.ipynb` 中写：

```python
import numpy as np

p = np.array([1.0, 2.0, 3.0])
R = np.eye(3)
t = np.array([10.0, 0.0, 0.0])

p_new = R @ p + t
print(p_new)
```

说明：这是最基本的“旋转 + 平移”。

## 2.2 齐次变换矩阵

### 要学什么

```text
旋转矩阵
平移向量
齐次坐标
4x4 齐次变换矩阵
坐标系连乘
```

机器人运动学中，经常把点写成：

```text
[x, y, z, 1]
```

再用 4x4 矩阵表示旋转和平移。这样多级连杆、机体坐标、腿局部坐标之间的关系可以统一计算。

### 推荐教程

| 内容                             | 链接                                                         | 使用方式                                   |
| -------------------------------- | ------------------------------------------------------------ | ------------------------------------------ |
| Robotics Toolbox for Python 文档 | <https://petercorke.github.io/robotics-toolbox-python/>      | 后续查机器人运动学工具，不作为第一学习入口 |
| SpatialMath for Python 文档      | <https://bdaiinstitute.github.io/spatialmath-python/>        | 查 SE3、SO3、旋转和平移表达                |
| Modern Robotics 在线资料         | <https://modernrobotics.northwestern.edu/chapters/chapter3/> | 看刚体运动、旋转、齐次变换概念             |

### 项目对应

这个阶段对应：

```text
sdk/hex.py
  local_to_body()
  body_to_local()

sdk/leg.py
  fk(q)
  ik(target)
```

先用 notebook 验证坐标变换，再回到正式代码中看 `hex.py` 如何把单腿 local 坐标转到 body 坐标。

## 2.3 正逆运动学数值计算

### 要学什么

```text
FK：已知关节角，算末端位置
IK：已知末端位置，算关节角
雅可比矩阵
数值迭代思想
几何法和数值法的区别
```

对六足项目来说，先理解单腿 3 自由度几何 IK，再理解整机六条腿如何分别求 IK。

### 推荐教程

| 内容                      | 链接                                                         | 使用方式                                                   |
| ------------------------- | ------------------------------------------------------------ | ---------------------------------------------------------- |
| Modern Robotics Chapter 4 | <https://modernrobotics.northwestern.edu/chapters/chapter4/> | 正运动学基础                                               |
| Modern Robotics Chapter 6 | <https://modernrobotics.northwestern.edu/chapters/chapter6/> | 逆运动学基础                                               |
| PythonRobotics            | <https://atsushisakai.github.io/PythonRobotics/>             | 查机器人算法的 Python 示例，重点看路径规划和运动学相关代码 |

### 项目小练习

在 `notebooks/kinematics.ipynb` 中做两件事：

```text
1. 输入一组三关节角，画出单腿三个连杆的大致位置。
2. 输入足端目标点，调用你自己写的简化 IK，输出 hip/thigh/calf。
```

暂时不要求完全复现真项目，只要理解输入输出。

## 2.4 多项式轨迹插值

### 要学什么

```text
三次 smoothstep
五次 smootherstep
轨迹位置连续
速度连续
加速度连续
摆动相和支撑相
```

本项目里你已经见过：

```python
def _smoothstep(progress: float) -> float:
    progress = _clamp01(progress)
    return progress * progress * (3.0 - 2.0 * progress)
```

三次 smoothstep 可以让起点和终点速度更平滑。后续可以考虑五次 smootherstep：

```python
def _smootherstep(progress: float) -> float:
    progress = _clamp01(progress)
    return progress * progress * progress * (progress * (progress * 6.0 - 15.0) + 10.0)
```

### 推荐教程

| 内容             | 链接                                                               | 使用方式                 |
| ---------------- | ------------------------------------------------------------------ | ------------------------ |
| NumPy 多项式工具 | <https://numpy.org/doc/stable/reference/routines.polynomials.html> | 查多项式相关函数         |
| SciPy 插值文档   | <https://docs.scipy.org/doc/scipy/tutorial/interpolate.html>       | 后续需要更复杂插值时再看 |

### 项目对应

这个阶段对应：

```text
sdk/gait.py
  _smoothstep()
  swing trajectory
  support trajectory
```

你要能说明：

```text
1. 三次函数不是控制“整机步态类型”，而是让单腿摆动过程更平滑。
2. 改为五次多项式后，起落脚速度和加速度更柔和，但不一定直接解决走偏。
3. 走偏还要看坐标系、舵机方向、支撑相、地面摩擦和 IMU/yaw 补偿。
```

---

# 阶段三：ROS 通信机制（3 周）

## 目标

写出完整的 ROS 节点，理解节点之间如何通过话题、服务、动作和 TF 协同工作。完成这一阶段后，应能看懂机器人驱动、传感器、导航和控制模块之间的信息流。

## 对应目录

```text
code/ros-nodes/
notes/03-ros-basics.md
```

## 3.1 ROS 版本说明

你的机器人项目可能同时涉及 ROS1 和 ROS2。多机器人导航项目使用 ROS1 Melodic；RealMan ECO65 机械臂当前更接近 ROS2 驱动环境；六足项目当前主要是 Python SDK 控制，不一定一开始就接 ROS。

因此学习 ROS 时要分清：

```text
ROS1：roscore、rostopic、rosservice、catkin、launch XML
ROS2：ros2 topic、ros2 service、ros2 action、colcon、launch.py
```

不要把 ROS1 和 ROS2 的命令混用。

### 推荐教程

| 内容                    | 链接                                             | 使用方式                         |
| ----------------------- | ------------------------------------------------ | -------------------------------- |
| ROS1 官方中文教程       | <http://wiki.ros.org/cn/ROS/Tutorials>           | 学 ROS1 节点、话题、服务、TF     |
| ROS2 官方文档           | <https://docs.ros.org/en/rolling/Tutorials.html> | 学 ROS2 概念和命令，注意版本差异 |
| 古月居 ROS 入门文字资料 | <https://www.guyuehome.com/>                     | 作为中文辅助资料，优先看文字文章 |

## 3.2 话题发布与订阅

### 要学什么

```text
node
publisher
subscriber
topic
message
queue
rate
callback
```

机器人里常见的话题：

```text
/cmd_vel       速度命令
/odom          里程计
/scan          激光雷达
/imu           惯性测量
/joint_states  关节状态
/tf            坐标变换
```

### 项目小练习

在 `code/ros-nodes/` 中写最小发布/订阅节点：

```text
1. 一个节点发布模拟速度命令。
2. 一个节点订阅速度命令并打印。
3. 记录发布频率和回调函数的执行顺序。
```

## 3.3 服务、客户端和动作服务

### 要学什么

```text
service：一次请求，一次响应
action：适合长时间任务，可反馈进度，可取消
client：发起请求的一方
server：处理请求的一方
```

机器人中常见用法：

```text
服务：查询状态、设置参数、触发一次标定
动作：导航到目标点、机械臂运动到目标姿态
```

### 推荐教程

| 内容             | 链接                                                                                             | 使用方式                  |
| ---------------- | ------------------------------------------------------------------------------------------------ | ------------------------- |
| ROS1 服务教程    | <http://wiki.ros.org/ROS/Tutorials/WritingServiceClient%28python%29>                             | 看 Python 服务/客户端写法 |
| ROS2 Action 教程 | <https://docs.ros.org/en/rolling/Tutorials/Intermediate/Writing-an-Action-Server-Client/Py.html> | 看动作服务基本结构        |

## 3.4 TF 坐标变换

### 要学什么

```text
坐标系
父子坐标系
base_link
odom
map
static transform
dynamic transform
TF tree
```

六足和机械臂都会大量使用坐标变换。机械臂中是各连杆坐标系；移动机器人中是 `map -> odom -> base_link -> sensor`；六足中可以理解为 `body -> leg_local -> foot`。

### 推荐教程

| 内容          | 链接                                                                       | 使用方式         |
| ------------- | -------------------------------------------------------------------------- | ---------------- |
| ROS TF 教程   | <http://wiki.ros.org/tf/Tutorials>                                         | 学 ROS1 TF 基础  |
| ROS2 tf2 教程 | <https://docs.ros.org/en/rolling/Tutorials/Intermediate/Tf2/Tf2-Main.html> | 学 ROS2 tf2 基础 |

---

# 阶段四：机器人算法（4 周）

## 目标

实现常用控制与感知算法。完成这一阶段后，应能独立写出简化版 PID、卡尔曼滤波、A* 路径规划和逆运动学求解器，并知道这些算法在机器人项目中的位置。

## 对应目录

```text
code/algorithms/
notes/04-robot-algos.md
```

## 4.1 PID 控制器

### 要学什么

```text
比例 P
积分 I
微分 D
误差 error
目标值 target
当前值 current
控制输出 output
饱和限制
积分限幅
```

PID 在机器人中常用于速度控制、位置控制、姿态控制和 yaw 纠偏。六足项目中，后续可以用一个简化 P 或 PID 对 yaw 偏差进行修正。

### 推荐教程

| 内容                    | 链接                                                                                       | 使用方式                           |
| ----------------------- | ------------------------------------------------------------------------------------------ | ---------------------------------- |
| PythonRobotics 控制示例 | <https://atsushisakai.github.io/PythonRobotics/modules/6_path_tracking/path_tracking.html> | 看路径跟踪和控制算法示例           |
| PID 控制概念            | <https://en.wikipedia.org/wiki/PID_controller>                                             | 查基本概念，中文可配合其他资料理解 |

### 项目小练习

写一个简化 PID：

```python
class PID:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.integral = 0.0
        self.prev_error = 0.0

    def step(self, target, current, dt):
        error = target - current
        self.integral += error * dt
        derivative = (error - self.prev_error) / dt if dt > 0 else 0.0
        self.prev_error = error
        return self.kp * error + self.ki * self.integral + self.kd * derivative
```

然后说明它可以怎样用于 yaw 纠偏。

## 4.2 卡尔曼滤波

### 要学什么

```text
状态估计
预测
更新
观测噪声
过程噪声
IMU 数据
互补滤波和卡尔曼滤波区别
```

对你当前阶段来说，不需要一开始就推完整卡尔曼公式。先知道它解决的问题：传感器数据有噪声，需要用模型和观测融合得到更稳定的状态估计。

### 推荐教程

| 内容                         | 链接                                                                                                    | 使用方式                   |
| ---------------------------- | ------------------------------------------------------------------------------------------------------- | -------------------------- |
| FilterPy 文档                | <https://filterpy.readthedocs.io/>                                                                      | 用 Python 学卡尔曼滤波实现 |
| PythonRobotics Kalman Filter | <https://atsushisakai.github.io/PythonRobotics/modules/2_localization/kalman_filter/kalman_filter.html> | 看定位中的卡尔曼滤波示例   |

### 项目对应

```text
sdk/imu.py
sdk/imu_check.py
sdk/stabilizer.py
```

先理解 roll/pitch 怎么由 IMU 估计，再考虑更复杂滤波。

## 4.3 A* 路径规划

### 要学什么

```text
栅格地图
起点和终点
障碍物
代价
启发函数
open set
closed set
路径回溯
```

A* 主要对应移动机器人导航项目，不是六足舵机底层控制。但它能帮助你理解多机器人路径规划和导航论文中的算法部分。

### 推荐教程

| 内容              | 链接                                                                                                           | 使用方式                       |
| ----------------- | -------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| PythonRobotics A* | <https://atsushisakai.github.io/PythonRobotics/modules/5_path_planning/grid_base_search/grid_base_search.html> | 看 A*、Dijkstra 等栅格搜索示例 |

## 4.4 逆运动学求解器

### 要学什么

```text
几何 IK
数值 IK
雅可比迭代
可达性判断
关节范围约束
```

六足项目当前优先使用几何 IK，因为单腿自由度少，结构明确，计算快。机械臂项目中后续可能更多使用矩阵法、D-H、MDH、雅可比和数值优化。

### 推荐教程

| 内容                        | 链接                                                         | 使用方式                   |
| --------------------------- | ------------------------------------------------------------ | -------------------------- |
| Modern Robotics IK          | <https://modernrobotics.northwestern.edu/chapters/chapter6/> | 逆运动学理论               |
| Robotics Toolbox for Python | <https://petercorke.github.io/robotics-toolbox-python/>      | 后续做机械臂建模和 IK 验证 |

---

# 阶段五：六足机器人实战（持续）

## 目标

让六足机器人从 dry-run、仿真、轨迹预览逐步走到真机低速测试。完成这一阶段后，应能解释完整控制链路，能定位步态走偏、舵机方向错误、IK 不可达、速度过快、支撑不稳定等问题。

## 对应目录

```text
hexapod/
notes/05-hexapod-notes.md
docs/hexapod-architecture.md
docs/faq.md
```

## 5.1 先读硬件事实

文件：

```text
sdk/config.py
docs/HARDWARE.md
```

重点：

```text
LEG_ORDER
LEG_LINKS
STAND_Q
GAIT_STANCE_Q
LEG_SPECS
SERVO_SPECS
SERVO_ZERO_OFFSETS_PWD
```

读完要能回答：

```text
1. 六条腿的名字是什么？
2. 每条腿有哪三个关节？
3. 每条腿对应哪些舵机 ID？
4. 默认站姿 q 是多少？
5. direction_sign 和 zero_offset_pwd 分别解决什么问题？
```

## 5.2 读 q 和 pwd 的转换

文件：

```text
sdk/servo.py
docs/sdk_md/servo.md
```

重点：

```text
pwd_to_q()
q_to_pwd()
calibrated_center()
to_cmd()
```

读完要能回答：

```text
1. q 是什么？
2. pwd 是什么？
3. 为什么 q -> pwd 只应该集中在 servo.py？
4. 为什么命令最后要按 servo id 排序？
```

## 5.3 读单腿 FK/IK

文件：

```text
sdk/leg.py
docs/sdk_md/leg.md
```

重点：

```text
fk(q)
ik(target)
_horizontal_direction()
_project_link()
```

读完要能回答：

```text
1. q_hip=0 时腿朝哪个方向？
2. FK 的输入和输出分别是什么？
3. IK 的输入和输出分别是什么？
4. 为什么 target_z >= 0 时 IK 返回 None？
```

## 5.4 读六足整机

文件：

```text
sdk/hex.py
docs/sdk_md/hex.md
```

重点：

```text
stand()
stand_qs()
local_to_body()
body_to_local()
ik()
to_cmd()
```

读完要能回答：

```text
1. 单腿 local 坐标怎样转到 body 坐标？
2. 六条腿的 IK 为什么可能整体返回 None？
3. hex.to_cmd() 为什么还会经过 servo.py？
```

## 5.5 读离散步态

文件：

```text
sdk/gait.py
docs/sdk_md/gait.md
docs/USAGE.md
```

重点：

```text
available_gaits()
build_config()
pose_with_states()
cycle_with_states()
commands()
pose_to_cmd()
```

读完要能回答：

```text
1. wave、ripple、tripod 的区别是什么？
2. swing 和 support 分别是什么？
3. stride_x、stride_y、yaw_stride、lift 分别控制什么？
4. gait.py 生成的是脚端目标，还是直接生成串口字节？
```

## 5.6 读发送入口

文件：

```text
sdk/send.py
docs/sdk_md/send.md
docs/OPERATIONS.md
```

重点：

```text
stand_command_frames()
gait_command_frames()
repeat_frames()
validate_frames()
validate_frame_speeds()
dry_run()
send_frames()
build_parser()
run()
```

读完要能回答：

```text
1. dry-run 走到哪里停止？
2. execute=True 后才多走了哪些步骤？
3. 真机发送前做了哪些检查？
4. 为什么普通步态脚本不应该绕过 send.py？
```

## 5.7 URDF 建模、仿真与调试

### 要学什么

```text
URDF link / joint
坐标系
惯性参数
碰撞模型
可视化模型
Gazebo / RViz
```

这部分和 ROS、TF、机器人建模联系紧密。六足实战中，URDF 主要用于仿真、可视化和调试，不直接替代 `gait.py`、`leg.py`、`servo.py`。

### 推荐教程

| 内容          | 链接                                      | 使用方式                                  |
| ------------- | ----------------------------------------- | ----------------------------------------- |
| ROS URDF 教程 | <http://wiki.ros.org/urdf/Tutorials>      | 学 link、joint、robot_description         |
| Gazebo 教程   | <https://classic.gazebosim.org/tutorials> | 如使用 Gazebo Classic，可查模型和仿真基础 |
| RViz 用户指南 | <http://wiki.ros.org/rviz/UserGuide>      | 学模型显示、TF、坐标系检查                |

## 5.8 步态控制器升级方向

后续不是只写：

```python
gait("wave", ...)
gait("ripple", ...)
gait("tripod", ...)
```

而是逐步升级为：

```python
controller.set_motion(vx=3.0, vy=0.0, yaw_rate=0.0)
controller.request_gait("wave")

while True:
    controller.step(dt)
```

升级方向：

```text
1. 保留 gait_control.py 做单步态测试。
2. 建立 gait_profiles.py，把 wave/ripple/tripod 表示为 phase_offsets + swing_fraction。
3. 新建 transition_manager.py，实现普通参数平滑和 phase_offset 圆周插值。
4. 新建 support_checker.py，判断支撑腿数量、支撑多边形和稳定裕度。
5. 新建 servo_safety.py，统一检查舵机角度范围和速度。
6. 后续加入 IMU yaw 纠偏、roll/pitch 足端高度补偿和机械臂 COM 前馈。
```

---

# 每日学习记录与项目归档方式

每阶段开始时，在 `notes/daily/` 做学习记录。建议格式：

```markdown
# 2026-xx-xx 学习记录

## 今天看的内容

## 今天写的代码

## 今天遇到的问题

## 解决方法

## 明天继续做什么
```

遇到坑统一整理到：

```text
docs/faq.md
```

算法验证统一放到：

```text
notebooks/
```

正式代码归档到对应目录：

```text
code/python-core/
code/numpy-practice/
code/ros-nodes/
code/algorithms/
hexapod/
```

这样区分“学习验证代码”和“正式项目代码”，避免把临时实验文件混进真机控制代码。

---

# 最小验收标准

当你能清楚回答下面问题，说明已经能开始真正读懂本项目：

```text
1. sdk/ 和 sdk_pi/ 的区别是什么？
2. q 和 pwd 的区别是什么？
3. LegQ、LegPose、ServoCmd 分别长什么样？
4. FK 和 IK 分别解决什么问题？
5. wave、ripple、tripod 大概有什么区别？
6. send.py 的 dry-run 和 execute=True 有什么区别？
7. 一条 wave 命令大概会经过哪些模块？
8. 为什么舵机速度检查必须在真机发送前执行？
9. config.py、servo.py、gait.py 各自不能随便混进什么职责？
10. 如果要查某个舵机 ID、方向或零偏，应该去哪里？
```

建议把这些问题写在 `notes/05-hexapod-notes.md` 的开头。每读完一个阶段，就回头用自己的话回答一次。
