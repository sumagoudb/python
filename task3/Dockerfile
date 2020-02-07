FROM python:2
RUN pip install --upgrade pip && \
    pip install --no-cache-dir gitpython

WORKDIR /work

EXPOSE 8080

CMD [ "python", "/work/task3_helloworld.py" ]