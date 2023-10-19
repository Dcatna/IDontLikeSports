FROM python:3.9-slim

WORKDIR /app
COPY . .

ADD mainactivity.py .
ADD testJson.py .
ADD database.py .
RUN pip install requests mysql-connector-python
EXPOSE 8080

# Define environment variable
# Note: The PORT environment variable is required for Google Cloud Run
ENV PORT=8080
CMD ["python", "mainactivity.py"]