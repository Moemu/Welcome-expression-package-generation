# “欢迎新人”表情包生成

## 效果截图

![](https://i.bmp.ovh/imgs/2021/07/dafc59b9b86d5dd8.jpg)

## 使用的字体

HarmonyOS Sans SC Black

## 文件说明

finally.jpg（输出文件）

first.jpg（未经加工的原文件）

fontlicence.txt（字体许可证）

Groupimg.py（主程序源码）

Groupimg.exe（主程序）

HarmonyOS_Sans_SC_Black.ttf（HarmonyOS_Sans_SC_Black字体文件）

licence（许可证）

LOGO.ico（作者的LOGO）

## 无GUI模式使用教程

（无GUI模式不自备exe可执行文件，您需要提前配置好Python环境和所使用的库）

下载此仓库的所有文件，运行`Groupimg.py`，在终端中输入新人的昵称后回车

然后会出现一个预览窗口（生成的表情包），预览后关闭此窗口，主程序根目录中会生成一个名为`finally.jpg`的图片，那就是刚才出现过的表情包

然后把它发到群上面去吧ヾ(≧▽≦*)o

## GUI使用教程

（使用GUI可能会降低启动速度）

下载此仓库的所有文件，运行`Groupimg(GUI).exe`，在弹出的窗口中输入新人的昵称，点击提交

然后会出现一个预览窗口（生成的表情包），预览后关闭此窗口，主程序根目录中会生成一个名为`finally.jpg`的图片，那就是刚才出现过的表情包

然后把它发到群上面去吧ヾ(≧▽≦*)o

## 高级教程

### 从源码启动程序

请先确认您有Python3环境，[点此跳转](https://www.python.org/)

在终端运行下列命令或确认您有指令中列出的库

```powershell
pip install opencv-python
pip install PySimpleGUI #GUI库
pip install Pillow
```

### 更改字体

请确认您更改的字体为可商用状态，若您使用未授权的字体而引发的版权问题WhitemuTeam概不负责

把你的字体文件放到此程序的根目录上

更改`Groupimg.py`：

```python
#设置需要显示的字体
fontpath= "HarmonyOS_Sans_SC_Black.ttf"
```

具体格式：fontpath= "你的字体文件.ttf"

保存退出，从源码启动程序

注意：这样可能会与原图片冲突，建议您联系WhitemuTeam获取原文件的psd，然后更改原文件的全部字体

### 更改提示语

更改`Groupimg.py`：

```python
word = '欢迎'+name+'进群' #生成第一行句子
```

或者联系WhitemuTeam获取原文件的psd，然后更改原文件的全部字体

## 许可证

HarmonyOS Sans SC Black为可商用状态，字体许可证见fontlicence.txt，如果侵犯了您的权益可联系WhitemuTeam

本程序遵守Apache License 2.0协议，未经允许不可商用

## 联系我们

邮箱：WhitemuTeam@outlook.com

WhitemuTeam
