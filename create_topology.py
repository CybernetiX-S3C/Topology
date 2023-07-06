import requests

def create_topology(subnets, pcs_per_subnet, mother_ip, subnet_ips):
  """Creates a topology in Cisco Packet Tracer.

  Args:
    subnets: The number of subnets.
    pcs_per_subnet: The number of PCs in each subnet.
    mother_ip: The mother IP address.
    subnet_ips: The IP addresses of each subnet.

  Returns:
    A URL to the topology in Cisco Packet Tracer.
  """

  url = "https://pt-api.cisco.com/v1/topologies"
  data = {
    "name": "Topology",
    "subnets": subnets,
    "pcs_per_subnet": pcs_per_subnet,
    "mother_ip": mother_ip,
    "subnet_ips": subnet_ips,
  }
  response = requests.post(url, json=data)
  if response.status_code == 200:
    return response.json()["url"]
  else:
    return None

if __name__ == "__main__":
  subnets = int(input("Enter the number of subnets: "))
  pcs_per_subnet = int(input("Enter the number of PCs per subnet: "))
  mother_ip = input("Enter the mother IP address: ")
  subnet_ips = []
  for i in range(subnets):
    subnet_ips.append(input("Enter the IP address of subnet {}: ".format(i + 1)))
  url = create_topology(subnets, pcs_per_subnet, mother_ip, subnet_ips)
  if url is not None:
    print("Topology created successfully.")
    print("URL: {}".format(url))
  else:
    print("Failed to create topology.")
    
