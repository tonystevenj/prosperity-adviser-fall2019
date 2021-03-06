﻿# 简介

项目代码库分为前端、后端两部分，采用前后端分离的开发方式，通过http api进行数据交互。

前端部分使用NodeJS + Vue框架 + ElementUI样式库

后端使用Python + Flask框架运行HTTP Server

# NodeJS 前端
**项目目录**：Application
首次启动需要安装NodeJS以及相关依赖，NodeJS安装方式可以google一下，然后按照下面方式进行：

``` bash
# 安装项目依赖
npm install

# dev方式启动项目，成功后访问 localhost:8081
npm run dev

# 开发完成后进行编译，此步骤可以忽略
npm run build
```

### 开发
#### 地图
地图所有代码在index.vue中，每个部分都有对应注释及文档链接

#### 图表
结构：components/layer.vue 为所有图表浮层的主文件，新增图表参照 components/drawTest.vue 及注释进行开发在layer.vue中引用



# Python 后端
**项目目录**：Server
## 依赖服务
- redis 用来做地理位置信息检索
> 仓库中的服务器地址是默认的本地地址，需要连公共服务需要替换配置文件 ***./config/redis.toml***

## 数据
### 可通过 python -m Server downloaddata 来获得所有需要的数据
### 保证以下文件在
- ./data/yelp_dataset/business.json
- ./data/yelp_dataset/review_Phoenix.csv
- ./data/parks.csv

## 环境初始化
所有系统环境都相对于DataVisualization目录下
``` bash
# 安装环境所需依赖
pip install -r Server/requirements.txt

# 开发完成后如果有新增的包，请通过pip安装pipreqs包进行包依赖的管理，然后提交更新后的requirements.txt
# 安装pipreqs
pip install pipreqs
# 梳理依赖
pipreqs Server --force
```

## 初始化脚本
### 用来将数据写入redis geo指定的key中
``` bash
# 进入目录 DataVisualization，执行
python -m Server init
```

## 启动Web服务
### 启动web服务
``` bash
# 进入目录 DataVisualization，执行
python -m Server run
```

### 测试访问地址
#### business数据
> http://127.0.0.1:8080/api/report/business?longitude=-112.073843&latitude=33.447999&radius=1

#### park数据
> http://127.0.0.1:8080/api/report/park?longitude=-112.073843&latitude=33.447999&radius=1

#### reviews大字报数据
> 所有数据： http://127.0.0.1:8080/api/report/reviews?longitude=-112.073843&latitude=33.447999&radius=0.1&category=reviewsfeature

#### Part 1, score 数据
>  http://127.0.0.1:8080/api/report/score?longitude=-112.073843&latitude=33.447999&radius=1&park_percentage=0.5&school_percentage=0.5&pride_percentage=0.5&hospital_percentage=0.5&rail_percentage=0.5

#### 与大字报有关的review/business数量数据
> 1. 关闭的店： http://127.0.0.1:8080/api/report/reviews?longitude=-112.073843&latitude=33.447999&radius=0.1&category=closedinfo
> 2. 1-3星的店：http://127.0.0.1:8080/api/report/reviews?longitude=-112.073843&latitude=33.447999&radius=0.1&category=star13info
> 3. 4-5星的店：http://127.0.0.1:8080/api/report/reviews?longitude=-112.073843&latitude=33.447999&radius=0.1&category=star45info




## 开发
### 扩展数据补充
> 1. 先确保自己本地的数据文件是最新的，通过 python -m Server downloaddata 来获取云端最新数据;
> 2. 加入在data folder里面加入自己要补充的数据，执行 python -m Server uploaddata AK SK 推送本地data到云端;
> 注：AK SK 是CDN服务器的登录密码
### 扩展数据开发
> 扩展数据参考./models/data/business.py，里面有详细的注释。
> 1. 在同目录下复制 ***business.py***（负责原始数据解析和导入） ，修改Business的类名以及其中的load方法，按指定格式返回两个dict，上游代码会自动在redis和内存中建立索引；
> 2. 在刚才新写好的类文件的最下面，注册这个类的对象；
> 3. 在同目录下 ***\_\_init\_\_.py*** 中仿照business那行的导入复制一条，让代码在启动时执行；
> 4. 可以使用 ***python -m Server init***（启动初始化脚本） 并输出进行验证数据是否成功解析；
> 5. 修改 ***/controller/report.py*** （负责api的具体业务逻辑），仿照business方法增加一个函数，接收请求参数并对数据进行处理然后输出；
> 6. 修改 ***./router.py*** （负责路由解析），仿照business添加一行，修改ruoute地址和业务处理方法，即上一条中新建的方法名；
> 7. 运行 ***python -m Server init*** （启动web服务）模拟请求进行验证；
> 8. 大功告成！
