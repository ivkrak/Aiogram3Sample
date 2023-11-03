FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN mkdir src
COPY run.py .
COPY src ./src
CMD ["python3", "run.py"]