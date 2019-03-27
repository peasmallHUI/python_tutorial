# Python Tutorial


## 第一章 Python基础
### 第一节 Linux操作系统基础
1. 常见命令
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

2. 通配符
    ```bash
    *           #任意内容
    ?           #任意一位
    []          #符合取值
    ```

3. 重定向
    ```bash
    $ ls > a.txt  #覆盖
    $ ls >> a.txt #追加
    ```

4. 管道
    ```bash
    $ ls -alh /bin | more
    ```

5. 路径相关
    ```bash
    $ cd ./a    #.表示当前路径
    $ cd ..     #..表示上一级路径
    $ cd ~      #~表示家目录
    ```

6. 归档
    ```bash
    $ tar -cvf test.tar *.py        #打包
    $ tar -xvf test.tar             #解包
    $ tar -zcvf test.tar.gz &.py    #压缩
    $ tar -zxvf test.tar.gz         #解压
    ```

7. 用户相关
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

- 基础知识
    >交互模式<br>
    >注释 `#`<br>
    >`input` `print`<br>
    >`if` `elif` `else`<br>
    >`for in ` `while`<br>
    >`break` `continue`<br>

1. 字符串

    - 下标
        >python第一个元素下标为0<br>
        >python下标可以为负数，其中-1代表最后一个元素，以此类推<br>

    - 切片
        >[x:y:i] x为切片第一个元素，y为最后一个（不包括），i为步长<br>
        >缺省为0，-1，1<br>
    
    - 命令
        ```python
        string.find()           #返回第一个对应字符下标，未找到返回-1
        string.rfind()          #从右边查找第一个对应字符
        string.count()          #返回括号内次数字符串
        string.replace(,)       #用第二个字符串替代括号内第一个字符串
        string.split()          #
        string.startswith()     
        string.endswith()       
        string.strip()
        string.partition()
        string.isalpha
        string.join()
        ```

2. 列表

    - 增
        ```python
        list.append()
        list.insert(,)
        list.extend()
        ```
    - 删
        ```python
        list.pop()
        list.remove("")
        del list[]
        ```

    - 改
        ```python
        list[] = 
        ```

    - 查
        ```python
        in
        not in
        ```
3. 字典
    >{key:value,key:value}

    - 增 / 改
        ```python
        dict["key"] = value
        ```

    - 删
        ```python
        del dict[key]
        ```

    - 查
        ```python
        dict.get(key)
        ```

    - 命令
        ```python
        len(list)
        dict.keys()
        dict.values()
        dict.items()
        ``` 

4. `for`、`else`语句
    ```python
    for i in list:
        pass
    else:
        pass
    ```

5. 元组
    >不可变类型：数字、字符串、元组<br>
    >可变类型：列表、字典

6. 函数
    ```python
    def fun(arg1,arg2,arg=1,*arg,**kwargs):
        pass
    ```

7. 引用
    ```python
    a = 100 
    b = a
    id(a)
    id(b)
    ```

8. 递归
    ```python
    def fun(*arg):
        pass
        return res1 if something else res2
    ```

9. 匿名函数
    ```python
    lambda input:output
    ```

10. 文件
    ```python
    f = open("test.py", "wr")
    f.read()
    f.readlines
    f.write()
    f.seek(,)
    f.close()
    ```

11. 面向对象编程
    >类组成包含：类名称、属性、方法

    - 创建类
        ```python
        class class_name(parents):
            pass
            def __init__(self):
                pass
        ```
    
    - 对象
        - 类对象和实例对象
        - 类属性和实例属性
        - 私有属性和私有方法
        - 类方法和静态方法
    
    - 创建对象
        - \_\_new__
        - \_\_init__
        - 返回引用
    
    - 单例
        ```python
        pass
        __instance = None
        def __new__(cls):
            if __instance = None:
                return cls.__instance = object.__new__(cls)
            else:
                return cls.__instance
        pass
        ```

12. 异常
    ```python
    try:
        pass
    except(excp_name1,excp_name2):
        pass
    except Exception as inst:
        pass
        raise
    else:
        pass
    finally:
        pass
    ```

## 第二章 Python核心
### 第一节 Python核心编程
1. 拷贝
    - 引用
        >正常赋值不会新建对象，而是引用计数加一
    
    - 浅拷贝
        >只拷贝一层
        ```python
        import copy
        a = [1, 2, 3]
        b = copy.copy(a)
        b = a[:]
        ```
    
    - 深拷贝
        >一直拷贝
        ```python
        import copy
        c = copy.deepcopy(a)
        ```

2. 私有化
    >xx:公有变量<br>
    >_xx:禁止导入，类对象和子类可以访问<br>
    >__xx:外部无法访问（名字重整）<br>
    >\_\_xx\_\_:系统属性<br>

3. property
    ```python
    class Number(object):
        def __init__ (self):
            self.__num = 100
        
        def getnum(self):
            return self.__num
        
        def setnum(self,num):
            self.__num = num
        
        num = property(getnum, setnum)
    ```

    ```python
    class Number(object):
        def __init__(self):
            self.__num = 100
        
        @property
        def num(self):
            return self.__num
        
        @num.setter
        def num(self,num):
            self.__num = num
    ```


