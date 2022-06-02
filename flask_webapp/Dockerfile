# start by pulling the python image
FROM python:3.8-alpine

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

RUN apk update
RUN apk add build-base
    
# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt
# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["view.py" ]




# Testing environment for AIOHappyBase
# FROM aiudirog/hbase:latest

# RUN apt-get update
# RUN apt-get install -y software-properties-common
# RUN apt-get update
# RUN add-apt-repository ppa:deadsnakes/ppa -y
# RUN apt-get update
# RUN apt-get install -y \
#     'python3.6' 'python3.7' 'python3.8' 'python3.9' \
#     'python3.6-dev' 'python3.7-dev' 'python3.8-dev' 'python3.9-dev' \
#     python3-pip net-tools git