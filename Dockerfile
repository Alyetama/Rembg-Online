FROM python:3.9.9-slim

RUN mkdir -p /home/app/.streamlit

WORKDIR /home/app

COPY requirements.txt /home/app
COPY streamlit_app.py /home/app
COPY .streamlit/config.toml /home/app/.streamlit

RUN pip install -r /home/app/requirements.txt
