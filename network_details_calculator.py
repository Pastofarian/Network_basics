# calcule masque décimal / adresse réseau et diffusion / nombre d'hôte a partir d'une adresse IP + masque 
import ipaddress

def calculate_network_details(ip_cidr):
    try:
        # Crée un objet réseau à partir de l'adresse IP et du masque CIDR
        network = ipaddress.IPv4Network(ip_cidr, strict=False)

        # Calcule le masque décimal
        decimal_mask = network.netmask
        # Calcule l'adresse réseau
        network_address = network.network_address
        # Calcule l'adresse broadcast
        broadcast_address = network.broadcast_address
        # Calcule le nombre d'hôtes (en excluant l'adresse réseau et broadcast)
        num_hosts = network.num_addresses - 2

        # Affiche les résultats
        print(f"Adresse IP avec CIDR: {ip_cidr}")
        print(f"Masque décimal: {decimal_mask}")
        print(f"Adresse réseau: {network_address}")
        print(f"Adresse broadcast: {broadcast_address}")
        print(f"Nombre d'hôtes: {num_hosts}")

    except ValueError as e:
        print(f"Erreur: {e}")

# Exemple d'utilisation
ip_cidr_input = input("Entrez une adresse IPv4 avec masque CIDR (ex: 131.108.78.235/21): ")
calculate_network_details(ip_cidr_input)
