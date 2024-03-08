FROM python:alpine
WORKDIR /app
COPY flask_score.py scores.txt index.html ./
RUN pip install flask
EXPOSE 5000
CMD python flask_score.py
