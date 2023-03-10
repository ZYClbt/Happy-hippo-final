# Supply Materials for Detection for Chimps

## Cleaning and organizing the data

我们使用该文件夹中`del.py`的脚本删除空白标注对应的图片文件, 然后在Windows系统中, 在标注的文件夹中将文件按大小升序排列, 删除所有排在最前面的显示大小为0的标注文件, 即完成了数据的清理.

## Training and testing

这部分我们使用[YOLOv5-7.0](https://github.com/ultralytics/yolov5)的代码框架, 从这里下载对应的预训练模型.

在组织数据集时, 我们编写了文件夹中的`mydataset.yaml`. 对于训练和验证数据集的组织, 图片和标注文件是训练集和验证集混在一起的, 用`mydataset.yaml`中路径对应的两个`.txt`文件确定训练集和测试集, 其中每一行是一张图片的位置. 我们用文件夹中的`txtgene.py`生成这两个文件. 当时在填写相对位置时出了一些错, 我们用`convert.py`做批量的修改.

使用如下格式的命令进行训练:

```
python train.py --weights checkpoints/yolov5m.pt  --cfg models/yolov5m.yaml  --data data/mydataset.yaml --epoch 300 --batch-size 8 --img 640 --workers 2 --device 0
```

我们去除不良数据以及进行数据增强所得的数据已经在[Roboflow](https://app.roboflow.com/)上开源, 并可以从下表的链接中下载. 如果在获取数据上存在困难, 可以联系我们进行获取, 可以提供录屏保证数据是在ddl之前产生的.

| 项目 |
|:------:|
| [去除不良数据](https://universe.roboflow.com/happy-hippo/happy-hippo/dataset/3) |
| [Hue+Saturation](https://universe.roboflow.com/happy-hippo/happy-hippo/dataset/9) |
| [Contrast+Brightness](https://universe.roboflow.com/happy-hippo/happy-hippo/dataset/5) |
| [Hue+Brightness](https://universe.roboflow.com/happy-hippo/happy-hippo/dataset/8) |

我们的训练日志和checkpoints的北大网盘链接(下面两个链接分别是两个作者完成的训练部分):

<https://disk.pku.edu.cn:443/link/66AD7371E51949CF405E66B1500E9C63>

<https://disk.pku.edu.cn:443/link/DA7AFC44F8265C4C2F719FF17EB02364>

我们的video demo的北大网盘链接:

<https://disk.pku.edu.cn:443/link/B59B41418D86BD2033E4C323D972D4B3>
