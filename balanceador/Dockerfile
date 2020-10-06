FROM python:latest

EXPOSE 5000

COPY requirements.txt .


RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "index.py" ]