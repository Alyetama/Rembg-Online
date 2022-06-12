#!/bin/bash

echo | docker-slim build \
	--http-probe=false \
	--preserve-path=/usr/local/lib/python3.9 \
	--preserve-path=/.u2net \
	--tag=rembg-app-slim \
	rembg-app
