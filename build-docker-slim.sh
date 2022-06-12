#!/bin/bash

export DOCKER_BUILDKIT=1

docker build . --tag rembg-app

echo | docker-slim build \
	--http-probe=false \
	--preserve-path=/usr/local/lib/python3.9 \
	--preserve-path=/.u2net \
	rembg-app
