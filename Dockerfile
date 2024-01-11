FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app

#COPY ./entrypoint.sh /entrypoint.sh

#RUN chmod +x /entrypoint.sh

#ENTRYPOINT "/entrypoint.sh"


#CMD python manage.py runserver 0.0.0.0:8000
#CMD sleep inf