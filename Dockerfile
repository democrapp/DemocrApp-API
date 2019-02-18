FROM python:3
WORKDIR /srv/api
ADD requirements.txt /srv/api
RUN pip install -r requirements.txt
ADD . /srv/api
CMD ["python", "-V"]
