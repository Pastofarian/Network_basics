import ipaddress

def calculate_ipv6_range_full(ipv6_cidr):
    try:
        # Créer un objet réseau IPv6 à partir de la notation CIDR
        network = ipaddress.IPv6Network(ipv6_cidr, strict=False)

        # Calculer la première adresse de la plage du réseau
        first_address = network.network_address.exploded
        # Calculer la dernière adresse de la plage du réseau
        last_address = network[-1].exploded

        # Retourner les adresses sous forme de chaînes de caractères complètes
        return first_address, last_address
    except ValueError as e:
        return f"Erreur: {e}"

# Fonction pour vérifier si l'adresse IPv6 et le masque CIDR sont valides
def is_valid_ipv6_cidr(ipv6_cidr):
    try:
        ipaddress.IPv6Network(ipv6_cidr)
        return True
    except ValueError:
        return False

# Demander à l'utilisateur d'entrer une adresse IPv6 avec le masque CIDR
ipv6_cidr_input = input("Entrez une adresse IPv6 avec masque CIDR (par exemple, 2001:db8::/32) : ")

# Vérifier si l'adresse IPv6 avec le masque CIDR est valide
if is_valid_ipv6_cidr(ipv6_cidr_input):
    # Calculer la plage d'adresses IPv6
    first_address, last_address = calculate_ipv6_range_full(ipv6_cidr_input)
    # Afficher les résultats
    print(f"Première adresse : {first_address}, Dernière adresse : {last_address}")
else:
    print("L'adresse IPv6 entrée est invalide.")
