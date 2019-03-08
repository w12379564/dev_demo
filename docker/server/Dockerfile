FROM python

WORKDIR /server

COPY . /server

RUN pip install Flask

EXPOSE 80

CMD ["python", "server.py"]