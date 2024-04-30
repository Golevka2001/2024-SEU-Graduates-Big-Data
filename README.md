# 2024-SEU-Graduates-Big-Data

## 本地开发

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

接下来，执行 [sql_scripts](./sql_scripts) 目录下的以 `gen_` 开头的 SQL 脚本，生成辅助统计表；

执行该目录下的 [calc_consts.sql](./sql_scripts/calc_consts.sql)
脚本，将统计得到的常量值填入 [constants.py](graduates_big_data/stat_data/constants.py) 中对应字段。

### 3. 网络相关配置

由于统一身份认证系统有服务授权限制，只对已注册的服务（域名）提供认证服务，所以在本地开发时需要配置域名解析和反向代理，将已报备注册的域名指向本地服务器。

#### 3.1 本地域名解析

向 `/etc/hosts` 文件中添加以下内容，将域名指向本地：

```text
127.0.0.1 gradudata2024.seu.edu.cn
```

#### 3.2 Nginx 反向代理

向 Nginx 配置文件中添加所要代理的域名配置：

```nginx
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
    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/cert.key;
    location / {
        proxy_pass http://127.0.0.1:8000;
    }
}
```

_注：由于此项目报备注册的域名为 https 协议，所以需要配置 https 代理和相应的 SSL 证书。否则，上述 https 部分配置可省略。_

### 4. 启动服务

```bash
python manage.py runserver 0.0.0.0:8000
```

## 补充说明

项目的 [CAS 认证客户端](./django_cas_ng) 部分主要基于 [django-cas-ng](https://github.com/django-cas-ng/django-cas-ng)
和 [python-cas](https://github.com/python-cas/python-cas)，在此基础上进行了一定的修改，以适配东南大学的统一身份认证系统。

修改部分在代码中按照以下形式标注：

```python
# ----- MODIFIED START ----- #
# code = 'original code'
code = 'modified code'
# ----- MODIFIED END ----- #
```

## 使用 Docker 部署

### 0. 环境

- 本地
    - Docker
- 服务器
    - Docker
    - MySQL 8.0
    - Nginx

### 1. 数据库相关配置

在服务器上配置好 MySQL 数据库，并推送所需数据。

按照 [配置连接信息](#21-配置连接信息) 部分的说明，将数据库连接信息填写到 `my.cnf` 文件中。

### 2. 【本地】构建并导出镜像

```bash
# 构建镜像（在项目根目录下执行）
docker buildx build -t graduates-big-data:latest .

# 导出镜像
docker save graduates-big-data:latest > docker-img-graduates-big-data.tar
```

### 3. 【服务器】导入并运行镜像

使用 `scp` 或其他方式将导出的镜像文件传输到服务器上，然后执行以下命令：

```bash
# 导入镜像
docker load < docker-img-graduates-big-data.tar

# 运行容器
docker run -d --name graduates-big-data --network host -p 8000:8000 graduates-big-data:latest
# 或者进入容器交互模式
docker run -it --name graduates-big-data --network host -p 8000:8000 graduates-big-data:latest /bin/bash
```
