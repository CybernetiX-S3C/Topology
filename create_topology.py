import requests
import json

def validate_input(subnets, pcs_per_subnet, mother_ip, subnet_ips):
  """Validates the input from the user.

  Args:
    subnets: The number of subnets.
    pcs_per_subnet: The number of PCs per subnet.
    mother_ip: The mother IP address.
    subnet_ips: The IP addresses of the subnets.

  Returns:
    True if the input is valid, False otherwise.
  """

  if not isinstance(subnets, int) or subnets < 1:
    raise ValueError("The number of subnets must be a positive integer.")

  if not isinstance(pcs_per_subnet, int) or pcs_per_subnet < 1:
    raise ValueError("The number of PCs per subnet must be a positive integer.")

  if not isinstance(mother_ip, str) or not mother_ip.startswith("192.168."):
    raise ValueError("The mother IP address must be in the format 192.168.xxx.xxx.")

  for subnet_ip in subnet_ips:
    if not isinstance(subnet_ip, str) or not subnet_ip.startswith("192.168."):
      raise ValueError("The subnet IP addresses must be in the format 192.168.xxx.xxx.")

  return True

def create_topology(subnets, pcs_per_subnet, mother_ip, subnet_ips):
  """Creates a topology in Cisco Packet Tracer.

  Args:
    subnets: The number of subnets.
    pcs_per_subnet: The number of PCs per subnet.
    mother_ip: The mother IP address.
    subnet_ips: The IP addresses of the subnets.

  Returns:
    A URL to the topology in Cisco Packet Tracer.
  """

  try:
    if not validate_input(subnets, pcs_per_subnet, mother_ip, subnet_ips):
      return None

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
      raise ValueError(response.text)
  except ValueError as e:
    print_error_message(e)
    return None

def print_error_message(error_message):
  """Prints a more detailed error message.

  Args:
    error_message: The error message to print.
  """

  print("Failed to create topology.")
  print(error_message)

def main():
  """The main function.
  """

  if len(sys.argv) == 1:
    print_help_message()
    return

  command = sys.argv[1]
  if command == "create":
    subnets = int(input("Enter the number of subnets: "))
    pcs_per_subnet = int(input("Enter the number of PCs per subnet: "))
    mother_ip = input("Enter the mother IP address: ")
    subnet_ips = []
    for i in range(subnets):
      subnet_ips.append(input("Enter the IP address of subnet {}: ".format(i + 1)))

    topology_data = {
      "subnets": subnets,
      "pcs_per_subnet": pcs_per_subnet,
      "mother_ip": mother_ip,
      "subnet_ips": subnet_ips,
    }

    file_name = input("Enter the file name to save the topology data to (leave blank to save to 'topology.json'): ")
    save_topology(topology_data, file_name)
  elif command == "help":
    print_help_message()
    return
  else:
    print("Unknown
