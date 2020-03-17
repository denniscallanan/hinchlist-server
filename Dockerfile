FROM python:3.7-alpine

ADD src/requirements.txt /usr/app/src/requirements.txt

RUN pip install --upgrade pip && pip install -r /usr/app/src/requirements.txt

ADD *.py /usr/app/
ADD *.md /usr/app/
ADD Makefile /usr/app/
ADD .pylintrc /usr/app/
ADD tests/*.py /usr/app/tests/
ADD src /usr/app/src

WORKDIR /usr/app/
ENTRYPOINT ["python3"]
CMD ["run_server.py"]