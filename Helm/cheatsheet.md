## List of Helm Commands

### Basic interpretations/context

Chart:
- It is name of your chart in case it has been pulled and untared.
- It is <repo_name>/<chart_name> in case the repository has been added but chart not pulled.
- It is the URL/Absolute path to the chart.

Name:
- It is the name you want to give to your current helm chart installation.

Release:
- Is the name you assigned to an installation instance. 

Revision
- Is the value from the Helm history command

### Chart Management
```bash
helm create [name] #creates a chart directory along with the common files and directories used in a chart.
helm package [chart-path]  #packages a chart into a versioned chart archive file.
helm lint [chart] # Run tests to examine a chart and identify possible issues:
helm show all [chart] #Inspect a chart and list its contents:
helm show values [chart] #displays the contents of the values.yaml file
helm pull [chart] #Download/pull chart 
helm pull [chart] --untar=true # if set to true, will untar the chart after downloading it
helm pull [chart] --verify  #verify the package before using it
helm pull [chart] --version <number> # default-latest is used, specify a version constraint for the chart version to use
helm dependency list [chart] # Display a list of a chart’s dependencies:
``` 

### Install and Uninstall Apps

```bash
helm install <name> <chart>                 # Install the chart with a name
helm install <name> <chart> --namespace <namespace>  # Install the chart in a specific namespace
helm install <name> <chart> --set key1=val1,key2=val2 # set values on the command line (can specify multiple or separate values with commas)
helm install <name> <chart> --values <yaml-file/url> # Install the chart with your specified values

helm install <name> <chart> --dry-run --debug  # Run a test installation to validate chart (p)
helm install <name> <chart> --verify     # verify the package before using it 
helm install <name> <chart> --dependency-update    # update dependencies if they are missing before installing the chart
helm uninstall <name>                          # Uninstall a release
```

### Perform App Upgrade and Rollback
```bash
helm upgrade [release] [chart]                           # Upgrade a release
helm upgrade [release] [chart] --atomic                # if set, upgrade process rolls back changes made in case of failed upgrade.
helm upgrade [release] [chart] --dependency-update  # update dependencies if they are missing before installing the chart
helm upgrade [release] [chart] --version <version_number>  # specify a version constraint for the chart version to use
helm upgrade [release] [chart] --values  # specify values in a YAML file or a URL (can specify multiple)
helm upgrade [release] [chart] --set key1=val1,key2=val2 # set values on the command line (can specify multiple or separate valuese)
helm upgrade [release] [chart] --force  # force resource updates through a replacement strategy
helm rollback [release] [revision]  # Roll back a release to a specific revision
helm rollback [release] [revision]  --cleanup-on-fail # Allow deletion of new resources created in this rollback when rollback fails
``` 

### List, Add, Remove, and Update Repositories
```bash
helm repo add [repo-name] [url]   #Add a repository from the internet:
helm repo list   # List added chart repositories
helm repo update  # update information of available charts locally from chart repositories
helm repo remove [repo_name] # remove one or more chart repositories
helm repo index [DIR] # Read the current directory and generate an index file based on the charts found.
helm repo index [DIR] --merge # Merge the generated index with an existing index file
helm search repo [keyword]  # search repositories for a keyword in charts
helm search hub [keyword]  # search for charts in the Artifact Hub or your own hub instance
```

### Helm Release monitoring
```bash
helm list  # lists all of the releases for a specified namespace, uses current namespace context if namespace not specified
helm list -all #show all releases without any filter applied, can use -a
helm list -all-namespaces  #list releases across all namespaces, we can use -A
helm -l key1=value1,key2=value2  # Selector (label query) to filter on, supports '=', '==', and '!='
helm list --date # sort by release date
helm list --deployed #show deployed releases. If no other is specified, this will be automatically enabled
helm list --pending #  show pending releases
helm list --failed # show failed releases
helm list --uninstalled #show uninstalled releases (if 'helm uninstall --keep-history' was used)
helm list --superseded # show superseded releases
helm list -o yaml # prints the output in the specified format. Allowed values: table, json, yaml (default table)
helm status [release]  #This command shows the status of a named release.
helm status [release] --revision <number> #if set, display the status of the named release with revision
helm history [release] #historical revisions for a given release.
helm env # Env prints out all the environment information in use by Helm.
```

### Download Release Information
```bash
helm get all [release] # a human readable collection of information about the notes, hooks, supplied values, and generated manifest file of the given release.
helm get hooks [release] #This command downloads hooks for a given release. Hooks are formatted in YAML and separated by the YAML '---\n' separator.
helm get manifest [release] # A manifest is a YAML-encoded representation of the Kubernetes resources that were generated from this release's chart(s). If a chart is dependent on other charts, those resources will also be included in the manifest.
helm get notes [release] # shows notes provided by the chart of a named release.
helm get values [release] #downloads a values file for a given release. use -o to format output
```

### Plugin Management
```bash
helm plugin install [path/url1]  #Install plugins
helm plugin list #View a list of all installed plugins
helm plugin update [plugin1]  #Update plugins
helm plugin uninstall [plugin] #Uninstall a plugin
```