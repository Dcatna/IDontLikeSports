FROM python:3.9-slim

COPY . .
ADD mainactivity.py .
ADD testJson.py .
ADD database.py .
RUN pip install requests mysql-connector-python
EXPOSE 8080
CMD ["python3", "mainactivity.py"]