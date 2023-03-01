---
title: kubectl Cheat Sheet
reviewers:
- erictune
- krousey
- clove
content_type: concept
weight: 10 # highlight it
card:
  name: reference
  weight: 30
---

<!-- overview -->

This page contains a list of commonly used `kubectl` cmds and flags.

<!-- body -->

## Kubectl autocomplete

### BASH

```bash
source <(kubectl completion bash) # set up autocomplete in bash into the current shell, bash-completion package should be installed first.
echo "source <(kubectl completion bash)" >> ~/.bashrc # add autocomplete permanently to your bash shell.
```

You can also use a shorthand alias for `kubectl` that also works with completion:

```bash
alias k=kubectl
complete -o default -F __start_kubectl k
```

### ZSH

```bash
source <(kubectl completion zsh)  # set up autocomplete in zsh into the current shell
echo '[[ $cmds[kubectl] ]] && source <(kubectl completion zsh)' >> ~/.zshrc # add autocomplete permanently to your zsh shell
```
### A note on `--all-namespaces`

Appending `--all-namespaces` happens frequently enough where you should be aware of the shorthand for `--all-namespaces`:

```kubectl -A```

## Kubectl context and configuration

Set which Kubernetes cluster `kubectl` communicates with and modifies configuration
information. See [Authenticating Across Clusters with kubeconfig](/docs/tasks/access-application-cluster/configure-access-multiple-clusters/) documentation for
detailed config file information.

```bash
kubectl config view # Show Merged kubeconfig settings.

# use multiple kubeconfig files at the same time and view merged config
KUBECONFIG=~/.kube/config:~/.kube/kubconfig2

kubectl config view

# get the password for the e2e user
kubectl config view -o jsonpath='{.users[?(@.name == "e2e")].user.password}'

kubectl config view -o jsonpath='{.users[].name}'    # display the first user
kubectl config view -o jsonpath='{.users[*].name}'   # get a list of users
kubectl config get-contexts                          # display list of contexts
kubectl config current-context                       # display the current-context
kubectl config use-context my-cluster-name           # set the default context to my-cluster-name

kubectl config set-cluster my-cluster-name           # set a cluster entry in the kubeconfig

# configure the URL to a proxy server to use for requests made by this client in the kubeconfig
kubectl config set-cluster my-cluster-name --proxy-url=my-proxy-url

# add a new user to your kubeconf that supports basic auth
kubectl config set-credentials kubeuser/foo.kubernetes.com --username=kubeuser --password=kubepassword

# permanently save the namespace for all subsequent kubectl cmds in that context.
kubectl config set-context --current --namespace=ggckad-s2

# set a context utilizing a specific username and namespace.
kubectl config set-context gce --user=cluster-admin --namespace=foo \
  && kubectl config use-context gce

kubectl config unset users.foo                       # delete user foo

# short alias to set/show context/namespace (only works for bash and bash-compatible shells, current context to be set before using kn to set namespace) 
alias kx='f() { [ "$1" ] && kubectl config use-context $1 || kubectl config current-context ; } ; f'
alias kn='f() { [ "$1" ] && kubectl config set-context --current --namespace $1 || kubectl config view --minify | grep namespace | cut -d" " -f6 ; } ; f'
```

## Kubectl apply

`apply` manages applications through files defining Kubernetes resources. It creates and updates resources in a cluster through running `kubectl apply`. This is the recommended way of managing Kubernetes applications on production. See [Kubectl Book](https://kubectl.docs.kubernetes.io).

## Creating objects

Kubernetes manifests can be defined in YAML or JSON. The file extension `.yaml`,
`.yml`, and `.json` can be used.

```bash
kubectl apply -f ./my-manifest.yaml            # create resource(s)
kubectl apply -f ./my1.yaml -f ./my2.yaml      # create from multiple files
kubectl apply -f ./dir                         # create resource(s) in all manifest files in dir
kubectl apply -f https://git.io/vPieo          # create resource(s) from url
kubectl create deployment nginx --image=nginx  # start a single instance of nginx

# create a Job which prints "Hello World"
kubectl create job hello --image=busybox:1.28 -- echo "Hello World"

# create a CronJob that prints "Hello World" every minute
kubectl create cronjob hello --image=busybox:1.28   --schedule="*/1 * * * *" -- echo "Hello World"

kubectl explain pods                           # get the documentation for pod manifests

# Create multiple YAML objects from stdin
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: busybox-sleep
spec:
  containers:
  - name: busybox
    image: busybox:1.28
    args:
    - sleep
    - "1000000"
---
apiVersion: v1
kind: Pod
metadata:
  name: busybox-sleep-less
spec:
  containers:
  - name: busybox
    image: busybox:1.28
    args:
    - sleep
    - "1000"
EOF

# Create a secret with several keys
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Secret
metadata:
  name: mysecret
type: Opaque
data:
  password: $(echo -n "s33msi4" | base64 -w0)
  username: $(echo -n "jane" | base64 -w0)
EOF

```
-------------------------------------------------------------------------------------------------------------------------------------------------------------

## Viewing/listing/updating and deleting  resources [CRUD]

### Node - Resource type

```bash
kubectl get nodes                            # List all nodes in the cluster
kubectl get nodes -w                         # Watch the nodes
kubectl get nodes -o wide                    # wide view along with the IP(internal/external), OS-image, Kernerl, Container-runtime
kubectl get nodes -o yaml                    # Prints out the yaml manifests including detailed node information
kubectl get nodes --show-labels              # Show all labels associated with the nodes
kubectl top nodes <node_name>                # The top-node cmd allows you to see the resource consumption of nodes.
```

### Pods - Resource type [CRUD]
- Read:
```bash
kubectl get pods                              # List all pods in the default namespace
kubectl get pods -o wide                      # List the pods in a wide view - [IP, Node, Nominated Node, etc.]
kubectl get pod <pod_name> -o yaml            # Get a pod's YAML
kubectl describe pod <pod_name>               # Describe the pod details
kubectl get pods --show-labels                # Show all labels associated with the pod
kubectl get pods -w                           # watch the all  pods, we can watch a specific pod with adding pod_name after 'pods'
kubectl logs <pod_name>                       # Return snapshot logs from pod <pod_name> with only one container
kubectl logs <pod_name> --all-container=true  # Return snapshot logs from pod <pod_name> with multi-container
kubectl logs -c <container> <pod_name>        # Return snapshot logs for <container> in the pod <pod_name>
kubectl logs -f <pod_name>                    # Begin streaming the logs, use -f with other cmds as well when straming is needed.
kubectl logs -f <pod_name> --tail=5:          # Tail the log lines of recent log file to display.
kubectl top pods <pod_name>                   # The top cmd allows you to see the resource [cpu/memory] consumption.
kubectl set env pods --all --list             # List the environment variables defined on all pods
kubectl set env pods <pod_name> --list        # List the environment variables defined on a specific pod
```
- Create + Update:

Note: below cmds are for default namespace, please specify your namespace as required (see further filtering).
```bash
kubectl exec <pod_name> -- <cmd>                         # run a cmd on a container - pod with single container
kubectl exec <pod_name> -c <container> -- <cmd>          # run a cmd on a specific container - pod with multi-container
kubectl edit pod <pod_name>                              # Edit the existing pod's yaml
kubectl label pod <pod_name> <key1>=<value1>             # Update pod <pod_name> with the label.
kubectl label --overwrite pod <pod_name> <key1>=<value2> # Update pod <pod_name> with the label, overwriting any existing value
kubectl label pods --all <key1>=<value1>                 # Update all pods in the namespace
kubectl cp /tmp/foo_dir <pod_name>:/tmp/bar_dir          # Copy /tmp/foo_dir local directory to /tmp/bar_dir in a remote pod in the default namespace
kubectl cp <namespace>/<pod_name>:/tmp/foo /tmp/bar      # Copy /tmp/foo from a remote pod to /tmp/bar locally
kubectl set image pod/<pod_name> nginx=nginx:latest      # Update existing container image of a pod, nginx is a container-name, followed by image:version
kubectl set image pod/<pod_name> *=nginx:latest          # Update all containers of this pod, nginx is a container-name, followed by image:version
kubectl annotate pods <pod_name> description='test'      # Update pod <pod_name> with the annotation 'description' and the value as 'test'
kubectl attach <pod_name>                                # Get output from running pod
kubectl attach <pod_name> -c <container_name>            # Get output from a container in a running pod
```

-  Delete:
```bash
kubectl delete pod <pod_name>               # Deletes the pod
kubectl label pod <pod_name> <key1>-        # Remove a label named <key1> if it exists. *No overwrite option needed.
```

> Further fitering options [ -A, -n, -l ] with examples:

These options can be used with the above cmds as and when required.
```bash
kubectl get pods -A                     # Lister pods across all namespaces.
kubectl get pods -n <namespace>         # Using namespace, we can use -n with all other cmds to point to resources in a specific namespace.
kubectl get pods -l <key1>=<value1>     # Using labels key1=value1 are the labels,  Matching objects must satisfy all of the specified label constraints
```

### Deployment + Replica Set - Resource type [CRUD]

- Read:
```bash
kubectl get deploy                         # List all deployment  in the default namespace
kubectl get deploy -o wide                 # List the deployment in a wide view - [Containers, Images, Selector]
kubectl get deploy <name> -o yaml          # Get a deployment's YAML
kubectl describe deploy <name>             # Describe the deployment details
kubectl get deploy --show-labels           # Show all labels associated with the deployment
kubectl get deploy -w                      # watch the all deployments, we can watch a specific deployment  with adding deployment name after 'deploy'
kubectl rollout history deploy/<name>      # View the rollout history of a deployment
kubectl rollout status deploy/<name>       # Check the status of your rollout.
kubectl set env deploy --all --list        # List the environment variables defined on all deployment
kubectl set env deploy/<name> --list       # List the environment variables defined on all deployment
kubectl logs -f deploy/<name> --tail=5:    # Tail the log lines of recent log file to display.
kubectl logs deploy/name -c nginx
```

- Create + Update:
```bash
kubectl exec deploy/<name> -- <cmd>                          # Run a cmd on the 1st pod of the deployment, 1st container by default is used.
kubectl exec deploy/<name> -c nginx -- <cmd>                 # Run a cmd on nginx container in the deployment <name>
kubectl edit deploy <name>                                   # Edit the existing deployment's yaml
kubectl label deploy/<name> <key>=<value>                    # Update <name> with the label.
kubectl label --overwrite deploy/<name> <key>=<value2>       # Update <name> with the label, overwriting any existing value
kubectl rollout undo deploy/<name>                           # Rollback to the previous deployment.
kubectl rollout undo deploy/<name> --to-revision=2           # Rollback to revision 2 of from the  previous deployment history
kubectl rollout restart deploy/<name>                        # Restart a deployment
kubectl rollout pause deploy/<name>                          # New updates to the deployment will not have an effect as long as this is paused
kubectl rollout resume deploy/<name>                         # Resume an already paused deployment
kubectl set env deploy/<name> env_var=test                   # Update deployment with a new env name 'env_var'='test'
kubectl set env --from=configmap/<name> deploy/<name>        # Import environment from a configmap 
kubectl set env --from=secret/<name> deploy/<name>           # Import environment from a secret
kubectl set image deploy/<name> nginx=nginx:latest           # Set a deployment's nginx container image to 'nginx:latest'
kubectl set image deploy/<name> *=nginx:1.14.2               # Update image of all containers of deployment to 'nginx:1.14.2'
kubectl set resources deploy/<name> -c nginx --limits=cpu=250m,memory=512Mi   # Set a deployments nginx container cpu limits to "200m" and memory to "512Mi" 
kubectl set resources deploy/<name> -c nginx --requests=cpu=250m,memory=512Mi # Set a deployments nginx container cpu requests to "200m" and memory to "512Mi" 
kubectl scale --replicas=3 deploy/<name>                     # Scale a replica set to 3, can scal̥le up or down
kubectl annotate deploy <name> description='test'            # Added nnotation, though we recommend adding these in the yaml for deployment.
kubectl autoscale deploy/<name> --min=2 --max=5 --cpu-percent=50              # Auto scalling - though we recommend creating a yaml for autoscaling.
kubectl attach deploy/<name>                                 # Get output from the first pod of a deployment
```

-  Delete:
```bash
kubectl delete deploy  <name>              # Deletes the deployment
kubectl label deploy <name> <key1>-        # Remove a label named <key1> if it exists. *No overwrite option needed.
```

> Further fitering options [ -A, -n, -l ] with examples:

These options can be used with the above cmds as and when required.
```bash
kubectl get deploy -A                            # Lister Deployments  across all namespaces.
kubectl get deploy -n <namespace>                # Using namespace, we can use -n with all other cmds to point to resources in a specific namespace.
kubectl get deploy -l <key1>=<value1>            # Using labels key1=value1, matching objects must satisfy all of the specified label constraints
```

---------------------------------------------------------------------------------------------------------------------------------------
```

## Interacting with Nodes and cluster

```bash
kubectl cordon my-node                                                # Mark my-node as unschedulable
kubectl drain my-node                                                 # Drain my-node in preparation for maintenance
kubectl uncordon my-node                                              # Mark my-node as schedulable
kubectl top node my-node                                              # Show metrics for a given node
kubectl cluster-info                                                  # Display addresses of the master and services
kubectl cluster-info dump                                             # Dump current cluster state to stdout
kubectl cluster-info dump --output-directory=/path/to/cluster-state   # Dump current cluster state to /path/to/cluster-state

# View existing taints on which exist on current nodes.
kubectl get nodes -o='custom-columns=NodeName:.metadata.name,TaintKey:.spec.taints[*].key,TaintValue:.spec.taints[*].value,TaintEffect:.spec.taints[*].effect'

# If a taint with that key and effect already exists, its value is replaced as specified.
kubectl taint nodes foo dedicated=special-user:NoSchedule
```

### Resource types

List all supported resource types along with their shortnames, [API group](/docs/concepts/overview/kubernetes-api/#api-groups-and-versioning), whether they are [namespaced](/docs/concepts/overview/working-with-objects/namespaces), and [Kind](/docs/concepts/overview/working-with-objects/kubernetes-objects):

```bash
kubectl api-resources
```

Other operations for exploring API resources:

```bash
kubectl api-resources --namespaced=true      # All namespaced resources
kubectl api-resources --namespaced=false     # All non-namespaced resources
kubectl api-resources -o name                # All resources with simple output (only the resource name)
kubectl api-resources -o wide                # All resources with expanded (aka "wide") output
kubectl api-resources --verbs=list,get       # All resources that support the "list" and "get" request verbs
kubectl api-resources --api-group=extensions # All resources in the "extensions" API group
```

### Formatting output

To output details to your terminal window in a specific format, add the `-o` (or `--output`) flag to a supported `kubectl` cmd.

Output format | Description
--------------| -----------
`-o=custom-columns=<spec>` | Print a table using a comma separated list of custom columns
`-o=custom-columns-file=<filename>` | Print a table using the custom columns template in the `<filename>` file
`-o=json`     | Output a JSON formatted API object
`-o=jsonpath=<template>` | Print the fields defined in a [jsonpath](/docs/reference/kubectl/jsonpath) expression
`-o=jsonpath-file=<filename>` | Print the fields defined by the [jsonpath](/docs/reference/kubectl/jsonpath) expression in the `<filename>` file
`-o=name`     | Print only the resource name and nothing else
`-o=wide`     | Output in the plain-text format with any additional information, and for pods, the node name is included
`-o=yaml`     | Output a YAML formatted API object

Examples using `-o=custom-columns`:

```bash
# All images running in a cluster
kubectl get pods -A -o=custom-columns='DATA:spec.containers[*].image'

# All images running in namespace: default, grouped by Pod
kubectl get pods --namespace default --output=custom-columns="NAME:.metadata.name,IMAGE:.spec.containers[*].image"

 # All images excluding "registry.k8s.io/coredns:1.6.2"
kubectl get pods -A -o=custom-columns='DATA:spec.containers[?(@.image!="registry.k8s.io/coredns:1.6.2")].image'

# All fields under metadata regardless of name
kubectl get pods -A -o=custom-columns='DATA:metadata.*'
```

More examples in the kubectl [reference documentation](/docs/reference/kubectl/#custom-columns).

### Kubectl output verbosity and debugging

Kubectl verbosity is controlled with the `-v` or `--v` flags followed by an integer representing the log level. General Kubernetes logging conventions and the associated log levels are described [here](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-instrumentation/logging.md).

Verbosity | Description
--------------| -----------
`--v=0` | Generally useful for this to *always* be visible to a cluster operator.
`--v=1` | A reasonable default log level if you don't want verbosity.
`--v=2` | Useful steady state information about the service and important log messages that may correlate to significant changes in the system. This is the recommended default log level for most systems.
`--v=3` | Extended information about changes.
`--v=4` | Debug level verbosity.
`--v=5` | Trace level verbosity.
`--v=6` | Display requested resources.
`--v=7` | Display HTTP request headers.
`--v=8` | Display HTTP request contents.
`--v=9` | Display HTTP request contents without truncation of contents.

## {{% heading "whatsnext" %}}

* Read the [kubectl overview](/docs/reference/kubectl/) and learn about [JsonPath](/docs/reference/kubectl/jsonpath).

* See [kubectl](/docs/reference/kubectl/kubectl/) options.

* Also read [kubectl Usage Conventions](/docs/reference/kubectl/conventions/) to understand how to use kubectl in reusable scripts.

* See more community [kubectl cheatsheets](https://github.com/dennyzhang/cheatsheet-kubernetes-A4).