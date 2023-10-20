ARG PYTORCH="1.9.0"
ARG CUDA="11.1"
ARG CUDNN="8"

FROM pytorch/pytorch:${PYTORCH}-cuda${CUDA}-cudnn${CUDNN}-devel

# To fix GPG key error when running apt-get update
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/3bf863cc.pub
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/7fa2af80.pub

RUN apt-get update && apt-get install -y git ninja-build libglib2.0-0 libsm6 libxrender-dev libxext6 libgl1-mesa-glx \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -U openmim
RUN mim install mmengine
RUN mim install 'mmcv==2.0.1'
RUN pip install 'mmdet==3.1.0'
RUN git clone https://github.com/open-mmlab/mmocr.git /mmocr
WORKDIR /mmocr
ENV FORCE_CUDA="1"
RUN pip install -r requirements.txt
RUN pip install --no-cache-dir -e .
RUN pip install -r requirements/albu.txt
RUN pip install flask psycopg2-binary openai

RUN adduser --disabled-password mckittrick

WORKDIR /home/mckittrick

USER mckittrick

COPY . .

EXPOSE 5000
#CMD [ "flask", "run","--host","0.0.0.0","--port","5000"]
