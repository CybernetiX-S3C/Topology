# Create Topology in Cisco Packet Tracer

This script creates a topology in Cisco Packet Tracer. The topology consists of a number of subnets, each with a number of PCs. The script also creates a "mother" PC that is connected to all of the subnets.

## Usage

To use the script, run it from the command line with the following arguments:


python create_topology.py [command] [parameters]


The `command` argument can be one of the following:

* `create`: Creates a new topology.
* `help`: Prints a help message.

The `parameters` argument depends on the command. For the `create` command, the parameters are the number of subnets, the number of PCs per subnet, the mother IP address, and the IP addresses of the subnets.

## Example

The following command creates a topology with 3 subnets, 2 PCs per subnet, a mother IP address of 192.168.1.1, and subnet IP addresses of 192.168.1.0, 192.168.2.0, and 192.168.3.0:


python create_topology.py create 3 2 192.168.1.1 192.168.1.0 192.168.2.0 192.168.3.0


## Output

If the script is successful, it will print the URL of the topology in Cisco Packet Tracer.

## Troubleshooting

If the script fails, it will print an error message. The error message will usually indicate the reason for the failure.

## License

This script is released under the MIT License.

## Author 
John Modica
