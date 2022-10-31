from kubernetes import client, config
import json
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    config.load_kube_config(config_file='./config')

    api_instance = client.CoreV1Api()

    body = {
        "metadata": {
            "labels": {
                "foo": "bar",
                "baz": None}
        }
    }

    # Listing the cluster nodes
    node_list = api_instance.list_node()

    print("%s\t\t%s" % ("NAME", "LABELS"))
    # Patching the node labels
    #logger.info(node_list.items)
    for node in node_list.items:
        
        api_response = api_instance.patch_node(node.metadata.name, body)
        print("%s\t%s" % (node.metadata.name, node.metadata.labels["zone"]))
        if("hardware-type" in node.metadata.labels):
           print(node.metadata.labels["hardware-type"])
        else:
           print("CPUs")


if __name__ == '__main__':
    main()
