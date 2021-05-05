docker build -f ./Dockerfile.dev -t trdb2py.dev .
docker rm trdb2py.dev
docker run -d -v $PWD/trdb2py:/src/trdb2py/trdb2py --name trdb2py.dev trdb2py.dev python -m grpc_tools.protoc --python_out=trdb2py/ --grpc_python_out=trdb2py/ -I=protos/ protos/*.proto