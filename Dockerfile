From python:3.6.4-slim-jessie

#install cherrpy
RUN pip install cherrypy==11.0
RUN pip install yacs==0.1.8
RUN pip install requests

WORKDIR /webservice
ADD config.yaml .
ADD *.py .



# Start web service
ENTRYPOINT ["python", "/webservice/webservice.py"]
CMD ["--logLevel", "INFO"]
