import ipaddress

def check_ip_address(ip_str):
    try:
        # Convertit la chaîne en objet IP
        ip = ipaddress.ip_address(ip_str)

        # Conditions spécifiques
        if ip_str == "127.0.0.1":
            return "boucle locale (Localhost)"
        elif ip_str.startswith("0") and ip_str != "0.0.0.0":
            return "adresse 0.x.x.x pas utilisé"
        elif ip_str == "0.0.0.0":
            return "adresse IP utilisée pour requête DHCP"
        elif ip_str == "255.255.255.255":
            return "adresse de diffusion générale"

        # Vérifie si l'adresse est valide
        if ip.is_private:
            print(f"{ip} est une adresse privée.")
        else:
            print(f"{ip} est une adresse publique.")

        # Vérifie les classes spéciales
        if ip.is_multicast:
            print(f"{ip} est une adresse multicast.")
        elif ip.is_link_local:
            print(f"{ip} est une adresse (link-local).")

        # Extrait le dernier octet
        last_octet = int(ip_str.split('.')[-1])

        # Vérifie si c'est une adresse réseau ou broadcast basé sur le dernier octet
        if last_octet == 0:
            print(f"{ip} est une adresse réseau.")
        elif last_octet == 255:
            print(f"{ip} est une adresse broadcast.")
        else:
            print(f"{ip} n'est ni une adresse réseau, ni une adresse broadcast.")

    except ValueError as e:
        print(f"Adresse non valide: {e}")

# Exemple d'utilisation
ip_to_test = input("Entrez une adresse IPv4 pour la tester: ")
print(check_ip_address(ip_to_test))
