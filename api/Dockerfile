FROM python:latest

EXPOSE 5000

COPY requirements.txt .


RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /elements/proc
CMD [ "python", "index.py" ]