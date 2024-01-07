### Elasticsearch, Kibana, and Logstash Docker Compose Setup / Kubernetes

This Docker Compose / k8s configuration allows you to quickly set up and run Elasticsearch, Kibana, and Logstash with security features enabled.

### Prerequisites
Before you begin, make sure you have Docker and Docker Compose installed on your machine.

## Case 1: k8s Architect Overview
###### k8s application process architecture 
<img src='./assets/k8s-application-process.png' />

> The application processes within the red border are Kibana, Elasticsearch, and Logstash, which we are currently creating here. Please confirm the outbound communication from Kibana to Elasticsearch, and note that Logstash does not have communication dependencies with any other process. 

###### k8s service architecture
<img src='./assets/k8s-service.png' />

> it's creating components for Kibana, Elasticsearch, and Logstash as services. While allowing outbound communication from Kibana to Elasticsearch, Logstash performs outbound access to the internet.

## Case 2: Docker Compose Architect Overview

<img src='./assets/compose-architect.png' />

> pls check [How to read the graph](https://github.com/pmsipilot/docker-compose-viz#how-to-read-the-graph) of my favorite repository `pmsipilot/docker-compose-viz` about each diagrams.

#### Usage
1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```

1. Navigate to the cloned directory:
    ```bash
    cd <repository-directory>/single-node-multicontainer
    ```

1. Create a .env file with the following environment variables:
    ```env
    ELASTIC_PASSWORD=<your-elastic-password>
    KIBANA_PASSWORD=<your-kibana-password>
    LOGSTASH_INTERNAL_PASSWORD=<your-logstash-internal-password>
    ```
1. Run the Docker Compose configuration:
    ```bash
    docker-compose up -d
    ```
    > This command will start Elasticsearch, Kibana, and Logstash containers.
    Wait for the services to be healthy:

    ```bash
    docker-compose ps
    ```
1. Access Kibana:
Open your browser and go to `http://localhost:5601` to access Kibana.
Log in with the following credentials:
    ```env
    Username: kibana_system
    Password: <your-kibana-password>
    ```
1. Start sending logs to Logstash and explore your data in Kibana.

    >Additional Information
    Elasticsearch is accessible at https://localhost:9200.
    Logstash is available on http://localhost:9600 for data exporting internally.
    Feel free to customize the Docker Compose file and configurations based on your specific requirements.