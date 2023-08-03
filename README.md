# A sample ElasticSearch Python client using Openshift DevSpaces

## Environment Variables

Set the following environment variables via terminal shell or ConfigMap:

```
ELASTIC_HOST
ELASTIC_USER
ELASTIC_PASSWORD
```

The [env-vars file](env-vars.yaml) contains an example ConfigMap. The ConfigMap can be created using either the Openshift console or CLI. 

CLI example:
```
oc apply -f env-vars.yaml -n <login-devspaces>
```

Run the [hello-elastic.py](hello-elastic.py) file from the *run* button in VSCode or the terminal shell.

```
python hello-elastic.py
```