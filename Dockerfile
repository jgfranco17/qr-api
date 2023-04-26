FROM python:3.11.0a6-alpine3.15
RUN sudo apt-get update && sudo apt-get install -y python3-pip 
WORKDIR /api
COPY requirements.txt /api
RUN pip install -r requirements.txt --no-cache-dir
COPY . /api
CMD python app.py --port 5050