import ipaddress
import math

def calculate_subnet_size(num_hosts):
    # Augmente le nombre d'hôtes de 10% et ajoute 2 pour le réseau et l'adresse de diffusion
    adjusted_hosts = int(math.ceil(num_hosts * 1.1)) + 2
    # Calcule la taille nécessaire du sous-réseau pour accueillir les hôtes ajustés
    return 32 - int(math.ceil(math.log2(adjusted_hosts)))

# def assign_specific_ip(subnets, ip_address, designated_network):
#     # Trouve le sous-réseau désigné et s'assure que l'IP peut être assignée
#     for subnet in subnets:
#         if subnet['Réseau'] == designated_network and ip_address in subnet['network'].hosts():
#             return subnet['network']
#     raise ValueError(f"L'adresse {ip_address} ne peut pas être assignée au réseau {designated_network}.")

def can_accommodate_subnets(base_network, hosts_per_subnet_list):
    base_net = ipaddress.ip_network(base_network, strict=False)
    total_required_addresses = sum(int(math.ceil(hosts * 1.1)) + 2 for hosts in hosts_per_subnet_list)
    return base_net.num_addresses >= total_required_addresses

def calculate_subnet_info(network, num_hosts):
    total_hosts = int(math.ceil(num_hosts * 1.1)) + 2
    subnet_prefix = 32 - int(math.ceil(math.log2(total_hosts)))
    for subnet in network.subnets(new_prefix=subnet_prefix):
        if subnet.num_addresses >= total_hosts:
            return subnet
    return None

def subnet_calculator(base_network, hosts_per_subnet_list):
    base_net = ipaddress.ip_network(base_network, strict=False)
    # Trie les demandes de sous-réseaux par le nombre d'hôtes décroissant
    sorted_hosts = sorted(((hosts, i) for i, hosts in enumerate(hosts_per_subnet_list)), reverse=True)
    subnets_info = []
    allocated_subnets = []

    for hosts, original_position in sorted_hosts:
        prefixlen = calculate_subnet_size(hosts)
        # Trouve le premier sous-réseau disponible qui peut accueillir le nombre d'hôtes
        for subnet in base_net.subnets(new_prefix=prefixlen):
            if subnet not in allocated_subnets and all(subnet.overlaps(allocated) == False for allocated in allocated_subnets):
                allocated_subnets.append(subnet)
                subnet_info = {
                    'Réseau': chr(65 + original_position),
                    'Nombre adresses': subnet.num_addresses,
                    'Adresse du sous-réseau': str(subnet.network_address),
                    'Masque': f"{subnet.netmask} ou /{subnet.prefixlen}",
                    '1ère machine': str(next(subnet.hosts())),
                    'Dernière Machine': str(subnet.broadcast_address - 1),
                    'Adresse de Diffusion': str(subnet.broadcast_address)
                }
                subnets_info.append((original_position, subnet_info))
                break

    # Trie les informations de sous-réseaux par position originale
    subnets_info.sort(key=lambda x: x[0])
    return [info for _, info in subnets_info]


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
if validated_address:
    num_subnets_input = int(input("Entrez le nombre de sous-réseaux désirés: "))
    hosts_per_subnet_list = [int(input(f"Entrez le nombre d'hôtes pour le sous-réseau {chr(65 + i)}: ")) for i in range(num_subnets_input)]
    subnets_info = subnet_calculator(validated_address, hosts_per_subnet_list)
    print_subnet_info(subnets_info)
else:
    print("Adresse IP non valide, veuillez réessayer.")

