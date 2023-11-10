# Use the official GDAL image as the base image
FROM osgeo/gdal:ubuntu-small-latest

# install pip
RUN apt-get update && apt-get -y install python3-pip --fix-missing

# install poetry
RUN pip3 install poetry

# Set the working directory in the container
WORKDIR /app

# --- Install all poetry dependencies ---
# copy .toml and .lock files)
# set virtualenvs.create to false, gdal image already comes with a virtualenv
# --no root prevents poetry from using root privileges.
# Poetry is only able to install depedences in the current venv.
# More secure and isolated
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false
RUN poetry install --no-root
# ---------------------------------------

RUN mkdir -p /app/notebooks

EXPOSE 8888

# Change path to Python environment
RUN export PATH="/app/venv/bin:$PATH"

CMD ["jupyter", "notebook", "--"]
