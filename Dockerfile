FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip==23.3.1
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "plant_project.wsgi:application", "--bind", "0.0.0.0:8000"]