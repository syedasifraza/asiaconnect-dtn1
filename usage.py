#!/usr/bin/python
# Script name: usage_info.py

from kubernetes import client, config
from subprocess import call

config.load_kube_config(config_file='./config')

api = client.CustomObjectsApi()
k8s_nodes = api.list_cluster_custom_object("metrics.k8s.io", "v1beta1", "nodes")
#call('kubectl describe node sukkur-node | grep -A1 "Capacity" | tail -n1', shell=True)
print(k8s_nodes)

#for stats in k8s_nodes['items']:
#    print(stats)
    #print("Node Name: %s\tCPU: %s\tMemory: %s" % (stats['metadata']['name'], stats['usage']['cpu'], stats['usage']['memory']))
