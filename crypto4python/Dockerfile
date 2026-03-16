FROM python
COPY task /home/task
COPY flag /flag
RUN sed -i 's/https:\/\/mirrors.aliyun.com/http:\/\/mirrors.cloud.aliyuncs.com/g' /etc/apt/sources.list
USER root
RUN apt-get update && apt-get install -y socat 
RUN pip config set global.index-url http://mirrors.aliyun.com/pypi/simple/
RUN pip config set global.trusted-host mirrors.aliyun.com
RUN pip install pycryptodome
RUN pip install gmpy2

EXPOSE 19132

CMD ["socat", "TCP4-LISTEN:19132,fork", "EXEC:\"python -u /home/task/task.py\""]