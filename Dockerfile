FROM python:3.10

WORKDIR /car
COPY . /car

RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates wget unzip && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb && apt-get clean && \
    curl -fsSL https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin/:$PATH"

RUN uv venv
RUN . .venv/bin/activate && uv sync

ENV AM_I_IN_A_DOCKER_CONTAINER=Yes

CMD ["/car/.venv/bin/python", "main.py"]
