# ASUS TUF GAMING Fan_Boost_Mode Controller
On Linux platforms, ASUS TUF GAMING laptops run in quiet mode by default. Under this mode, the fans always run at low speed regardless the CPU and GPU loads, causes performance decrease due to overheating under heavy tasks.  
This script writes the value of `/sys/class/hwmon/hwmon5/device/fan_boost_mode` to enable or disable the Fan Boost Mode. __It requires `root` persmission to run.__
  
  
It is confirmed to work properly on my TUF GAMING FX504GM (FX80GM in China), but I'm not sure if it works on every TUF GAMING laptops. If it does not work, just find the correct path for your device and modify the script.
  
  
## Installation
0. Install `python3`.
1. Download the `fanboost.py` and put it to somewhere you like. The path should not contain any special characters.
2. Make it executable and link to `/usr/bin`:  
```
chmod +x fanboost.py
sudo ln fanboost.py /usr/bin/fanboost
```
3. Run `fanboost --help` for usage.
  
  
# 飞行堡垒风扇狂暴模式控制器
在Linux平台上，华硕飞行堡垒笔记本默认以安静模式运行。在此模式下，无论CPU和GPU负载多高，风扇都只会以低速运行。这造成的结果就是跑高负载任务的时候很容易降频。  
此脚本通过修改 `/sys/class/hwmon/hwmon5/device/fan_boost_mode` 的值开关风扇“狂暴”模式，__这需要`root`权限来操作__。
  
  
我只能确定此工具在我的飞行堡垒FX504GM（国内FX80GM）上正常运行。如果你的其他飞行堡垒机型没法正常使用，可以尝试找到正确的配置文件路径并修改脚本中的值。
  
  
## 安装
0. 安装 `python3`
1. 下载 `fanboost.py` 并放到看着顺眼的地方。路径里最好不要有特殊字符。
2. 设置执行权限，链接到`/usr/bin`：
```
chmod +x fanboost.py
sudo ln fanboost.py /usr/bin/fanboost
```
3. 运行 `fanboost --help` 查看帮助信息。
