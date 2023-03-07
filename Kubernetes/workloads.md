# Workloads
Workloads Kubernetes Objects - apiVersion, Kind, metadata, and Spec.

-----------------------------------------------------------------
## Pod

```bash
kubectl api-resources

kubectl explain pod.spec.containers
kubectl explain pod.spec.containers [--]recursive
```
Checkout [cheatsheet](cheatsheet.md) to know more about the commands that can be run to manage the pods.
Navigate to the pods section to get details about deployment commands.


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
Any manifest placed into this directory will be owned by kubelet and it will run the manifests. Any changes made to the maifest yamls in this directory will be real time, no restarts needed.

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
Navigate to the Deployment section to get details about deployment commands.


## Daemon Set



```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: fluentd-elasticsearch
  namespace: kube-system
  labels:
    k8s-app: fluentd-logging
spec:
  selector:
    matchLabels:
      name: fluentd-elasticsearch
  template:
    metadata:
      labels:
        name: fluentd-elasticsearch
    spec:
      tolerations:
      # this toleration is to have the daemonset runnable on master nodes
      # remove it if your masters can't run pods
      - key: node-role.kubernetes.io/master
        operator: Exists
        effect: NoSchedule
      containers:
      - name: fluentd-elasticsearch
        image: quay.io/fluentd_elasticsearch/fluentd:v2.5.2
        resources:
          limits:
            memory: 200Mi
          requests:
            cpu: 100m
            memory: 200Mi
        volumeMounts:
        - name: varlog
          mountPath: /var/log
        - name: varlibdockercontainers
          mountPath: /var/lib/docker/containers
          readOnly: true
      terminationGracePeriodSeconds: 30
      volumes:
      - name: varlog
        hostPath:
          path: /var/log
      - name: varlibdockercontainers
        hostPath:
          path: /var/lib/docker/containers
```
For complete Commands for daemonset see [cheatsheet](cheatsheet.md)
```bash
kubectl apply -f https://k8s.io/examples/controllers/daemonset.yaml
kubectl get ds
kubectl describe ds fluentd-elasticsearch
kubectl get pods -o wide | grep fluentd
```

## Jobs
```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: pi
spec:
  template:
    spec:
      containers:
      - name: pi
        image: busybox:1.28
        imagePullPolicy: IfNotPresent
        command:
            - /bin/sh
            - -c
            - date; echo Hello from the Kubernetes cluster
      restartPolicy: Never
  backoffLimit: 4
```
```bash
kubectl apply -f job.yaml 
kubectl describe jobs/pi pods=$(kubectl get pods --selector=job-name=pi --output=jsonpath='{.items[*].metadata.name}')
echo $pods 
kubectl logs $pods
```

## CronJobs
```bash
wget https://k8s.io/examples/application/job/cronjob.yaml
Note: Change version in yaml
kubectl create -f cronjob.yaml
kubectl get cronjob hello
kubectl get jobs -w
kubectl delete -f cronjob.yaml
```

Configuration basics

Introduction:
All JAVA Spring Configuration item
MySQL DB Configuration


## Env

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: envar-demo
  labels:
    purpose: demonstrate-envars
spec:
  containers:
  - name: envar-demo-container
    image: gcr.io/google-samples/node-hello:1.0
    env:
    - name: DEMO_GREETING
      value: "Hello from the environment"
    - name: DEMO_FAREWELL
      value: "Such a sweet sorrow"
```
```bash
kubectl apply -f https://k8s.io/examples/pods/inject/envars.yaml
kubectl get pods -l purpose=demonstrate-envars

kubectl exec envar-demo -- printenv
```

## ConfigMaps
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: game-demo
data:
  # property-like keys; each key maps to a simple value
  player_initial_lives: "3"
  ui_properties_file_name: "user-interface.properties"

  # file-like keys
  game.properties: |
    enemy.types=aliens,monsters
    player.maximum-lives=5    
  user-interface.properties: |
    color.good=purple
    color.bad=yellow
    allow.textmode=true  
```
```bash
kubectl describe cm game-demo
```

Using Env
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: dapi-test-pod01
spec:
  containers:
    - name: test-container
      image: k8s.gcr.io/busybox
      command: [ "/bin/sh", "-c", "env" ]
      env:
        - name: LIVES
          valueFrom:
            configMapKeyRef:
              name: game-demo
              key: player_initial_lives
        - name: FILE_NAME
          valueFrom:
            configMapKeyRef:
              name: game-demo
              key: ui_properties_file_name
  restartPolicy: Never
```

Using EnvFrom
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: dapi-test-pod02
spec:
  containers:
    - name: test-container
      image: k8s.gcr.io/busybox
      command: [ "/bin/sh", "-c", "env" ]
      envFrom:
      - configMapRef:
          name: game-demo
  restartPolicy: Never
```


## Secrets
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: mysecret
type: kubernetes.io/basic-auth
stringData:
  username: admin
  password: t0p-Secret
---
apiVersion: v1
kind: Pod
metadata:
  name: secret-env-pod
spec:
  containers:
  - name: mycontainer
    image: redis
    env:
      - name: SECRET_USERNAME
        valueFrom:
          secretKeyRef:
            name: mysecret
            key: username
      - name: SECRET_PASSWORD
        valueFrom:
          secretKeyRef:
            name: mysecret
            key: password
  restartPolicy: Never
```
```bash
kubectl exec -it secret-env-pod env
```