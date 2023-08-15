FROM python:3.10.9-alpine

RUN mkdir -p /code

WORKDIR /code

COPY ews_calculator.py .
COPY test-deploy/setup_repo.py .
COPY test-deploy/run.sh .
COPY test-deploy/requirements.txt .
COPY test-deploy/repo-config.ttl .
COPY test-deploy/orgA.ttl .
COPY test-deploy/orgB.ttl .
COPY test-deploy/full_ews.owl .
COPY test-deploy/uo.owl .

RUN pip install -r requirements.txt

RUN chmod +x run.sh

ENTRYPOINT ["./run.sh"]
