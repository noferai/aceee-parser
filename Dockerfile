FROM python:3.7-slim
COPY . .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
CMD scrapy crawl aceee