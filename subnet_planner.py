# calcule des sous réseaux à partir d'une adresse IP + masque
import ipaddress
import math

def subnet_calculator(base_network, num_subnets, hosts_per_subnet):
    base_net = ipaddress.ip_network(base_network, strict=False)
    # Calcule la taille de sous-réseau nécessaire pour accueillir les hôtes
    subnet_size = 32 - int((hosts_per_subnet-1).bit_length())
    subnets = list(base_net.subnets(new_prefix=subnet_size))

    if len(subnets) < num_subnets:
        raise ValueError("Le nombre de sous-réseaux demandés ne peut pas être accommodé.")

    # Affiche les informations de base
    print(f"Réseau complet : {base_net.network_address} à {base_net.broadcast_address} {base_net.prefixlen}")

    # Affiche les informations pour chaque sous-réseau
    for i, subnet in enumerate(subnets[:num_subnets]):
        print(f"Sous-réseau {i+1}: {subnet.network_address} à {subnet.broadcast_address} /{subnet.prefixlen}")

# Exemple d'utilisation
base_network_input = input("Entrez le réseau de base avec CIDR (ex: 220.100.80.0/24): ")
num_subnets_input = int(input("Entrez le nombre de sous-réseaux désirés: "))
hosts_per_subnet_input = int(input("Entrez le nombre d'hôtes par sous-réseau: "))
host_10_percent = round(hosts_per_subnet_input * 1.1)

subnet_calculator(base_network_input, num_subnets_input, host_10_percent)
