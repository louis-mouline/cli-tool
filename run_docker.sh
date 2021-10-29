#!/usr/bin/env bash

# Build image
docker build --tag=clickecho .

# List containers
docker image ls

# Run container
docker run -it clickecho python app.py --name "Louis"