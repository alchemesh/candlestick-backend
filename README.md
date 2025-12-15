# Candlestick Pattern - Python Backend

The Python backend for the Candlestick Pattern application.

The Python backend is used as an ETL job given by the event trigger. The event is passed through a queue (RabbitMQ), which is consumed by the Python backend for processing. Stock market data is extracted using the YFinance library. The data is then tranformed for easier pattern recognition and passed to the Java API. Unit testing is done with Pytest, and coverage testing is done through Pytest Coverage. 


## How to use ##

Deploy the image using Docker, Kubernetes, or any other container orchestration service using the docker io image: sabatiel180/candlestick-backend-app

### Environment variables ###

The docker image needs 2 environment variables to function which are used to connect to RabbitMQ and the Java API
- RABBITMQ
- JAVA_API

***Note: This application is a consumer, and therefore will not perform any function without the queue. The Java API is just as equally important, for the data will not have a destination without it.***


### Docker ###

#### Docker Build ####
The manual approach can be used by downloading the repository your local machine. Navigate to the folder and run:

docker build -t [your_image_name] .

#### Docker Run ####
Run the image using the environment variables for the RabbitMQ and Java API images.

docker run -itd --env=RABBITMQ=[your_rabbitmq_image_name] --env=JAVA_API=[your_java_api_name] --name [your_container_name] [your_image_name]

Where:
* your_rabbitmq_image_name = (The docker image name for your RabbitMQ instance)
* your_java_api_name = (The docker image name for the Java API instance)
* your_container_name = (The name you want to issue to the running container)
* your_image_name = (The name you used if you built the image manually. Use sabatiel180/candlestick-backend-app for easier deployment)

Information about deployment for the Java API can be found at [Java API] (https://github.com/alchemesh/candlestick-java-api). RabbitMQ is the queue service used for the application and has its own official image from Docker. No additional configuration is needed for RabbitMQ and can be deployed with the following command:

* docker run -itd --name [your_container_name] rabbitmq:3-management


### Kubernetes ###
The Kubernetes files in this repo can be used as a template for deployment.

#### Deployment ####
The deployment.yaml file will deploy the python backend as a replica set with a name and app labels as candlestick-backend-app-deploy and candlestick-backend-app respectfully. ***Note: The RABBITMQ and JAVA_API environment variables are set to the Kubernetes RABBITMQ and Java API deployment service names which should be deployed as well***

#### Service ####
The Python backend replicaset is deployed as a LoadBalancer service. This can potentially allow for horizontal scaling for the backend application to balance the load should it ever be necessary. The service name, candlestick-backend-service, is not used by any other application on the stack for communication.