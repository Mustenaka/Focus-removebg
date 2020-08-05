# Focus-removebg

本项目为利用removebg的接口实现的自动替换证件照背景色的PYTHON小工具，并随项目一共副赠几个已经申请了的API接口，每一个API接口每个月可以免费使用50次。

#### 运行前需求：

安装pillow使用

> pip install pillow

或者

> pip install -r requirements.txt

#### 运行时：

直接python RemoveBG_Color.py 即可

#### 程序修改说明：

\# API KEY这里填写申请得到的API

APIkey = "swgmh9EQKCxBbEv52CJMqNpE"



\# 输入 -- 需要修改的图片，请放在img文件夹下

Imgname = "sunxiaochuan.jpeg"



\# 输出 -- 填空则为默认地址out/ans.png

outImagePath = ""



\# 需要替换的颜色 RGB 值，自己百度一下RGB色轮表即可

changeColor = (255, 255, 255) 



#### 提供的几个邮箱和API

| mail                                                        | API                      |
| ----------------------------------------------------------- | ------------------------ |
| [vss6jwct29pw@163.com](mailto:vss6jwct29pw@163.com)         | L3m76WEGhFpTUTZoL5JX1i8c |
| [iwcmzjp69gtzgjz3@163.com](mailto:iwcmzjp69gtzgjz3@163.com) | swgmh9EQKCxBbEv52CJMqNpE |
| [rb1brel18ey@163.com](mailto:rb1brel18ey@163.com)           | Fd7aGL8iDDaTvP3NbVFPczqW |
| [j0jwjt0gmt@163.com](mailto:j0jwjt0gmt@163.com)             | gbs4wR7Rcr7VzdXcETx1xTAH |
| [ms5icpzfpvp@163.com](mailto:ms5icpzfpvp@163.com)           | o1o22TyLk3NNnvnCEh8aFqas |

#### 生成：

如例：

在img文件夹中放有：sunxiaochuan.jpeg

![sunxiaochuan](/img/sunxiaochuan.jpeg)

运行后在img生成一个无背景图片的缓存文件sunxiaochuan.jpeg_no_bg.png

![sunxiaochuan.jpeg_no_bg](/img/sunxiaochuan.jpeg_no_bg.png)

如果没有特殊的输出需求，则默认在out文件夹中生成一个经过颜色替换后的图片

![ans](/out/ans.png)



#### 其余内容：

> error.log						生成错误文件
>
> requirements.txt		为python的第三方库需求文件

各种升级修改任君想象，由于API地址已经开源，因此建议由此需求的项目可以自行批量注册一批API