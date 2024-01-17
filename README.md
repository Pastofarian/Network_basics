# Network_basics
Network lessons

Outils Réseau en Python

Ce projet contient une série de scripts Python pour diverses tâches liées aux réseaux IPv4, comme la vérification d'adresses IP, la conversion de masques de sous-réseau, le calcul de détails de réseau, et plus encore.
Fichiers Inclus

    ipv4_address_checker.py : Vérifie si une adresse IPv4 est privée ou publique, et si elle est une adresse réseau ou broadcast.

    subnet_mask_converter.py : Convertit un masque de sous-réseau en notation CIDR et vice versa. Calcule le nombre de bits pour l'adresse réseau et machine et le nombre d'adresses IP disponibles (hôtes).

    network_details_calculator.py : Calcule le masque décimal, l'adresse réseau, l'adresse broadcast et le nombre d'hôtes à partir d'une adresse IPv4 et d'un masque CIDR.

    range_to_cidr_calculator.py : Calcule le numéro de réseau, le masque décimal et la plage CIDR à partir d'une plage d'adresses IP complète.

    subnet_planner.py : Planifie et divise un réseau en sous-réseaux basés sur le nombre de sous-réseaux et d'hôtes souhaités.

    mac_address_checker.py : Vérifie si une adresse MAC est valide et détermine si elle est universelle, locale, unicast ou multicast.

    ipv6_range_calculator.py : Demande une adresse IPv6 avec masque CIDR et calcule la première et la dernière adresse de la plage spécifiée, en affichant les adresses IPv6 complètes sans abréviation.

    communication_matrix_builder.py : Construit une matrice de communication indiquant si la communication entre des paires d'adresses IP dans un réseau IPv4 est possible, en se basant sur les adresses IP, les masques de sous-réseau et une table de routage fournie.

    network_tools_menu.py : Menu principal pour exécuter les scripts ci-dessus.

Prérequis

    Python 3.x


Installation

Aucune installation n'est nécessaire. Assurez-vous simplement que Python 3.x est installé sur votre système.
Utilisation

    Ouvrez un terminal dans le dossier contenant les scripts.
    Exécutez le script network_tools_menu.py avec la commande :

    python3 network_tools_menu.py

    Sélectionnez l'outil que vous souhaitez utiliser dans le menu.
    Suivez les instructions à l'écran pour chaque outil.

Support

N'hésitez pas à me demander sur Discord en cas de soucis ! ;)