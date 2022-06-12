FROM python:3.9.10-slim

RUN mkdir -p /home/app/.streamlit

WORKDIR /home/app

COPY requirements.txt streamlit_app.py /home/app/

RUN pip install -U pip
RUN pip install -r /home/app/requirements.txt

RUN mkdir -p /root/.u2net
RUN python -c 'from urllib import request; request.urlretrieve("https://github.com/Alyetama/Rembg-Online/releases/download/v0.0.0/u2net.onnx", "/root/.u2net/u2net.onnx")'
