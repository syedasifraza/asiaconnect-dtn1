from kubernetes import client, config


def main():
    config.load_kube_config(config_file='./config')
    api_instance = client.CoreV1Api()

    node_list = api_instance.list_node()

    print(node_list.items)

    for node in node_list.items:
        if ("nvidia.com/gpu" in node.status.capacity):
           print(node.status.capacity["cpu"], "\t",node.status.capacity["memory"],"\t",node.status.capacity["nvidia.com/gpu"])
        else:
            print(node.status.capacity["cpu"], "\t",node.status.capacity["memory"],"\t","0")


if __name__ == '__main__':
    main()
