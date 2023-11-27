# convertit un masque décimal en CIDR ou l'inverse
import ipaddress

def decimal_mask_to_cidr(mask):
    try:
        # Convertit le masque décimal en objet IP
        ip = ipaddress.IPv4Network(f"0.0.0.0/{mask}")
        # Affiche la notation CIDR
        return f"Le masque {mask} en notation CIDR est : /{ip.prefixlen}"
    except ValueError as e:
        return f"Masque non valide: {e}"

def cidr_to_decimal_mask(cidr):
    try:
        # Crée un réseau avec un masque CIDR
        network = ipaddress.IPv4Network(f"0.0.0.0/{cidr}")
        # Affiche le masque en format décimal
        return f"La notation CIDR /{cidr} correspond au masque : {network.netmask}"
    except ValueError as e:
        return f"Notation CIDR non valide: {e}"

# Exemple d'utilisation
choice = input("Choisissez (1) pour convertir de décimal à CIDR, (2) pour convertir de CIDR à décimal: ")

if choice == '1':
    mask = input("Entrez le masque de sous-réseau en format décimal (ex: 255.255.255.0): ")
    print(decimal_mask_to_cidr(mask))
elif choice == '2':
    cidr = input("Entrez la notation CIDR (ex: 24): ")
    print(cidr_to_decimal_mask(cidr))
else:
    print("Choix non valide.")
