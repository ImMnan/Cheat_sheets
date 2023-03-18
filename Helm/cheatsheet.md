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