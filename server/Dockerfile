# Use Python 3.9.1
FROM python:3.9.1-slim AS development

# Build arguments to set non-root user
ARG USER_ID=1000
ARG GROUP_ID=1000

# Environment variables to configure FastAPI
ENV PYTHONPATH="/usr/src/api" \
    API_HOST="0.0.0.0" \
    API_PORT="5000" \
    API_GROUP="fastapi" \
    API_USER="fastapi" \
    API_DIR="/usr/src/api" \
    FASTAPI_ENV="development" \
    FASTAPI_APP="api.py"

# Work directory inside container
WORKDIR ${API_DIR}

# Install Python packages
ADD requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

# Add all other files to the container
ADD . .

# Create non-root user fastapi and give appropriate permissions
RUN groupadd -g ${GROUP_ID} ${API_GROUP} \
  && useradd -u ${USER_ID} -g ${API_GROUP} ${API_USER} \
  && chown ${USER_ID}:${GROUP_ID} ${API_DIR}

# Set non-root user fastapi to run FastAPI
USER ${USER_ID}:${GROUP_ID}

# Expose FastAPI to outside the container
EXPOSE ${API_PORT}

# By default, execute FastAPI
CMD uvicorn my_app.api:api --host ${API_HOST} --port ${API_PORT} --reload
