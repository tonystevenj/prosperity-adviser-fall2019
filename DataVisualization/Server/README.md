## 依赖服务
- redis 用来做地理位置信息检索
> 仓库中的服务器地址是默认的本地地址，需要连公共服务需要替换配置文件 ***./config/redis.toml***

## 数据
### 保证以下文件在
- ./data/yelp_dataset/business.json
- ./data/parks.csv

## 初始化脚本
### 用来将数据写入redis geo指定的key中
> 进入目录 ***DataVisualization***，执行 ***python -m Server init***

## 启动服务
### 启动web服务
> 进入目录 ***DataVisualization***，执行***python -m Server run***

### 测试访问地址
#### business数据
> http://127.0.0.1:8080/api/report/business?latitude=-112.073843&longitude=33.447999&radius=1

#### park数据
> http://127.0.0.1:8080/api/report/park?latitude=-112.073843&longitude=33.447999&radius=1

## 开发
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
