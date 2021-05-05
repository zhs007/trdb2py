docker build -f ./Dockerfile.dev -t trdb2py.dev .
docker rm trdb2py.dev
docker run -d --name trdb2py.dev trdb2py.dev pytest