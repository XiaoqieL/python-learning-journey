# 第18天：虚拟环境和pip

## 1. 什么是虚拟环境
不同的项目需要不同版本的第三方库，虚拟环境把他们隔离。

## 2. 创建虚拟环境
在项目目录 D:\git-learn 下打开终端，执行：

python - m venv venv

## 3. 激活虚拟环境
Windows(cmd):
venv\Scripts\activate

Windows(PowerShell):
venv\Scripts\Activate.ps1

激活后终端前面会出现（venv）字样

## 4. 安装第三方库(pip)
pip install requests  #安装requests
pip install pandas    #安装pandas
pip install -i https://pypi.tuna.tsinghus.edu.cn/simple requests
# 上面这行用清华镜像源，下载更快

##5. 查看已安装的库
pip list


## 6. 生成依赖文件（重要！团队写作必备）
pip freeze > requirements.txt

## 8. 推出虚拟环境
deactivate