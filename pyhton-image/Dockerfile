FROM python:3.9
#WORKDIR /BettingApplication/pyhton-image/mainactivity.py
COPY . .
ADD mainactivity.py .
ADD testJson.py .
ADD database.py .
RUN pip install requests mysql.connector

CMD ["python3", "mainactivity.py"]