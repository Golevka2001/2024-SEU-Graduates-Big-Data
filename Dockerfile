FROM --platform=$BUILDPLATFORM python:3.9-bookworm

EXPOSE 8000

WORKDIR /app

COPY ./requirements.txt /app
COPY ./graduates_big_data /app

RUN pip install -r requirements.txt --no-cache-dir

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]