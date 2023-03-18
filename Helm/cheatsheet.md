## List of Helm Commands

### Basic interpretations

Chart:
- It is name of your chart in case it has been pulled and untared.
- It is <repo_name>/<chart_name> in case the repository has been added but chart not pulled.
- It is the URL/Absolute path to the chart.

### Install and Uninstall Apps

```bash
helm install <name> <chart>                 # Install the chart with a name
helm install <name> <chart> --namespace <namespace>  # Install the chart in a specific namespace
helm install <name> <chart> --values <yaml-file/url> # Install the chart with your specified values
helm install <name> <chart> --dry-run --debug  # Run a test installation to validate chart (p) 
helm uninstall <name>                          # Uninstall a release
```
