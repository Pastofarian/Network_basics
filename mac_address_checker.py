import re

def check_mac_address(mac_str):
    # Vérifie le format de l'adresse MAC
    if not re.match("[0-9a-fA-F]{2}([-:][0-9a-fA-F]{2}){5}$", mac_str):
        return f"{mac_str} n'est pas une adresse MAC valide."
    
    # Convertit le premier octet en valeur binaire
    first_byte_binary = format(int(mac_str[:2], 16), '08b')
    
    # Analyse les bits pour déterminer unicast/multicast (bit le plus à droite) et unique/locale (deuxième bit le plus à droite)
    ul_bit = first_byte_binary[-2]  # Unique/Locale bit
    ig_bit = first_byte_binary[-1]  # Unicast/Multicast bit

    ul_status = "Locale" if ul_bit == '1' else "Unique"
    ig_status = "Multicast" if ig_bit == '1' else "Unicast"

    # Ajoute la représentation binaire du premier octet dans la réponse
    return f"{mac_str} est une adresse MAC {ul_status} et {ig_status}. {mac_str[:2]} en binaire = {first_byte_binary}."

# Exemple d'utilisation
mac_to_test = input("Entrez une adresse MAC pour la tester: ")
result = check_mac_address(mac_to_test)
print(result)
