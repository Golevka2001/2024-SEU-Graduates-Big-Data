# 2024-SEU-Graduates-Big-Data

## 开发

### 0. 环境

- Python 3.9
- MySQL 8.0

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

_注：安装依赖前请确保本地 MySQL Client 已配置完成_

### 2. 配置数据库

创建数据库（本地或远程均可），并在项目根目录下创建 `my.cnf` 文件，内容如下：

```ini
[client]
database = database_name
user = username
password = P4ssw0rd
host = 127.0.0.1
port = 3306
default-character-set = utf8
```

_注：请按照实际情况填写上述各字段_

### 3. 启动服务器

```bash
python manage.py runserver
```
