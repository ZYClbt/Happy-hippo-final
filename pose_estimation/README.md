# Supply Materials for 2D Pose Estimation for Chimps

## Practice with AlphaPose
这部分我们直接使用[AlphaPose](https://github.com/MVIG-SJTU/AlphaPose)的框架.

代码下载到本地后, 在AlphaPose中新建一个videos文件夹, 将欲处理的视频放在其中, 在终端运行下面的命令, 结果生成在`--outdir`中.

```
demo_inference.py --cfg configs/halpe_coco_wholebody_136/resnet/256x192_res50_lr1e-3_2x-regression.yaml --checkpoint pretrained_models/multi_domain_fast50_regression_256x192.pth --video videos/test_video1.mp4 --outdir examples/res --save_video
```

这部分我们的测试用视频和结果在下面的北大网盘链接中提取:

<https://disk.pku.edu.cn:443/link/20A5FBF88B912B4B573BBBFB5FFD3566>

## Practice with MMPose
这部分我们基于[MMPose](https://github.com/open-mmlab/mmpose)的框架.

使用同上面的欲处理视频, 运行下面的命令, 可以生成结果在`--video-path`中. 这是论文中所说使用Macaque baseline, 因为没有进行detection产生的错误结果.

```
python demo/top_down_video_demo_full_frame_without_det.py configs/animal/2d_kpt_sview_rgb_img/topdown_heatmap/macaque/res50_macaque_256x192.py checkpoints/res50_macaque_256x192-98f1dd3a_20210407.pth --video-path test_video1.mp4 --out-video-root results/
```

该结果视频在下面的北大网盘链接中提取:

<https://disk.pku.edu.cn:443/link/E6E21AC0A3012DBC6DCDCB8A081D32EC>

我们使用coco-annotator自行整理并标注的猩猩数据集在下面的北大网盘链接中提取:

<https://disk.pku.edu.cn:443/link/5BF8FC299FD497DB5374350BB4558A09>

这个数据集放在mmpose文件夹的data子文件夹下, 这样就与mmpose的内设路径一致, 可以直接运行例如下面的命令进行训练.

```
python tools/train.py configs/animal/2d_kpt_sview_rgb_img/topdown_heatmap/macaque/hrnet_w32_macaque_256x192.py --work-dir work_dirs/hr32-3
```

涉及的三个配置文件对训练轮数和策略做了一些修改, 同时新增了加载预训练模型的步骤, 传在这个github文件夹中.

baseline的checkpoints在[MMPose的网站中](https://mmpose.readthedocs.io/en/latest/topics/animal.html)下载.






