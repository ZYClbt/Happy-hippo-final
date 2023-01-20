# Supply Materials for identification for Chimps

## Baseline

Baseline的结果及日志在下面的北大网盘链接中提取:
<https://disk.pku.edu.cn:443/link/BE6C2D682820C5028F0B6B550D2C8507>

## Practice with SimSiam
这部分我们直接使用[SimSiam](https://github.com/PatrickHua/SimSiam)的框架.

代码下载到本地后, 在`SimSiam/datasets`中新建一个`DATA`文件夹, 将欲处理的图片转化为cifar10的格式放在其中, 在终端运行下面的命令, 结果生成在`SimSiam/logs`中.

```
python main.py --data_dir datasets/Data/ --log_dir logs/ -c configs/simsiam_cifar.yaml --ckpt_dir ~/.cache/ --hide_progress --device cuda:0
```
将原有的数据集转化为cifar10格式的python代码参考了github上的[这个](https://github.com/haodonga/CIFAR-Dataset-master)项目，转化后的数据集在下面的北大网盘链接中提取:

<https://disk.pku.edu.cn:443/link/8CB9DA1A9FDCAD49F09055DF83BDA260>

我们在报告中展示了来自两次训练的训练日志，这两份训练的结果及日志在下面的北大网盘链接中提取:

<https://disk.pku.edu.cn:443/link/762CBD65EEA8BBC346497EAF14A3CB9D>

## Practice with YOLOv5
这部分我们基于[YOLOv5](https://github.com/ultralytics/yolov5)的框架.

代码下载到本地后, 在`yolov5-v7.0`中新建一个`datasets`文件夹, 将欲处理的图片放在其中, 在终端运行下面的命令, 结果生成在`yolov5-v7.0/runs/train-cls`中.

```
python classify/train.py --model weights/yolov5m-cls.pt --data datasets/id --epochs 150 --img 224 --batch 64 --device 0 --workers 2
```
训练用的数据集在下面的北大网盘链接中提取:

<https://disk.pku.edu.cn:443/link/7BE7093DB50B8D3A9B78BAC47E27E25B>

由于技术有限，没能完成演示视频，我们将验证集中的所有图片经上面训练得到的模型进行了验证，该结果在下面的北大网盘链接中提取:

<https://disk.pku.edu.cn:443/link/43C5A6DDDAAACFA89896C14BB64556CF>

进行上面的验证需要在终端运行的命令是

```
python classify/detect.py --weights weights/best.pt --source datasets/id/test/ --device 0 --img 224
```

我们在报告中展示了来自五次训练的训练日志，这五份训练的结果及日志在下面的北大网盘链接中提取:

<https://disk.pku.edu.cn:443/link/AB46940142AAF1C54613AE6914B482C3>




