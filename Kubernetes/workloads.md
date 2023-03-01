# Workloads
Workloads Kubernetes Objects - apiVersion, Kind, metadata, and Spec.

-----------------------------------------------------------------
## Pod

```bash
kubectl api-resources

kubectl explain pod.spec.containers
kubectl explain pod.spec.containers [--]recursive
```

### One-container-per-Pod
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:

  containers:
  - name: nginx
    image: nginx:1.14.2
    ports:
    - containerPort: 80
```

### Multi-container-pod
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: multicontainer-pods
  labels:
    app: httpd
    tier: frontend-backend
    version: v1
spec:
  containers:
  #Container 01
  - name: web
    image: httpd
    ports:
    - containerPort: 80
  #Container 02
  - name: redis
    image: redis
```

### Init Container
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: purple
spec:
  containers:
    - command:
        - sh
        - -c
        - echo The app is running! && sleep 3600
      image: busybox:1.28
      name: purple-container
  # Adding 2 init containers to execute sleep commands
  initContainers:
    - command:
        - sh
        - -c
        - sleep 60
      image: busybox:1.28
      name: warm-up-1
    - command: ["sh", "-c", "sleep 120"]
      image: busybox:1.28
      name: warm-up-2
```
Watch the init container-
```
kubectl get pods -w
```

### Static-Pod
```bash
cd /etc/kubernetes/manifests
ls -l
```

create a yaml file:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: static-web
  labels:
    role: myrole
spec:
  containers:
    - name: web
      image: nginx
      ports:
        - name: web
          containerPort: 80
          protocol: TCP
```

In the master node:
```bash
kubeclt get pods -A
```
The pod will appear in default namespace, delete the static pod file in worker01
Run the following in the master node:
```bash
kubectl get pods -A
```
The pod will Disappear in default namespace


### Resource limits

Set resource limits or requests for a pod

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: rl-pod
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    ports:
    - containerPort: 80
    resources:
      requests: # Minimum Value        
        memory: "100Mi"
        cpu: "250m" # 1 core = 1000m
      limits:  # Maximum Value         
        memory: "128Mi"
        cpu: "300m"
```
------------------------------------------------------------------------------------------------------------
## Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
```

```bash
kubectl get deployments
kubectl rollout status deployment/nginx-deployment
kubectl get rs
kubectl get pods --show-labels
```

Checkout [cheatsheet](cheatsheet.md) to know more about the commands that can be run to manage the deployment.
