from ipaddress import ip_address, ip_network

def check_ip_address(ip_str, cidr=None):
    """
    Vérifie et catégorise une adresse IP selon plusieurs critères :
    - Validité
    - Spéciale, Multicast, Link-local
    - Privée ou Publique
    - Assignabilité à une machine
    
    Args:
    ip_str (str): L'adresse IP à vérifier.
    cidr (str): Notation CIDR spécifiant le masque de sous-réseau.
    
    Returns:
    str: Description de la catégorisation de l'adresse IP.
    """
    try:
        # Sépare l'adresse IP du CIDR si présent
        if '/' in ip_str:
            ip_str, cidr = ip_str.split('/')
        
        # Convertit la chaîne en objet IP
        ip = ip_address(ip_str)
        
        response = []
        
        # Conditions spécifiques
        if ip_str == "127.0.0.1":
            return "boucle locale (Localhost)"
        elif ip_str.startswith("0.") and ip_str != "0.0.0.0":
            return "adresse 0.x.x.x pas utilisé"
        elif ip_str == "0.0.0.0":
            return "adresse IP utilisée pour requête DHCP"
        elif ip_str == "255.255.255.255":
            return "adresse de diffusion générale"
        
        # Vérifie si l'adresse est valide
        if ip.is_private:
            response.append(f"{ip} est une adresse privée.")
        else:
            response.append(f"{ip} est une adresse publique.")
        
        # Vérifie les classes spéciales
        if ip.is_multicast:
            response.append(f"{ip} est une adresse multicast.")
        if ip.is_link_local:
            response.append(f"{ip} est une adresse link-local.")
        
        # Gestion du masque de sous-réseau pour calculer la plage d'adresses
        if cidr:
            network = ip_network(f"{ip_str}/{cidr}", strict=False)
            if ip == network.network_address:
                response.append("adresse réseau")
            elif ip == network.broadcast_address:
                response.append("adresse broadcast")
            else:
                response.append("adresse machine")
        
        return "\n".join(response)
    except ValueError as e:
        return f"Adresse non valide: {e}"

# Demande à l'utilisateur d'entrer une adresse IP avec un masque CIDR
ip_input = input("Entrez une adresse IPv4 pour la tester: (ex: 192.168.0.1/24) ")
# Appelle la fonction avec l'adresse IP et le CIDR
print(check_ip_address(*ip_input.split('/')))
