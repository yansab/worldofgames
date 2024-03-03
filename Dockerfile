FROM python:alpine
COPY flask_score.py scores.txt index.html .
RUN pip install flask
EXPOSE 5000
CMD python flask_score.py
    