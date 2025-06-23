FROM gitpod/workspace-full

# Install Python 3.10.11 and required system packages
RUN sudo apt update && \
    sudo apt install -y make build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
    libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev \
    libffi-dev liblzma-dev && \
    pyenv install 3.10.11 && \
    pyenv global 3.10.11
