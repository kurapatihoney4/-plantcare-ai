FROM python:3.10-slim

WORKDIR /app

# ✅ system dependencies required for tensorflow + opencv
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

COPY . /app

# upgrade pip tools
RUN pip install --upgrade pip setuptools wheel

# install python dependencies
RUN pip install -r requirements.txt

EXPOSE 8000

# IMPORTANT: bind to correct port for Render
CMD ["gunicorn", "plant_project.wsgi:application", "--bind", "0.0.0.0:8000"]