FROM mysql

RUN apt-get update && apt-get -y install libmysqlclient-dev
RUN apt-get update && apt-get -y install libmariadbclient-dev

RUN apt-get update && apt-get -y install software-properties-common
RUN apt-get update && apt-get -y install python3 && apt-get install -y python3-pip

ADD *.py /usr/app/
ADD *.md /usr/app/
ADD Makefile /usr/app/
ADD .pylintrc /usr/app/
ADD tests/*.py /usr/app/tests/
ADD src /usr/app/src

ADD src/requirements.txt /usr/app/src/requirements.txt
RUN pip3 install -r /usr/app/src/requirements.txt

WORKDIR /usr/app/
ENTRYPOINT ["python3"]
CMD ["run_server.py"]