# Supply Materials for 2D Pose Estimation for Chimps

## Practice with AlphaPose
这部分直接使用[AlphaPose](https://github.com/MVIG-SJTU/AlphaPose)的框架.
代码下载到本地后, 在AlphaPose中新建一个videos文件夹, 将欲处理的视频放在其中, 在终端运行下面的命令, 结果生成在`--outdir`中.
```
demo_inference.py --cfg configs/halpe_coco_wholebody_136/resnet/256x192_res50_lr1e-3_2x-regression.yaml --checkpoint pretrained_models/multi_domain_fast50_regression_256x192.pth --video videos/test_video1.mp4 --outdir examples/res --save_video
```


