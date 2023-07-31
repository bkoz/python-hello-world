# Sample ElasticSearch Python client

## Environment Variables

Set the following environment variables via shell or ConfigMap:

Example ConfigMap

```
kind: ConfigMap
apiVersion: v1
metadata:
  name: my-env-vars
  labels:
    controller.devfile.io/mount-to-devworkspace: 'true'
    controller.devfile.io/watch-configmap: 'true'
  annotations:
    controller.devfile.io/mount-as: env
data:
  ELASTIC_HOST: elastic-host
  ELASTIC_USER: elastic-user
  ELASTIC_PASSWORD: elastic-passwd
```

Run the test client.

```
python hello-elastic.py
```