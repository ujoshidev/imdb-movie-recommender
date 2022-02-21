FROM python:3.8.4-slim

RUN pip install -U pip

COPY requirements.txt app/requirements.txt
RUN pip install -r app/requirements.txt

# copy into a directory of its own (so it isn't in the toplevel dir)
COPY . /app
WORKDIR /app

CMD ["python", "-m", "streamlit", "run", "web_interface.py", "--server.port=8080"]
EXPOSE 8080