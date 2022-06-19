#!/bin/sh
echo "start"
sudo snap install docker
sudo docker pull marekplaza/apiuslab:2022SSH2
sudo docker pull marekplaza/ceos64-lab:4.27.1.1F
sudo docker tag marekplaza/ceos64-lab:4.27.1.1F ceos64-lab:4.27.1.1F
cd /home/apiuslab/apiuslab
sudo docker run --rm -it --privileged     --network host     -v /var/run/docker.sock:/var/run/docker.sock     -v /var/run/netns:/var/run/netns     -v /etc/hosts:/etc/hosts     --pid="host"     -v $(pwd):$(pwd)     -w $(pwd)  marekplaza/apiuslab:2022SSH2
echo "end"