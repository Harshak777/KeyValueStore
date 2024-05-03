# KeyValueStore
A scalable Key-Value store data application that uses FastAPI for server and Redis for message queue and storage, deployed in Kubernetes

## Objective:
Develop a key-value store using Kubernetes (k8s), FastAPI, and Huey as a REDIS queue that can scale reliably across multiple pods/deployments.

### Create a kubernetes cluster
Could install minikube
```
minikube start
kubectl create namespace <namespace>
```

### Creating the redis cluster for master-slave and adding sentinel for High Availability
Kubernetes deployment details [link](https://github.com/Harshak777/kubernetes-redis)

Note:
For redis port-forwarding use the following
```
kubectl -n <namespace> port-forward <redis> 6379:6379
```

### Creating the redis cluster for master-slave and adding sentinel for High Availability
Deploy a simple redis cluster with Horizontal Pod Autoscaling 
```
kubectl -n <namespace> apply -f redis-statefulSet.yaml
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

### Deploying the KeyValueStore cluster
```
kubectl -n <namespace> apply -f kvserver-deployment.yaml
```

### Enable port-forwarding to be accessed via local machine
```
kubectl -n <namespace> port-forward svc/keyvaluestore-service 8000:8000
```

### Test using a API testing tool like postman
Available endpoints:
1. GET endoints:
    - Testing - `<host>:<port>/`
    - get the value for a key - `<host>:<port>/get/{key}`
2. POST endpoints:
    - Set the key and value pair - `<host>:<port>/set`
3. DELETE endpoints:
    - Delete a key value pair - `<host>:<port>/delete/{key}`

### Cleanup
```bash
kubectl -n <namespace> delete -f redis-statefulset.yml

kubectl -n <namespace> delete -f kvserver-deployment.yml

minikube stop
minikube delete
```
