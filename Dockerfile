FROM python:3.9.7

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENV HAFIFA=True

COPY . .

ENTRYPOINT ["python", "main.py"]