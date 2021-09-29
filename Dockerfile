FROM python:alpine 
WORKDIR /code
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 192.168.80.30
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["flask", "run"]
