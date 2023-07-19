# Simple prometeheus + python example

To use this example you will need docker

1. Edit [prometheus.yml::9](prometheus.yml) with the ip address of your local host. On wsl2 I got this with `ip addr show`, this is needed
since docker wont recogineze (obviously) localhost as the ip that runs the python example.
2. Build the docker image, which will copy the prometheus.yml to the docker env. I my case I 
wasn't able to get it working using -v option that is listed on the examples due to wsl2 issues.
```
docker build -t prometheus .
```
4. Run the docker container on any available port. To test if prometheus is running, just open localhost:9090 (in my case), and check prometheus targets
```
docker run -p 9090:9090 prometheus
```
3. Once the container is running, run [example.py](example.py). I've added a simple counter and gauge for example purposes.