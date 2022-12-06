FROM python:3.8-slim

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN python -m pip install --upgrade pip && pip3 install -r requirements.txt --no-cache-dir

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]