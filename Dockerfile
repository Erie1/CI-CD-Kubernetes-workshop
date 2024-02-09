FROM python:3.11-slim

WORKDIR /workdir

copy . /workdir

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5005"]

EXPOSE 5005