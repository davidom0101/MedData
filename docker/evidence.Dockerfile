FROM node:22-slim

WORKDIR /app

# no evidence project yet, just proves node image builds
CMD ["node", "--version"]
