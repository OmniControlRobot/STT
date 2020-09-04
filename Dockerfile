FROM hyeonwoong/stt-base-model

WORKDIR /app

COPY requirements.txt /app

# RUN apt-get install update
RUN apt-get install llvm -y
RUN apt-get install libsndfile1-dev -y
RUN pip install -r requirements.txt 
RUN apt-get install sox -y

COPY . /app

CMD ["python3", "server.py"]
