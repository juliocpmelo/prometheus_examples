# Simple prometeheus + python example

To use this example you will need docker

1. Edit [prometheus.yml::9](prometheus.yml) with the ip address of your local host. Using wsl I got this value on `ip addr show`
2. Build the docker image, which will copy the prometheus.yml to the docker env. I my case I 
wasn't able to get it working using -v option that is listed on the examples due to wsl2 issues.
3. Once the docker container is running, run [example.py](example.py). I've added a simple counter and gauge  for example purposes.