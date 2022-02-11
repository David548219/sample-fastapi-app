FROM python:3.9
WORKDIR /sample-fastapi-app
COPY ./requirements.txt /sample-fastapi-app/requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r /sample-fastapi-app/requirements.txt
COPY ./app /sample-fastapi-app/app
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
