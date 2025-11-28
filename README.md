# 目录

[安装](#安装)

[使用](#使用)

# 安装

## 前置条件

确保安装 `Python3` 及其 `Flask` 库。

`Flask` 库可以通过

```shell
pip install flask
```

安装。

## 安装/运行

### Windows

运行目录下 `Windows_Start.bat`。**（未测试）**

### MacOS

1、**终端进入当前目录**。

2、运行 

```shell
chmod a+x MacOS_Start.sh
```

确保可以正常运行。**（只有第一次需要使用这个代码）**

3、运行

```shell
MacOS_Start.sh
```

### Linux

运行目录下 `Linux_Start.bat`。**（未测试）**

### 停止运行

点击 `Ctrl+C`。

地址为 `http://服务器ip:5000`。

## 附：内网穿透



在终端运行 `ngrok http 5000` 即可进行内网穿透，它会给你一个域名，具体操作可上网搜索，教程很多。

### 添加/更改/删除用户

打开同目录下的 `start.py`，找到 `UserPw` 字典，修改键值对，注意是字符串类型，改成如：

```python
UserPw={
'username':'password', # 前面是用户名，后面是密码
'user2':'pw2'
}
```

那么就有2个用户，第一个叫username，其密码为password，第二个叫user2，其密码为pw2。

~~直接改源代码，实现起来就是简单（~~

# 使用

## 上传文件

确保你已经登录。

点击“选取文件”按钮，选好后**点击上传**，看到“上传完成”后代表上传完成。

## 下载文件（仅测试版）

确保你已经登录。

`http://服务器ip:5000/download/文件名` 下载自己已上传的文件。
