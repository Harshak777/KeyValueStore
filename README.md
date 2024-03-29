# KeyValueStore
A scalable Key-Value store data application that uses FastAPI for server and Redis for message queue and storage,, deployed in Kubernetes

## Objective:
Develop a key-value store using Kubernetes (k8s), FastAPI, and Huey as a REDIS queue that can scale reliably across multiple pods/deployments.

### Creating the redis cluster
Kubernetes deployment details [link](https://github.com/Harshak777/kubernetes-redis)

Note:
For port-forwarding use the following
```
kubectl -n redis port-forward redis-0 6379:6379
```

### App
Activate virtual environment(Optional)
```
python3 -m venv key_store
source key_store/bin/activate
```
Install python requirements
```
pip install -r requirements.txt
```
Run FastAPI using uvicorn(ASGI server for python)
```
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
Start huey consumer
```
python3 huey_consumer.py services.huey
```
Optional step
Build and push the Docker image
```
docker build . -t kharshak777/key-value-server
docker push kharshak777/key-value-server
```