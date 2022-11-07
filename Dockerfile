FROM python:3.9

WORKDIR /app

COPY ["requirements.txt", "./"]

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY ["app.py", "pickle_model.pkl", "./"]

EXPOSE 8000

ENTRYPOINT ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"] 
