import re

def check_mac_address(mac_str):
    # Vérifie le format de l'adresse MAC
    if not re.match("[0-9a-fA-F]{2}([-:][0-9a-fA-F]{2}){5}$", mac_str):
        return f"{mac_str} n'est pas une adresse MAC valide."

    # Extrait le second caractère du premier octet de l'adresse MAC
    second_char = mac_str[1].lower()

    # Détermine si l'adresse est universelle ou locale
    if second_char in '048159cCdD':
        ul_status = "Universelle"
    else:
        ul_status = "Locale"

    # Détermine si l'adresse est unicast ou multicast
    if second_char in '02468aAcCeE':
        ig_status = "Unicast"
    else:
        ig_status = "Multicast"

    return f"{mac_str} est une adresse MAC {ul_status}, {ig_status}."

# Exemple d'utilisation
mac_to_test = input("Entrez une adresse MAC pour la tester: ")
result = check_mac_address(mac_to_test)
print(result)
