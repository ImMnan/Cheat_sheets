# Workloads
Workloads Kubernetes Objects - apiVersion, Kind, metadata, and Spec.

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



