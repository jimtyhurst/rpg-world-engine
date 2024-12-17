FROM mcr.microsoft.com/vscode/devcontainers/base:ubuntu

# use this Dockerfile to install additional tools you might need, e.g.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>

# uv to manage Python dependencies.
# TODO: uv is *not* available in Terminal after workspace starts ... Why?
RUN curl -LsSf https://astral.sh/uv/install.sh | sh \
    && uv venv --python 3.13 \
    && uv sync
