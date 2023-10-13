FROM python:3.9

COPY . .
ADD mainactivity.py .
ADD testJson.py .
ADD database.py .
RUN pip install requests mysql-connector-python

CMD ["python3", "mainactivity.py"]