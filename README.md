# ximalaya
这个项目可以快速爬取喜马拉雅广播电台的音频，注意是广播电台！

# 使用方法
打开喜马拉雅网页端，右键“检查”，选择“网络”，看到形如

![image](https://github.com/user-attachments/assets/461654b3-0a3e-4906-a161-50b79f1aca7f)的数据包，
选择后点击“响应”，看到形如
![image](https://github.com/user-attachments/assets/655855ee-e0b1-4638-a589-546ba2096bfd)的数据，

例如本图中出现的是
https://broadcast.tx.xmcdn.com/live/1011_64_240717_000331_2630.ts

就可以将main.py中第13行替换成
https://broadcast.tx.xmcdn.com/live/1011_64_240717_000331_{i:04x}.ts

可以简单观察到240717表示日期，2630是16进制的数据包编号。

由于广播电台是每7s更新一次，2630的十进制是9776，9776*7/60/60≈19

可以推断出这是19点的广播电台音频数据。

根据这个原理，你可以计算你想要爬取的开始数据包编号和结束数据包编号（十进制），然后修改main.py的7,8行。

目前还不知道000331表示的是什么

# 安装
需要安装以下：

requests：用于HTTP请求。

pydub：用于处理音频文件。

ffmpeg：用于音频和视频处理。

