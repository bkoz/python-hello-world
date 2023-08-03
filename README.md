# A sample ElasticSearch Python client using Openshift DevSpaces

The client programs expect the following environment variables to be set. This is best accomplished using a ConfigMap.

```
ELASTIC_HOST
ELASTIC_USER
ELASTIC_PASSWORD
```

The [env-vars file](env-vars.yaml) contains an example ConfigMap. The ConfigMap can be created using either the Openshift console or from a DevSpaces/VSCode terminal. 

Edit the [env-vars file](env-vars.yaml) to reflect your environment and create the ConfigMap.

From within a DevSpaces/VSCode terminal:
```
oc apply -f env-vars.yaml
```

Run the [hello-elastic.py](hello-elastic.py) file from the *run* button in VSCode or the terminal shell.

```
python hello-elastic.py
```