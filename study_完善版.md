---
tags:
  - study
  - python
  - hexapod
---
> 精简学习指南：围绕六足机器人项目代码调用链，整理新手需要优先掌握的 Python 知识和源码阅读顺序。

# 六足机器人 Python 学习指南

本文面向纯机械背景、0 编程基础的新手，目标不是把 Python 全部学完，而是先学会“读懂并逐步修改这个六足机器人项目所需的 Python”。读这个项目时，最重要的是先理解代码怎样把“想让机器人走一步”一步步变成“18 个腿部舵机的命令”。

项目核心调用链可以先记住这一条：

```text
send.py -> gait.py -> hex.py -> leg.py / servo.py -> config.py
```

含义是：

```text
命令入口 -> 生成步态足端轨迹 -> 六条腿整机 IK -> 单腿运动学 / 舵机换算 -> 硬件参数
```

学习时不要一开始就试图从第一行代码看到最后一行。先学 Python 必备语法，再顺着这条调用链看。

## 0. 先建立几个概念

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

新手主要先读：

```text
README.md
docs/HARDWARE.md
docs/API.md
docs/USAGE.md
docs/OPERATIONS.md
study.md
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

## 1. Python 第一阶段：会运行 Python

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

你不需要一开始就懂所有命令，只需要知道“命令是在某个目录下运行某个 Python 文件”。

### 本项目里的例子

开发机直接运行脚本：

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

### 要能回答的问题

```text
1. 当前终端在哪个文件夹？
2. .py 文件是什么？
3. python xxx.py 和 python -m xxx 有什么直观区别？
4. 为什么不加 --execute 就不会控制真机？
```

### 小练习

只做阅读练习，不接真机：

```text
1. 打开 docs/USAGE.md，找到 send.py CLI 示例。
2. 找出哪些参数控制步幅、抬脚高度、帧数和每帧时间。
3. 找出哪一个参数表示真正发送到硬件。
```

## 2. Python 第二阶段：基础语法

### 要学什么

必须先学会：

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

### 要能回答的问题

```text
1. if/else 是怎么让程序走不同路径的？
2. return 是怎么把结果交给调用者的？
3. True/False 在 execute 这种开关参数里是什么意思？
4. 为什么参数不合法时程序要提前报错？
```

### 小练习

纸面练习：

```python
execute = False

if execute:
    result = "send to hardware"
else:
    result = "dry-run only"
```

回答：最后 `result` 是什么？如果把 `execute` 改成 `True` 呢？

## 3. Python 第三阶段：常用数据结构

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

可以按身体位置理解：

```text
lh rear left
lm middle left
lf front left
rh rear right
rm middle right
rf front right
```

### 本项目里怎么看

先看：

```text
sdk/robot_types.py
sdk/config.py
sdk/hex.py
```

重点找这些名字：

```text
ServoCmd
LegQ
LegPose
LEG_ORDER
LEG_SERVO_IDS
LEG_SPECS
```

### 要能回答的问题

```text
1. 为什么 LegQ 用 tuple，而不是一个普通数字？
2. 为什么 LegPose 用 dict？
3. ServoCmd 里的每个小列表为什么是 [id, pwd]？
4. 六条腿的名字为什么不能随便写？
```

### 小练习

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

## 4. Python 第四阶段：函数

### 要学什么

必须掌握：

```text
def 如何定义函数
参数
默认参数
关键字参数
返回值
函数调用函数
```

例子：

```python
def add(a, b=1):
    return a + b

value = add(2, b=3)
```

这里：

```text
a 是参数
b=1 是默认参数
b=3 是关键字参数
return 把结果返回
```

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

### 要能回答的问题

```text
1. 一个函数从哪里拿输入？
2. 一个函数把结果 return 给了谁？
3. 默认参数有什么用？
4. 为什么高层函数不直接写所有细节，而是继续调用别的函数？
```

### 小练习

用纸面追踪：

```text
send.gait_command_frames("wave", frames=18)
```

依次写出它大概会经过哪些模块：

```text
send.py
gait.py
hex.py
leg.py
servo.py
config.py
```

不用看懂每一行数学，只要先能看懂“谁调用谁”。

## 5. Python 第五阶段：模块和包

### 要学什么

必须掌握：

```text
import
from ... import ...
包 package
__init__.py
相对导入 from .config import ...
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

### 本项目里的导入兼容

有些文件里会看到：

```python
try:
    from .config import ...
except ImportError:
    ...
```

这是为了让同一个文件既能作为包模块运行，也能被直接当脚本运行。新手第一次读时不需要完全掌握 `sys.path` 和 `importlib`，只要知道这是“导入兼容代码”。

### 要能回答的问题

```text
1. sdk/ 为什么能被 import？
2. from sdk import hex 是什么意思？
3. from .config import SERVO_SPECS 是什么意思？
4. 为什么运行方式不同会影响 import？
```

### 小练习

在纸上画出模块关系：

```text
send.py imports gait.py, hex.py, servo_feedback.py, stabilizer.py
gait.py imports hex.py and config.py
hex.py imports leg.py, servo.py and config.py
servo.py imports config.py
leg.py imports config.py
```

然后回答：如果要查舵机 ID，应该去哪个文件？

## 6. Python 第六阶段：类、dataclass 和类型提示

### 要学什么

这个项目里有类，但新手不要一开始学复杂面向对象。先把很多类理解成“有名字的数据盒子”。

必须掌握：

```text
class
对象
属性
dataclass
frozen=True
类型提示
```

简单例子：

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: float
    y: float

p = Point(1.0, 2.0)
```

这里 `p.x` 是 `1.0`，`p.y` 是 `2.0`。

`frozen=True` 表示创建后尽量不要修改，适合保存配置和硬件事实。

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

在 `sdk/gait_controller.py`：

```text
MotionCommand        连续运动命令
GaitControllerFrame  连续控制器输出的一帧结果
```

在 `sdk/imu.py`：

```text
ImuSample            一帧 IMU 原始数据
OrientationEstimate  roll/pitch 估计结果
ImuFilterConfig      滤波参数
```

### 类型提示怎么读

常见类型提示：

```python
tuple[float, float, float]
```

意思是：

```text
三个 float 组成的 tuple
```

例如：

```text
(x, y, z)
(hip, thigh, calf)
```

再看：

```python
Mapping[str, Point3]
```

意思是：

```text
key 是 str，value 是 Point3 的映射
```

也就是类似：

```python
{"lf": (x, y, z), "rf": (x, y, z)}
```

再看：

```python
ServoCmd
```

这是项目自己定义的类型别名，去 `sdk/robot_types.py` 查。

### 要能回答的问题

```text
1. dataclass 为什么适合保存硬件参数？
2. ServoSpec 里 direction_sign 是什么？
3. LegSpec 里 hip_origin_body 和 mount_alpha_deg 是什么？
4. GaitFrame 为什么既要保存 pose，也要保存 leg_states？
```

### 小练习

打开 `sdk/config.py`，找到：

```text
class ServoSpec
class LegSpec
SERVO_SPECS
LEG_SPECS
```

回答：

```text
1. 7 号舵机属于哪条腿的哪个关节？
2. lf 的 hip_origin_body 是什么？
3. 左腿和右腿的 thigh direction_sign 是否一样？
```

## 7. Python 第七阶段：错误处理和安全检查

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

### 你要理解的安全逻辑

```text
1. pwd 必须在 0..1000。
2. 舵机 ID 必须是支持的 ID。
3. 一帧命令必须包含合法的腿部舵机命令。
4. 相邻帧之间不能让同一个舵机运动太快。
5. IK 不可达时不能硬算一个假结果。
```

dry-run 可能打印 WARNING；真机执行前速度风险会阻断。

### 要能回答的问题

```text
1. 为什么 _validate_pwd() 要检查 pwd 范围？
2. 为什么 IK 不可达时返回 None？
3. 为什么 send_frames() 打开串口前要先 validate_frame_speeds()？
4. 为什么新手不应该绕过 send.py 直接调用底层 Board？
```

### 小练习

纸面判断：

```text
pwd = 1200 是否合法？
duration = 0 是否合法？
target_z = 5 的单腿 IK 是否应该接受？
```

再去对应函数里找代码验证你的判断。

## 8. Python 第八阶段：项目会用到的标准库

### 必须学

`math`：

```text
三角函数、角度和弧度转换、hypot、sin、cos、atan2
对应文件：sdk/leg.py、sdk/hex.py、sdk/gait.py、sdk/cpg_phase.py
```

`argparse`：

```text
命令行参数解析
对应文件：sdk/send.py、sdk/cpg_control.py、sdk/imu_check.py
```

`dataclasses`：

```text
数据类
对应文件：sdk/config.py、sdk/gait.py、sdk/gait_controller.py、sdk/imu.py
```

`typing`：

```text
类型提示，提高读代码效率
对应文件：sdk/robot_types.py 和多数 sdk/*.py
```

`pathlib`、`sys`、`importlib`：

```text
处理路径和导入兼容
对应文件：多个可直接运行的 sdk/*.py
```

### 暂时不用学

为了看懂这个项目，先不要花时间学：

```text
网络编程
数据库
网页开发
异步 async/await
多线程
爬虫
大型后端框架
```

这些不是当前项目主线。

## 9. Python 学完后的源码阅读顺序

### 第一步：读硬件事实

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

### 第二步：读 q 和 pwd 的转换

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

### 第三步：读单腿 FK/IK

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

### 第四步：读六足整机

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

### 第五步：读离散步态

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

### 第六步：读发送入口

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

### 第七步：读高层动作封装

文件：

```text
sdk/gait_control.py
docs/sdk_md/gait_control.md
```

重点：

```text
gait()
gait_sequence()
```

读完要能回答：

```text
1. 为什么 gait_control.py 不重新实现 gait 算法？
2. 单段动作和多段动作怎么组织？
3. execute=False 默认值为什么重要？
```

### 第八步：读连续控制和 CPG

文件：

```text
sdk/gait_profiles.py
sdk/gait_controller.py
sdk/cpg_phase.py
sdk/cpg_control.py
docs/ROADMAP.md
```

重点：

```text
GaitProfile
MotionCommand
GaitController
GaitControllerFrame
CpgPhaseNetwork
cpg_transition()
```

读完要能回答：

```text
1. 离散步态和连续控制有什么区别？
2. safe 和 cpg 两种 transition_mode 有什么区别？
3. CPG 在本项目里只负责什么？
4. CPG 是否替代 IK、servo.py 或 send.py？
```

### 第九步：读 IMU、稳定性和工具

文件：

```text
sdk/imu.py
sdk/imu_check.py
sdk/stabilizer.py
sdk/com.py
sdk/safety_margin.py
sdk/servo_trajectory_viewer.py
sdk/experiment_logger.py
sdk/plot_paper_figures.py
```

重点：

```text
IMU 当前是只读估计，不是真实闭环控制
stabilizer 当前主要是模拟 roll/pitch 补偿
com.py 是离线稳定裕度分析
viewer 是开发版预览和日志工具
绘图工具只读日志，不控制硬件
```

读完要能回答：

```text
1. imu_check.py 是否会控制舵机？
2. send.py --stabilize 是否是真实 IMU 闭环？
3. viewer 保存的日志是真实舵机回读吗？
4. safety_margin.py 是分析工具还是发送工具？
```

## 10. 建议学习节奏

### 第 1 周：只补 Python 基础

目标：

```text
能看懂变量、if、for、函数、list/tuple/dict
能看懂简单的 import
能知道 .py 文件和命令行参数是什么
```

不要急着读 CPG、IMU、viewer。

### 第 2 周：读核心数据结构和硬件参数

目标：

```text
读懂 sdk/robot_types.py
读懂 sdk/config.py 的大部分常量
读懂 q、pwd、LegQ、LegPose、ServoCmd
```

重点是把“代码里的数据”对应到“机械结构里的腿、关节、舵机”。

### 第 3 周：读运动学主线

目标：

```text
读懂 sdk/servo.py
大致读懂 sdk/leg.py 的 FK/IK
读懂 sdk/hex.py 如何把六条腿组织起来
```

数学细节可以慢一点，但函数输入输出必须先搞清楚。

### 第 4 周：读步态和发送

目标：

```text
读懂 gait.py 如何生成 pose / command
读懂 send.py 如何 dry-run、检查速度和发送
能从一个 CLI 示例追踪到核心调用链
```

这周结束后，应该能完整解释：

```text
python .\sdk\send.py --mode wave --stride-x 2 --lift 2.5 ...
```

大概经过哪些函数。

### 第 5 周以后：读进阶模块

目标：

```text
连续控制 gait_controller.py
CPG cpg_phase.py / cpg_control.py
IMU imu.py / imu_check.py
稳定性 com.py / safety_margin.py
viewer 和日志绘图工具
```

这些模块不是入门第一优先级。

## 11. 每读一个文件都按这个方法

不要从第一行开始硬啃。按下面顺序：

```text
1. 先读文件顶部 docstring，看它负责什么。
2. 再看 import，知道它依赖哪些模块。
3. 找 dataclass 和常量，知道它处理什么数据。
4. 找公开函数，也就是不以下划线开头的函数。
5. 找 main/run/build_parser，判断它是不是命令行入口。
6. 最后再读以下划线开头的内部 helper。
```

做阅读笔记时，每个函数只先记四件事：

```text
函数名
输入
输出
它调用了谁
```

例如：

```text
send.gait_command_frames()
输入：gait 名称、帧数、步态配置
输出：list[ServoCmd]
调用：gait.commands()
```

## 12. 新手最容易犯的误区

### 误区 1：把 q 当成 pwd

`q` 是几何关节角，单位是度。`pwd` 是舵机位置值。

```text
q   用在 FK/IK/gait/viewer
pwd 用在真实舵机命令
```

两者只通过 `servo.py` 转换。

### 误区 2：一看到方向反了就改 gait.py

步态方向、几何安装、舵机响应方向是分层的：

```text
hip_origin_body/mount_alpha_deg  描述几何安装
direction_sign                  描述舵机脉宽响应方向
gait.py                         描述足端轨迹
```

不要把硬件方向问题随便塞进步态算法。

### 误区 3：以为 dry-run 会动真机

不加 `--execute` 时，只打印和检查，不打开串口。

真机相关命令必须先 dry-run，再在安全条件下加 `--execute`。

### 误区 4：绕过 send.py 直接发舵机

`send.py` 里有统一的帧结构检查和速度检查。绕过它会跳过安全边界。

### 误区 5：一开始就读 viewer

`servo_trajectory_viewer.py` 很长，包含 UI、绘图、连续控制和硬件同步。新手先读核心链路，再读 viewer。

### 误区 6：先学太多无关 Python

网络、数据库、网页、异步不是当前重点。先把本项目用到的 Python 学扎实。

## 13. 最小验收标准

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

建议把这些问题写在笔记本第一页。每读完一个阶段，就回头用自己的话回答一次。

## 14. 中文文字教程与链接

这一部分只收录文字教程、官方文档和可查阅的中文网页，不把视频教程作为主要学习资料。使用方法不是从头到尾背完，而是按照前面 1～8 阶段遇到的问题去查对应内容。对于本项目来说，最重要的是能读懂 `send.py -> gait.py -> hex.py -> leg.py / servo.py -> config.py` 这条代码调用链，而不是把 Python 所有方向都学完。

### 14.1 入门主线教程

| 教程名称 | 链接 | 建议学习内容 | 对应本项目阶段 |
|---|---|---|---|
| 廖雪峰 Python 教程 | <https://liaoxuefeng.com/books/python/index.html> | 变量、字符串、判断、循环、函数、模块、类的基本概念 | 第 1～6 阶段 |
| 菜鸟教程 Python3 | <https://www.runoob.com/python3/python3-tutorial.html> | 基础语法速查，适合查列表、元组、字典、条件判断、循环、函数 | 第 2～4 阶段 |
| Python 官方中文文档 | <https://docs.python.org/zh-cn/3/> | 权威文档，适合遇到不确定概念时查证 | 全阶段 |

建议先读“廖雪峰 Python 教程”的基础部分，因为它比较适合从零开始建立语法框架。不要一开始就读到网络编程、数据库、Web 开发、协程这些部分，它们和当前六足机器人代码关系不大。菜鸟教程更适合当作语法速查表，遇到 `list`、`dict`、`for`、`if`、`def` 不熟时再查。

### 14.2 Windows、PowerShell 和 VS Code

| 教程名称 | 链接 | 建议学习内容 | 对应本项目问题 |
|---|---|---|---|
| VS Code Python 中文教程 | <https://vscode.github.net.cn/docs/python/python-tutorial> | 安装 Python 扩展、选择解释器、创建虚拟环境、运行和调试 Python 文件 | `.venv`、运行 `.py`、调试代码 |
| Microsoft PowerShell 中文文档 | <https://learn.microsoft.com/zh-cn/powershell/> | 当前目录、命令行、路径、脚本执行的基本概念 | Windows 终端运行 `python .\sdk\send.py ...` |
| Python 虚拟环境 venv 官方文档 | <https://docs.python.org/zh-cn/3/library/venv.html> | 虚拟环境的创建、激活、隔离依赖 | `.venv`、`requirements.txt` |

你在 Windows 里运行项目时，最容易卡住的不是 Python 数学，而是“当前终端在哪个目录”“为什么找不到文件”“为什么 Python 解释器不是项目里的 `.venv`”。所以 VS Code 和 PowerShell 的基础要先补一点。

需要掌握的最低要求是：

```text
1. 会用 cd 切换目录。
2. 会用 dir 或 ls 查看当前文件夹内容。
3. 知道 python .\sdk\send.py 是运行某个文件。
4. 知道 python -m sdk_pi.send 是按包模块运行。
5. 知道 .venv 是项目自己的 Python 环境。
6. 知道 requirements.txt 是第三方库清单。
```

### 14.3 项目代码中常用标准库

| 标准库 / 概念 | 链接 | 你需要看懂的内容 | 对应项目文件 |
|---|---|---|---|
| `argparse` | <https://docs.python.org/zh-cn/3/library/argparse.html> | 命令行参数，如 `--mode`、`--stride-x`、`--lift`、`--execute` | `send.py`, `cpg_control.py`, `imu_check.py` |
| `dataclasses` | <https://docs.python.org/zh-cn/3/library/dataclasses.html> | `@dataclass`、数据类、`frozen=True` | `config.py`, `gait.py`, `gait_controller.py`, `imu.py` |
| `typing` | <https://docs.python.org/zh-cn/3/library/typing.html> | 类型提示，如 `tuple[float, float, float]`、`Mapping[str, Point3]` | `robot_types.py` 和多数 `sdk/*.py` |
| `math` | <https://docs.python.org/zh-cn/3/library/math.html> | 三角函数、角度弧度转换、`sin`、`cos`、`atan2`、`hypot` | `leg.py`, `hex.py`, `gait.py`, `cpg_phase.py` |
| `pathlib` | <https://docs.python.org/zh-cn/3/library/pathlib.html> | 文件路径处理，避免路径字符串混乱 | 日志、配置、绘图工具 |
| `sys` | <https://docs.python.org/zh-cn/3/library/sys.html> | Python 解释器、模块搜索路径、命令行参数 | 导入兼容代码 |
| `importlib` | <https://docs.python.org/zh-cn/3/library/importlib.html> | 动态导入模块，初期只需知道它和导入兼容有关 | 可直接运行的工具脚本 |

这些官方文档不适合像教材一样从头读。更好的方式是：先在项目代码里遇到，再回到文档里查。例如你看到 `@dataclass(frozen=True)`，再去看 `dataclasses`；你看到 `parser.add_argument(...)`，再去看 `argparse`。

### 14.4 模块、包和导入

| 教程名称 | 链接 | 建议学习内容 | 对应项目问题 |
|---|---|---|---|
| Python 模块和包教程 | <https://pythonhowto.readthedocs.io/zh_CN/latest/module.html> | `import`、包、`__init__.py`、模块搜索路径 | 理解 `sdk/` 为什么能被 import |
| Python 官方模块教程 | <https://docs.python.org/zh-cn/3/tutorial/modules.html> | 模块、包、从模块导入名称 | 理解 `from .config import ...` |

本项目中 `sdk/` 和 `sdk_pi/` 都应理解为 Python 包。因为包里有多个 `.py` 文件互相调用，所以会出现：

```python
from .config import LEG_ORDER
from . import hex
from sdk import gait
```

这里不要死记。你只要先建立这个直观理解：

```text
一个 .py 文件可以被当成模块。
一个带 __init__.py 的文件夹可以被当成包。
包里面的模块可以互相 import。
```

### 14.5 NumPy 和 Matplotlib

| 教程名称 | 链接 | 建议学习内容 | 对应项目问题 |
|---|---|---|---|
| NumPy 官方中文文档 | <https://numpy.org/doc/stable/user/index.html> | 数组、矩阵、向量运算，先看基础数组即可 | 后续轨迹、坐标变换、绘图数据处理 |
| Matplotlib 官方教程 | <https://matplotlib.org/stable/tutorials/index.html> | 基础折线图、坐标轴、图例、保存图片 | 舵机轨迹、IMU 数据、论文图 |
| Matplotlib 中文教程 | <https://www.runoob.com/matplotlib/matplotlib-tutorial.html> | 快速查画图语法 | `servo_trajectory_viewer.py`, `plot_paper_figures.py` |

NumPy 和 Matplotlib 不是第一周重点。等你开始分析舵机脉宽曲线、IMU 曲线、足端轨迹、论文图表时再看。入门阶段只需要知道：NumPy 更适合处理一组数字，Matplotlib 用来画图。

### 14.6 Git 和项目管理

| 教程名称 | 链接 | 建议学习内容 | 对应项目问题 |
|---|---|---|---|
| Git 官方中文文档 | <https://git-scm.com/book/zh/v2> | 仓库、提交、分支、查看修改 | 保存不同版本的代码 |
| GitHub 文档中文入口 | <https://docs.github.com/zh> | 克隆仓库、查看代码、管理项目 | 阅读别人开源六足机器人代码 |

Git 不是控制机器人运动的代码，但对你后续改项目很重要。你至少要学会：

```text
git status      查看哪些文件被修改
git diff        查看具体改了什么
git add         暂存修改
git commit      保存一个版本
git log         查看历史记录
```

不要在没有备份的情况下直接大改 `config.py`、`servo.py`、`gait.py`。尤其是舵机方向、零偏、安装角这类硬件事实，改错后会影响真机安全。

### 14.7 推荐学习顺序

如果只按最省时间的路线走，可以这样安排：

| 顺序 | 学习内容 | 推荐链接 | 学到什么程度就够 |
|---|---|---|---|
| 1 | Python 基础语法 | <https://liaoxuefeng.com/books/python/index.html> | 能看懂变量、判断、循环、函数、列表、字典 |
| 2 | 语法速查 | <https://www.runoob.com/python3/python3-tutorial.html> | 遇到不会的语法能查到例子 |
| 3 | VS Code 运行 Python | <https://vscode.github.net.cn/docs/python/python-tutorial> | 会选择解释器、运行 `.py`、调试简单代码 |
| 4 | PowerShell 基础 | <https://learn.microsoft.com/zh-cn/powershell/> | 会看当前目录、切换目录、运行命令 |
| 5 | 模块和包 | <https://docs.python.org/zh-cn/3/tutorial/modules.html> | 能理解 `import`、包、`from .config import ...` |
| 6 | `argparse` | <https://docs.python.org/zh-cn/3/library/argparse.html> | 能看懂 `send.py` 里的命令行参数 |
| 7 | `dataclasses` | <https://docs.python.org/zh-cn/3/library/dataclasses.html> | 能看懂 `ServoSpec`、`LegSpec`、`GaitFrame` 这类数据类 |
| 8 | `typing` | <https://docs.python.org/zh-cn/3/library/typing.html> | 能看懂类型提示，不需要自己写复杂泛型 |
| 9 | `math` | <https://docs.python.org/zh-cn/3/library/math.html> | 能看懂三角函数、角度和弧度转换 |
| 10 | NumPy / Matplotlib | <https://numpy.org/doc/stable/user/index.html>，<https://matplotlib.org/stable/tutorials/index.html> | 后续会处理轨迹数据和论文图时再深入 |

### 14.8 不建议现在花时间看的内容

下面这些内容不是不好，而是暂时和当前主线关系不大：

```text
Web 后端
爬虫
数据库
网络编程
异步 async / await
多线程 / 多进程
机器学习框架
大型 GUI 框架
```

你当前最需要的是：

```text
能运行脚本
能看懂函数调用
能看懂 list / tuple / dict
能看懂 import
能看懂 dataclass
能看懂 argparse
能顺着 send.py -> gait.py -> hex.py -> leg.py / servo.py -> config.py 读下去
```

### 14.9 怎么把教程和项目代码对应起来

不要单独学完 Python 再回来看项目。建议使用“教程 20 分钟 + 项目代码 40 分钟”的方式。

例如学完 `if / else` 后，马上去看：

```text
sdk/send.py
validate_args()
_validate_gait_args()
run()
main()
```

学完 `dict` 后，马上去看：

```text
sdk/config.py
LEG_SPECS
SERVO_SPECS
LEG_SERVO_IDS
```

学完函数后，马上去追踪：

```text
send.gait_command_frames()
↓
gait.commands()
↓
gait.pose_to_cmd()
↓
hex.ik()
↓
leg.ik()
↓
servo.q_to_pwd()
```

学完 `argparse` 后，回头看命令：

```text
python .\sdk\send.py --mode wave --stride-x 2 --lift 2.5 --frames 18 --cycles 1 --duration 0.9
```

逐个解释：

```text
--mode       选择 stand / wave / ripple / tripod
--stride-x   前后方向步幅
--lift       抬脚高度
--frames     一个周期分多少帧
--cycles     执行几个周期
--duration   每帧或每段持续时间，具体以代码实现为准
--execute    是否真正发送到硬件
```

最后的学习目标不是“我学完了 Python”，而是你能用自己的话解释：

```text
一条命令如何从终端输入，经过 send.py 参数解析，进入 gait.py 生成足端轨迹，再经过 hex.py 和 leg.py 求 IK，最后由 servo.py 转成 pwd 舵机命令。
```
