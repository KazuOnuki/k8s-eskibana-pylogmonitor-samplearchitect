step:
-----

```bash
1. kubectl delete ns eskibana
2. docker-compose up
```


```bash
3. create config/logstash.yml 

input {
  azure_blob_storage
  {
      storageaccount => "<your storage account>"
      access_key => "<your access key>"
      container => "<your container log>"
  }
}
# as you like, you customeze grok pattern👍
filter {
  grok {
      match => { "message" => "%{LOGLEVEL:loglevel} %{USERNAME:username} %{TIMESTAMP_ISO8601:timestamp} %{GREEDYDATA:message}" }
    }
}
output {
  elasticsearch {
    hosts => ["https://<your-elasticsearch-container-name>:9200/"]
    index => "<your-any-index>"
    cacert => "/usr/share/logstash/config/certs/ca/ca.crt"
    user => "<ELASTICSEARCH_USERNAME eg. default:  logstash_internal>"  # user who have elasticsearch role to control elastic search index
    password => "<ELASTICSEARCH_PASSWORD eg. default: logstash_internal>" # the user's pass
  }
  stdout {}
}
```

```bash
# export config/ data to ./manifest/01-configMap.yaml manifest
4. kubectl create configmap es-certs-configmap --from-file=config/certs/ca.zip --from-file=config/certs/certs.zip --from-file=config/certs/instances.yml --from-file=config/certs/es01/es01.crt --from-file=config/certs/es01/es01.key --from-file=config/certs/ca/ca.crt --from-file=config/certs/ca/ca.key --from-file=config/kibana.yml --from-file=config/logstash.conf --from-file=config/logstash.yml --dry-run=client -o yaml > ./manifest/01-configMap.yaml

5. kubectl create ns eskibana
6. kubectl apply -f ./manifest -n eskibana
```