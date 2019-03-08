利用Visual Studio跨平台远程调试功能实现一体化开发和调试。使用一个docker container作为调试环境并与本地后端环境交互。

![框架结构](https://github.com/w12379564/dev_demo/blob/master/images/arc.png)

本demo后端将post方法的json直接返回，并调试client使用post方法发送json到后端，并将返回结果打印到控制台。

步骤：

1. clone仓库到本地。

2. 运行命令`docker-compose up`。

![compose](https://github.com/w12379564/dev_demo/blob/master/images/compose.PNG)

3. 载入`dev_demo/client/client.sln`

4. 点击调试进入调试。

![click](https://github.com/w12379564/dev_demo/blob/master/images/click.PNG)

![debug](https://github.com/w12379564/dev_demo/blob/master/images/debug.PNG)
