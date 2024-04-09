# interview-service-troubleshooting
Try to find and fix as many issues as possible.

## Description

Some description and requirements of the service are listed below:

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
