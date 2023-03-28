# Base image
FROM python:3.9

# # Set environment variables
# ENV PYTHONUNBUFFERED 1
# ENV NODE_VERSION 14.x

# # Install dependencies
# RUN apt-get update \
#     && apt-get install -y --no-install-recommends \
#     curl \
#     nodejs \
#     npm \
#     gettext \
#     libpq-dev \
#     && rm -rf /var/lib/apt/lists/*

# # Install Node.js
# RUN curl -sL https://deb.nodesource.com/setup_$NODE_VERSION | bash -

# # Upgrade npm
# RUN npm install -g npm

# # Install Python dependencies
# RUN pip install --upgrade pip
# COPY ./requirements.txt /app/requirements.txt
# WORKDIR /app
# RUN pip install -r requirements.txt

# # Set up the app directory
# RUN mkdir -p /app/frontend
# WORKDIR /app/frontend

# # Install frontend dependencies
# COPY ./frontend/package.json /app/frontend/package.json
# COPY ./frontend/package-lock.json /app/frontend/package-lock.json
# RUN npm install

# # Copy the app code
# WORKDIR /app
# COPY . /app

# # Start the development server
# CMD ["./start_dev.sh"]
