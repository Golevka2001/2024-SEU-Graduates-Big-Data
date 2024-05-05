FROM --platform=$BUILDPLATFORM python:3.9-bookworm

EXPOSE 8000

WORKDIR /app

COPY . /app

# RUN apt update && apt install -y vim
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]