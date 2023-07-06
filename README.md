# Topology

A Python script to create a topology in Cisco Packet Tracer.

## Author

John Modica

## Usage

1. Clone the repository.

```
git clone https://github.com/CybernetiX-S3C/Topology
```

2. Move into directory.

```
cd Topology
```

3. Install the dependencies.

```
pip install -r requirements.txt
```

4. Run the script.

```
python create_topology.py create
```

This will create a topology with 3 subnets, 2 PCs per subnet, a mother IP address of 192.168.1.1, and subnet IP addresses of 192.168.1.0, 192.168.2.0, and 192.168.3.0. The topology data will be saved to a file called `topology.json`.

## Help

```
usage: create_topology.py [-h] [-f FILE]

Create a topology in Cisco Packet Tracer.

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Save the topology data to a file.
```
## Description

```
This script uses the Cisco Packet Tracer API to create a topology. The script takes a few parameters, such as the number of subnets, the number of PCs per subnet, and the mother IP address. The script also allows you to save the topology data to a file.
```

## Examples

# Create a topology with 3 subnets, 2 PCs per subnet, and a mother IP address of 192.168.1.1.
python create_topology.py create

# Save the topology data to a file called 'topology.json'.
python create_topology.py create --file topology.json

## License

This script is released under the MIT License.
