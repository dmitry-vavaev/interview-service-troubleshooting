# interview-service-troubleshooting

## Task

Tasks for this exercise are below:

1. Service is not able to meet performance requirements. Please find the reason.
2. Try to find and fix as many issues as possible to make this solution work as mentioned in the description below.
3. Give recommendations if any to improve quality of the solution.

## Description

There is a service which provides some HTTP endpoints for the users. It should run as a standalone service inside of docker container.
Ansible playbooks are used for build and deploy the service.


Some description and requirements of the service are listed below:

```
1. The service uses external api to get data. That api is considered as stable. Response time is up to 2 seconds per request.
2. Logs should be printed to stdout
3. Service has performance requirements:
  3.1 response to HTTP GET request to /items < 10 seconds
  3.2 response to HTTP GET request to /health < 2 seconds
4. Service should respond to HTTP GET requests:
  4.1 /health - shows if service is still alive, expected response: HTTP code 200, content: ok
  4.2 /items - gets data from remote service and provides output as json data.
5. The service should be delivered as a Docker container image
6. The service uses ansible playbook to build the image and start container on the same host.
```
