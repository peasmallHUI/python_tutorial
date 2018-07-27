# Python Tutorial


## 第一章 Python基础
### 第一节 Linux操作系统基础
- 常见命令
```bash
ls (-alh)   #查看当前路径内容
pwd         #查看当前路径
cd          #切换路径
touch       #创建文件
mkdir       #创建文件夹
clear       #清屏
--help      #帮助文档
man         #帮助文档，manual page
cat         #显示查看
rm (-r)     #删除，-r表示递归删除
more        #分屏显示
mv          #重命名，移动
cp          #复制
find        #查找，-size -name 
grep        #搜索，-n 行数，-v 反向，"^……"， "……$" 
ps          #进程
top         #实时进程
```

- 通配符
```bash
*           #任意内容
?           #任意一位
[]          #符合取值
```

- 重定向
```bash
$ ls > a.txt  #覆盖
$ ls >> a.txt #追加
```

- 管道
```bash
$ ls -alh /bin | more
```

- 路径相关
```bash
$ cd ./a    #.表示当前路径
$ cd ..     #..表示上一级路径
$ cd ~      #~表示家目录
```

- 归档
```bash
$ tar -cvf test.tar *.py        #打包
$ tar -xvf test.tar             #解包
$ tar -zcvf test.tar.gz &.py    #压缩
$ tar -zxvf test.tar.gz         #解压
```

- 用户相关
```bash
$ useradd testname -m           #增加用户，-m表示创建家目录
$ userdel testname              #删除用户
$ ssh name@ip                   #远程连接
$ chown                         #改变文件拥有着
$ chgroup                       #改变文件拥有组
$ chmod u=rwx                   #改变用户权限
$ chmod 137                     #改变用户权限，r=4，w=2，x=1
```

### 第二节 Python语法基础
