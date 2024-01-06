> You need to setup environmen variable(.env) in docker-compose.yml for k8s/01-setup-deployment.

command step:
-----

```bash
kubectl delete ns eskibana
docker-compose up
kubectl create configmap es-certs-configmap --from-file=config/certs/ca.zip --from-file=config/certs/certs.zip --from-file=config/certs/instances.yml --from-file=config/certs/es01/es01.crt --from-file=config/certs/es01/es01.key --from-file=config/certs/ca/ca.crt --from-file=config/certs/ca/ca.key --from-file=config/kibana.yml --dry-run=client -o yaml > ./01-configMap.yaml
kubectl create ns eskibana
kubectl apply -f ./01-configMap.yaml -n eskibana
kubectl apply -f ./02-setup-deployment.yaml -n eskibana
kubectl apply -f ./03-es01-deployment.yaml -n eskibana
kubectl apply -f ./04-es01-service.yaml -n eskibana
kubectl apply -f ./05-kibana-deployment.yaml -n eskibana
kubectl apply -f ./06-kibana-service.yaml -n eskibana
```