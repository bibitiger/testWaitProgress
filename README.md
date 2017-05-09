#用于PYQT的加载动画，基于QPainter实现

##使用

```
self.progress = MyWaitProgressDialog('begin...',self)
        self.progress.RotateStyle = MyRotateProgress.MyRotateProgress.PenStyleNormal
        self.progress.exec()
```

###分为三种样式
1.PenStyleGradient

self.progress.RotateStyle = MyRotateProgress.MyRotateProgress.PenStyleGradient

![ProgressGradient] (http://7xtz1f.com2.z0.glb.clouddn.com/image/qtProgress/ProgressGradient.gif-shuiyinBlack)

2.PenstylePerGradient

self.progress.RotateStyle = MyRotateProgress.MyRotateProgress.PenstylePerGradient

![ProgressPerGradient] (http://7xtz1f.com2.z0.glb.clouddn.com/image/qtProgress/ProgressPerGradient.gif-shuiyinBlack)


3.PenstyleNormal

self.progress.RotateStyle = MyRotateProgress.MyRotateProgress.PenstyleNormal

![ProgressNormal] (http://7xtz1f.com2.z0.glb.clouddn.com/image/qtProgress/ProgressNormal.gif-shuiyinBlack)