## 胡搞的一点东西

最近上了个其实没太多营养的实训课，有小组作业要求做点东西，于是瞎搞了点东西。

过程比较随意，没用版本控制工具，写好了随便组合一下，这里仅上传我写的一点东西，可以作为以后Flask应用(搬砖)的一点参考。

## 残疾功能的介绍

#### 1.登录

有登录界面，但登录判断函数为摆设(队友来写)，第一次点击登录失败，第二次点击登录成功。

#### 2.山东省天气可视化

异步爬虫爬国家气象局 + 傻瓜式数据分析 + 搬砖画图

本来打算直接在flask中实现，但发现跑异步有问题报错没有解决，然后曲线救国使用多线程在线程中跑异步又报错了，于是直接用线程开命令行指令跑进程。(人菜瘾大)

#### 3.静态漫画

批量生成html代码的搬砖东西，很捞，其他没什么可说的，成品网页应该比我爬过的任何一个网页都好爬# Incomplete-Useless-Flask-Sample
