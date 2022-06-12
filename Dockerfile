FROM python:3.9.10-slim

RUN mkdir -p /home/app/.streamlit && mkdir -p /.u2net
WORKDIR /home/app
COPY requirements.txt streamlit_app.py download_model.py /home/app/

RUN pip install -U pip && pip install -r /home/app/requirements.txt
RUN rm -rf "$(pip cache dir)"

RUN python download_model.py

ENTRYPOINT ["streamlit", "run", "streamlit_app.py"]