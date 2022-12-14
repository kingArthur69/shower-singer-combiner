# start by pulling the python image
FROM python:3.8

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN apt-get update && apt-get install -y ffmpeg && pip install --no-deps -r requirements.txt
RUN bash -c 'mkdir {combined,download,separated}'

# copy every content from the local file to the image
COPY . /app

EXPOSE 5000

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["app.py" ]