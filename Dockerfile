FROM python:3.11-slim

WORKDIR /app
# Copy the requirements file into the container
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8888

CMD [ "python", "run.py" ]
