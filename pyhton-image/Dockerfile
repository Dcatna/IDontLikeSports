FROM python:3.9-slim

WORKDIR /app
COPY . .
RUN pip install flask requests mysql-connector-python pytz

EXPOSE 8080
ENV PORT=8080
CMD ["python", "mainactivity.py"]
