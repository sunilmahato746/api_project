FROM python:alpine
WORKDIR /opt

COPY ./requirements.txt ./

RUN pip install -r /opt/requirements.txt

COPY ./ ./

CMD ["python","/opt/main.py"]