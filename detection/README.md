# Supply Materials for Detection for Chimps

这部分我们使用[YOLOv5-7.0](https://github.com/ultralytics/yolov5)的代码框架.

使用如下格式的命令进行训练:

```
python train.py --weights checkpoints/yolov5m.pt  --cfg models/yolov5m.yaml  --data data/mydataset.yaml --epoch 300 --batch-size 8 --img 640 --workers 2 --device 0
```

我们去除不良数据以及进行数据增强所得的数据应该已经在[Roboflow](https://app.roboflow.com)上开源, 搜索Happy-hippo即可. 如果在获取数据上存在困难, 可以联系我们进行获取, 可以提供录屏保证数据是在ddl之前产生的.

我们的训练日志和checkpoints的北大网盘链接:

<https://disk.pku.edu.cn:443/link/66AD7371E51949CF405E66B1500E9C63>

<https://disk.pku.edu.cn:443/link/DA7AFC44F8265C4C2F719FF17EB02364>

我们的video demo的北大网盘链接:

<https://disk.pku.edu.cn:443/link/B59B41418D86BD2033E4C323D972D4B3>
