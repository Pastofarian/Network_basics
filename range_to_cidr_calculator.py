# calcule le numéro de réseau / Masque décimal / CIDR à partir d'une plage d'adresse
import ipaddress

def calculate_network_from_range(start_ip, end_ip):
    start = ipaddress.IPv4Address(start_ip)
    end = ipaddress.IPv4Address(end_ip)

    # Vérifie que la plage est valide
    if int(start) > int(end):
        raise ValueError("L'adresse de début doit être inférieure à l'adresse de fin.")

    # Calcule le nombre de bits nécessaire pour couvrir la plage d'adresses
    num_addresses = int(end) - int(start) + 1
    cidr_bits = 32 - (num_addresses-1).bit_length()
    
    # Construit le réseau CIDR
    network = ipaddress.ip_network(f"{start}/{cidr_bits}", strict=False)
    network_address = network.network_address
    decimal_mask = network.netmask

    return network_address, decimal_mask, f"/{network.prefixlen}"

# Exemple d'utilisation
start_ip_input = input("Entrez l'adresse de début de la plage (ex: 221.118.64.1): ")
end_ip_input = input("Entrez l'adresse de fin de la plage (ex: 221.118.127.254): ")

try:
    network_address, decimal_mask, cidr = calculate_network_from_range(start_ip_input, end_ip_input)
    print(f"Numéro de réseau : {network_address}")
    print(f"Masque décimal : {decimal_mask}")
    print(f"Plage CIDR : {cidr}")
except ValueError as e:
    print(e)
