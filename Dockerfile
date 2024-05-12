FROM --platform=$BUILDPLATFORM python:3.9-bookworm

EXPOSE 8000

WORKDIR /app

# Timezone
ENV TZ=China/Shanghai

# RUN apt update && apt install -y vim

# Install dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
RUN pip install -r requirements.txt --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple some-package

# Start the application
CMD ["uwsgi", "--ini", "uwsgi.ini"]