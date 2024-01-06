import ipaddress
import math

def calculate_subnet_info(network, num_hosts):
    total_hosts = int(math.ceil(num_hosts * 1.1)) + 2
    subnet_prefix = 32 - int(math.ceil(math.log2(total_hosts)))
    for subnet in network.subnets(new_prefix=subnet_prefix):
        if subnet.num_addresses >= total_hosts:
            return subnet
    return None

def subnet_calculator(base_network, hosts_per_subnet_list):
    base_net = ipaddress.ip_network(base_network, strict=False)
    current_network = base_net
    subnets_info = []

    # Sort the list in descending order of number of hosts to allocate largest subnets first
    sorted_hosts = sorted([(hosts, i) for i, hosts in enumerate(hosts_per_subnet_list)], reverse=True)

    for hosts, original_position in sorted_hosts:
        new_subnet = calculate_subnet_info(current_network, hosts)
        if not new_subnet:
            raise ValueError(f"Cannot accommodate {hosts} hosts in any subnet from {current_network}")

        # Prepare subnet information
        subnet_info = {
            'Réseau': chr(65 + original_position),
            'Nombre adresses': new_subnet.num_addresses,
            'Adresse du sous-réseau': str(new_subnet.network_address),
            'Masque': f"{new_subnet.netmask} ou /{new_subnet.prefixlen}",
            '1ère machine': str(new_subnet.network_address + 1),
            'Dernière Machine': str(new_subnet.broadcast_address - 1),
            'Adresse de Diffusion': str(new_subnet.broadcast_address)
        }
        subnets_info.append((original_position, subnet_info))
        
        # Update the current network to the remaining address space after the new subnet
        current_network = list(new_subnet.supernet().address_exclude(new_subnet))[0]

    # Sort subnets_info based on the original position
    subnets_info.sort(key=lambda x: x[0])
    return [info for position, info in subnets_info]

def print_subnet_info(subnets_info):
    for subnet_info in subnets_info:
        print(f"Réseau: {subnet_info['Réseau']}")
        print(f"Nombre adresses: {subnet_info['Nombre adresses']}")
        print(f"Adresse du sous-réseau: {subnet_info['Adresse du sous-réseau']}")
        print(f"Masque: {subnet_info['Masque']}")
        print(f"1ère machine: {subnet_info['1ère machine']}")
        print(f"Dernière Machine: {subnet_info['Dernière Machine']}")
        print(f"Adresse de Diffusion: {subnet_info['Adresse de Diffusion']}\n")


def validate_ip_address(address):
    try:
        network = ipaddress.ip_network(address, strict=True)
        return str(network)
    except ValueError:
        try:
            ip = ipaddress.ip_address(address.split('/')[0])
            network = ipaddress.ip_network(f"{ip}/{address.split('/')[1]}", strict=False)
            return str(network.network_address) + '/' + address.split('/')[1]
        except ValueError as ve:
            print(f"Erreur d'adresse IP : {ve}")
            return None

# Exemple d'utilisation
base_network_input = input("Entrez le réseau de base avec CIDR (ex: 220.100.80.0/24): ")
validated_address = validate_ip_address(base_network_input)
if validated_address is not None:
    num_subnets_input = int(input("Entrez le nombre de sous-réseaux désirés: "))
    hosts_per_subnet_list = []
    for i in range(num_subnets_input):
        hosts = int(input(f"Entrez le nombre d'hôtes pour le sous-réseau {chr(65 + i)}: "))
        hosts_per_subnet_list.append(hosts)

    subnets_info = subnet_calculator(validated_address, hosts_per_subnet_list)
    print_subnet_info(subnets_info)
else:
    print("Adresse IP non valide, veuillez réessayer.")
