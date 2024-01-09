source .venv/Scripts/activate
cd ./k8s
kubectl delete ns eskibana
docker-compose up
kubectl create configmap es-certs-configmap --from-file=config/certs/ca.zip --from-file=config/certs/certs.zip --from-file=config/certs/instances.yml --from-file=config/certs/es01/es01.crt --from-file=config/certs/es01/es01.key --from-file=config/certs/ca/ca.crt --from-file=config/certs/ca/ca.key --from-file=config/kibana.yml --from-file=config/logstash.conf --from-file=config/logstash.yml --dry-run=client -o yaml > ./manifest/01-configMap.yaml
kubectl create ns eskibana
kubectl apply -f ./manifest -n eskibana
kubectl get svc kibana -n eskibana --output=jsonpath='{.spec.ports[?(@.port==5601)].nodePort}'| xargs -I {} sh -c 'python ../sample-pylog.py && start http://localhost:{}'