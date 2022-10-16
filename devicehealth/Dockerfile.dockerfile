FROM MySQL:latest

COPY app.py /app.py

CMD [ "python", "./app.py" ]
