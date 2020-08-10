FROM python:3.6 
ENV PYTHONUNBUFFERED 1 
ADD ./requirements.txt /requirements.txt 
RUN pip install -U pip && 
LIBRARY_PATH=/lib:/usr/lib /bin/sh -c "pip install -r /requirements.txt --no-cache-dir" RUN mkdir /code WORKDIR /code ADD ./src . 
EXPOSE 8000