<div align="center">
  <img src="README.assets/congratulations.svg"
    alt="congratulations image"
    style="width: 20rem;">
  <h1>2024-SEU-Graduates-Big-Data</h1>
  <p style="font-weight: bold;">东南大学 2024 届毕业生大数据项目</p>
  <p>网页链接：<a href="https://gradudata2024.seu.edu.cn">https://gradudata2024.seu.edu.cn</a></p>
  <p style="font-size: 0.8rem; font-style: italic;">（本应用仅对东南大学 2024 届全体毕业生开放，非毕业生可访问 <a href="https://gradudata2024.seu.edu.cn/demo">demo 页面</a> 查看效果）</p>
</div>

## :movie_camera: 演示

<div align="center">
  <img src="README.assets/demo.gif"
    alt="demo gif"
    style="width: 15rem;">
</div>

## :clapper: 简介

本项目由东南大学网络与信息中心牵头组织，在毕业之际回顾在东南大学的校园生活，为每位毕业生留下一份独一无二的美好回忆。

插画绘制和UI设计由唐万媛同学完成，文案部分由李蕴晗同学撰写，前后端开发及部署由李光伟完成，感谢各位在此期间的辛勤付出，以及感谢网信中心的老师、同学们提供的原始数据、服务器、域名申请等支持，还有参与内测的同学们所反馈的宝贵意见。

应该是学校首次推出此类数据报告，难免存在考虑不周的地方，但总体上希望这是一个好的尝试和开端，期待未来的同学们能在此基础上产出更好的作品。

**技术栈**：

- 后端
  - 框架：Django
  - 数据库：MySQL
  - 身份认证：基于 django-cas-ng
  - 性能监测：django-debug-toolbar
- 前端
  - HTML + CSS + JavaScript
  - 轮播插件：Swiper.js
- 服务部署
  - Docker + Nginx + uWSGI

## :page_facing_up: 使用许可

项目代码使用 [GPL 3.0 License](./LICENSE)，欢迎自由使用、修改、分享

项目中的插图、UI 等资源版权归原作者所有，**未经授权勿作它用**

## :open_file_folder: 目录结构

```text
2024-SEU-Graduates-Big-Data
|---2024_SEU_Graduates_Big_Data     # 项目主目录
|   |---settings.py                 # - 项目配置文件
|   |---urls.py                     # - 项目 URL 配置
|   \---wsgi.py                     # - 项目 WSGI 配置
|
|---app_health_check                # 健康检查应用目录（提供给数据中心用于检查服务状态）
|
|---app_demo                        # 演示应用目录（页面样式与主应用相同，但不使用真实数据）
|
|---app_main                        # 向用户展示的主应用目录
|   |---models                      # - 数据模型目录
|   |---templates                   # - HTML 模板目录
|   |---views                       # - 视图函数目录（欢迎页面、个人数据展示页面）
|   \---urls.py                     # - 应用 URL 配置
|
|---django_cas_ng                   # CAS 认证客户端目录（修改自 django-cas-ng ）
|
|---sql_scripts                     # SQL 脚本
|   |---fill_null_values.sql        # - 填充 graduates_big_data 表中的空值
|   \---gen_xxx_table.sql           # - 生成辅助统计表
|
|---static                          # 静态文件
|   |---app_main                    # - 主应用静态文件（CSS、字体、图片）
|   \---swiper-11.1.3               # - Swiper 轮播图插件
|
|---Dockfile                        # Docker 镜像构建文件
|---my.cnf                          # MySQL 连接信息（需自行创建）
|---requirements.txt                # 依赖包列表
|---uwsgi.ini                       # uWSGI 配置文件
\---xxx_uwsgi.sh                    # uWSGI 启动、停止脚本
```

## :compass: 本地开发指导

默认本地开发过程中 `DEBUG=True`，否则需要配置静态文件等服务，请参照 [使用 Docker 部署](#使用-docker-部署) 中相关内容进行配置。

### 0. 环境

- Python 3.9
- MySQL 8.0
- Nginx

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

_注：安装依赖前请确保本地 MySQL Client 已配置完成_

### 2. 数据库相关配置

#### 2.1 配置连接信息

创建数据库（本地或远程均可），并在项目根目录下创建 `my.cnf` 文件，填写连接信息，内容如下：

```ini
[client]
database = database_name
user = username
password = P4ssw0rd
host = localhost
port = 3306
default-character-set = utf8
```

_注：请按照实际情况填写上述各字段_

#### 2.2 数据库迁移

配置完成后，执行以下命令进行数据库迁移，创建对应数据表：

```bash
python manage.py makemigrations
python manage.py migrate
```

将会在所指定的数据库中创建多张表： 以 `gbd_` 开头的为数据统计、展示相关表；以 `django_cas_ng_`
开头的为身份认证相关表；以 `auth_` 和 `django_` 开头的为 Django 默认表。

#### 2.3 提供数据

首先，必须要提供以下 3 张表的数据：

`gbd_graduate_personal_stat`、`gbd_library_borrowing_stat` 和 `gbd_sports_competition_stat`

接下来，执行 [sql_scripts](./sql_scripts/) 目录下的几个 SQL
脚本（[fill_null_values.sql](./sql_scripts/fill_null_values.sql) 应被首先执行），填充空值、生成辅助统计表。

### 3. 网络相关配置

由于统一身份认证系统有服务授权限制，只对已注册的服务（域名）提供认证服务，所以在本地开发时需要配置域名解析和反向代理，将已报备注册的域名指向本地服务器。

#### 3.1 本地域名解析

向 `/etc/hosts` 文件中添加以下内容，将域名指向本地：

```text
127.0.0.1 gradudata2024.seu.edu.cn
```

#### 3.2 Nginx 反向代理

向 Nginx 配置文件中添加所要代理的域名配置：

```text
# http
server {
    listen 80;
    server_name gradudata2024.seu.edu.cn;
    location / {
        proxy_pass http://127.0.0.1:8000;
    }
}

# https
server {
    listen 443 ssl;
    server_name gradudata2024.seu.edu.cn;
    ssl_certificate /path/to/cert.pem;  # 证书路径
    ssl_certificate_key /path/to/cert.key;  # 证书密钥路径
    location / {
        proxy_pass http://127.0.0.1:8000;
    }
}
```

_注：由于此项目报备注册的域名为 https 协议，所以需要配置 https 代理和相应的 SSL 证书。_

### 4. 启动服务

```bash
python manage.py runserver 0.0.0.0:8000
```

## :whale: 使用 Docker 部署

当项目开发基本完成后，需要将服务部署到服务器上。为了简化环境配置的过程，强烈建议使用 Docker 部署。

在本项目中，Docker 仅用于提供 Django 服务所需的 Python 及其依赖包的运行环境，而没有将 MySQL 和 Nginx 一并打包，如有需要也可自行修改。

### 0. 环境

- 本地
    - Docker
- 服务器
    - Docker
    - MySQL 8.0
    - Nginx
    - 拷贝整个项目到服务器

### 1. 部署前配置

#### 1.1 环境变量

在生产环境中，需要设置 `DEBUG=False`，并配置 `SECRET_KEY` 以确保安全性。

在项目根目录下创建 `.env` 文件，填写以下内容：

```text
DJANGO_DEBUG=False
DJANGO_SECRET_KEY='xxxx'
```

_注：`SECRET_KEY` 可以通过以下命令生成：_

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

#### 1.2 数据库

在服务器上配置好 MySQL 数据库，按照 [配置连接信息](#21-配置连接信息) 部分的说明，创建并将数据库连接信息填写到 `my.cnf`
文件中。

#### 1.3 Nginx

避免在生产环境使用 `runserver` 命令，本项目中使用 uWSGI 配合 Nginx 进行部署。

在 Nginx 配置文件中添加以下内容，配置静态文件服务和 uWSGI 代理：

```text
server {
    listen       20246;  # 对外端口
    server_name  gradudata2024.seu.edu.cn;

    location /static {
        alias /path/to/2024-SEU-Graduates-Big-Data/static;  # 静态文件目录
    }
    location / {
        include uwsgi_params;
        uwsgi_pass 127.0.0.1:3031;  # 与 uwsgi.ini 中的 socket 一致
    }
}
```

### 2. 【本地】构建并导出镜像

```bash
# 构建镜像（在项目根目录下执行）
docker buildx build -t graduates-big-data:latest .

# 导出镜像
docker save graduates-big-data:latest > docker-img-graduates-big-data.tar
```

### 3. 【服务器】导入并运行镜像

使用 scp 或其他方式将**导出的镜像文件**及**整个项目目录**传输到服务器上。

执行以下命令导入镜像：

```bash
docker load < /path/to/docker-img-graduates-big-data.tar
```

进入容器交互模式，在容器中执行数据库迁移、静态文件收集等操作。

在这里使用了 `-v` 参数挂载整个项目目录，以便在容器外修改代码：

```bash
docker run -it --name graduates-big-data \
           -v /path/to/2024-SEU-Graduates-Big-Data:/app \
           --env-file /path/to/2024-SEU-Graduates-Big-Data/.env \
           --network host graduates-big-data:latest \
           /bin/bash

# 容器内执行
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
python manage.py check --deploy  # 检查部署环境
uwsgi --ini uwsgi.ini  # 测试 uWSGI 配置是否正确
exit
```

在数据推送完成、静态文件服务配置完成，且测试运行正常后，可以守护进程方式运行容器：

```bash
docker run -d --name graduates-big-data \
           -v /path/to/2024-SEU-Graduates-Big-Data:/app \
           --env-file /path/to/2024-SEU-Graduates-Big-Data/.env \
           --network host graduates-big-data:latest
```

_注：上述各命令中的 `/path/to/xxx` 需要替换为实际路径。_

容器仅用于为 Django 服务提供运行环境，所以保持运行即可。服务的启动、停止可以借助目录下的两个脚本：

```bash
docker exec -it graduates-big-data /bin/bash /app/start_uwsgi.sh  # 启动服务
docker exec -it graduates-big-data /bin/bash /app/stop_uwsgi.sh   # 停止服务
```

代码有变动无须重启容器，将代码推送到服务器后使用上述脚本重启服务即可。

## :ladder: 补充说明

项目的 [CAS 认证客户端](./django_cas_ng/) 部分主要基于 [django-cas-ng](https://github.com/django-cas-ng/django-cas-ng) 和 [python-cas](https://github.com/python-cas/python-cas)（均使用 MIT License），在此基础上进行了一定的修改，以适配东南大学的统一身份认证系统。

修改部分在代码中按照以下形式标注，以便检索：

```python
# ----- MODIFIED START ----- #
# code = 'original code'
code = 'modified code'
# ----- MODIFIED END ----- #
```
