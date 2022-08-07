#Dockerfile, image, container

FROM python:3.8-slim-buster
ADD . /project_fast_api
WORKDIR /project_fast_api
RUN pip3 install -r requirements.txt
CMD [ "python3", "./main.py"]