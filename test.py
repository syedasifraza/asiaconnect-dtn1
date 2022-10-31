from kubernetes import client, config
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config(config_file='./config')

k8s_api = client.CoreV1Api()
logger.info("Getting k8s nodes...")
response = k8s_api.list_node()
nodes = []
for node in response.items:
    nodes.append(node)
response.items = nodes
#logger.info(response.items)

logger.info("Current k8s node count is {}".format(len(response.items)))


