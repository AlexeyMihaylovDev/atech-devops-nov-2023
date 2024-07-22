FROM python:3.8

RUN apt update && \
    apt install -y nano

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8443

CMD ["python3", "app.py"]