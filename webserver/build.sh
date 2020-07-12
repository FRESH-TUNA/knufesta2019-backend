#!/bin/sh

# migrate
docker-compose run --entrypoint="sh ./docker/common/asset_compile.sh" app
cp -r ../web/static ./
rm -rf ../web/static

# finish
docker build -t lunacircle4/knufestival2019-nginx:latest .
rm -rf ./static
