# interview-service-troubleshooting
Try to find and fix as many issues as possible.

## Description

Some description and requirements of the service are listed below:

1. The service should be delivered as a Docker container image
2. Logs should be printed to stdout
3. Service has performance requirements:
  3.1 response to HTTP GET request to /items < 1 minute
  3.2 response to HTTP GET request to /health < 10 seconds
4. Service should respond to HTTP GET requests:
  4.1 /health - shows if service is still alive, expected response: HTTP code 200, content: ok
  4.2 /items - gets data from remote service and provides output as json data.
