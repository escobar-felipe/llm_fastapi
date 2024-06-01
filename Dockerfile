FROM python:3.10-slim-buster

RUN apt-get -y update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    curl \
    git-lfs \
    python3-dev \
    gcc && \
    apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y libreoffice  # needed to load .doc and other MS files
RUN apt-get install tesseract-ocr -y && apt-get install poppler-utils  # needed for image pdf

WORKDIR /opt/app/

RUN pip install --upgrade pip
COPY src/requirements.txt /opt/app/requirements.txt

RUN pip --no-cache-dir install -r requirements.txt

ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH "/opt/app:${PATH}"

COPY src/ /opt/app/
COPY ops/ /opt/ops/

EXPOSE 8081

CMD [ "bash", "start.sh" ]
