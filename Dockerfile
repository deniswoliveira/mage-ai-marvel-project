FROM mageai/mageai:latest

ARG PROJECT_NAME=marvel_api
ARG MAGE_CODE_PATH=/home/src

WORKDIR ${MAGE_CODE_PATH}

# Replace [project_name] with the name of your project (e.g. demo_project)
COPY ${PROJECT_NAME} ${PROJECT_NAME}
COPY ./secrets /home/secrets

# Install custom Python libraries
COPY marvel_api/marvel_api/requirements.txt .
RUN pip3 install -r requirements.txt

ENV PYTHONPATH="${PYTHONPATH}:/home/src"

CMD ["/bin/sh", "-c", "/app/run_app.sh"]