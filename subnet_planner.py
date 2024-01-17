import ipaddress

# Determine if an IP address belongs to a given network
def belongs_to_network(ip, network_cidr):
    return ipaddress.ip_address(ip) in ipaddress.ip_network(network_cidr, strict=False)

# Determine if two IP addresses can communicate
def can_communicate(ip1, mask1, gateway1, ip2, mask2, gateway2, routing_table):
    network1 = ipaddress.IPv4Network(f"{ip1}/{mask1}", strict=False)
    network2 = ipaddress.IPv4Network(f"{ip2}/{mask2}", strict=False)
    
    if network1.overlaps(network2):
        return 'OK'
    
    for network_cidr in routing_table:
        if belongs_to_network(ip1, network_cidr) and belongs_to_network(ip2, network_cidr):
            return 'OK'
    
    return 'NOK'

# Main function to collect data and fill in the communication table
def main():
    num_networks = int(input("Entrez le nombre de réseaux : "))
    network_names = [chr(65 + i) for i in range(num_networks)]

    networks = {}
    all_machines = {}
    for network_name in network_names:
        machines_info = input(f"Entrez le nombre de machines dans le réseau {network_name} et leurs noms (ex : 2 D, E) : ")
        num_machines, machine_names = machines_info.split(maxsplit=1)
        machine_names = machine_names.replace(' ', '').split(',')
        networks[network_name] = {
            'machines': {name: {} for name in machine_names},
            'gateway': input(f"Entrez l'adresse IP de la passerelle du réseau {network_name} : ")
        }
        all_machines.update({name: network_name for name in machine_names})

    for machine_name, network_name in all_machines.items():
        ip_input = input(f"Entrez l'adresse IP pour la machine {machine_name} : ")
        subnet_mask_input = input(f"Entrez le masque de sous-réseau pour la machine {machine_name} : ")
        gateway_input = input(f"Entrez l'adresse IP pour la passerelle de la machine {machine_name} : ")
        networks[network_name]['machines'][machine_name] = (ip_input, subnet_mask_input, gateway_input)

    # Collect entries for the routing table
    num_routes = int(input("Combien y a-t-il d'entrées dans la table de routage ? "))
    routing_table = []
    for _ in range(num_routes):
        route_cidr = input("Entrez l'entrée de la table de routage (IP/masque en notation CIDR, ex : 192.168.1.0/24) : ")
        routing_table.append(route_cidr)

    communication_table = {m: {} for m in all_machines}

    for network1 in networks.values():
        for network2 in networks.values():
            for machine1, data1 in network1['machines'].items():
                for machine2, data2 in network2['machines'].items():
                    if machine1 == machine2:
                        communication_table[machine1][machine2] = 'X'
                    else:
                        ip1, mask1, gateway1 = data1
                        ip2, mask2, gateway2 = data2
                        communication_table[machine1][machine2] = can_communicate(ip1, mask1, gateway1, ip2, mask2, gateway2, routing_table)

    print("Tableau de communication :")
    headers = sorted(communication_table.keys())
    print("   ", "  ".join(headers))
    for key1 in headers:
        print(key1, " ", "  ".join(communication_table[key1].get(key2, 'NOK') for key2 in headers))

if __name__ == "__main__":
    main()
