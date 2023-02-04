FROM python:3.9.16-alpine3.17
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN mkdir /books

WORKDIR /books
ADD requirements.txt /temp/requirements.txt
RUN pip install -r /temp/requirements.txt
COPY books /books
EXPOSE 8000