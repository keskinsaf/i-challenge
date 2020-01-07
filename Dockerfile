FROM python:3.6-alpine

MAINTAINER keskinsaf "keskinsaf@gmail.com"

# set working directory to /app
WORKDIR /app

# copy all files at the current directory into the /app in container
COPY ./ ./

# add some core libraries
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers

# add Pillow, Flask and uwsgi
RUN pip install Pillow && pip install Flask && pip install uwsgi

# run in development
# CMD ["flask", "run"]

# run in deployment
CMD ["uwsgi", "--http", ":5000", "--wsgi-disable-file-wrapper", \
     "-s", "/tmp/i-challenge.sock", "--manage-script-name", \
     "--mount", "/=app:app"]

