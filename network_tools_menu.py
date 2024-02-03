import subprocess

def main_menu():
    while True:
        print("\nMenu Principal")
        print("1. Vérificateur d'adresse IPv4")
        print("2. Convertisseur de masque de sous-réseau")
        print("3. Calculateur de détails du réseau IPv4")
        print("4. Calculateur de plage CIDR à partir d'une plage complète")
        print("5. Planificateur de sous-réseaux")
        print("6. Vérificateur d'adresse MAC")
        print("7. Calculateur de plage IPv6 à partir d'une adresse et d'un masque")
        print("8. Constructeur de matrice de communication IPv4 (Beta)")
        print("0. Quitter")

        choice = input("Entrez votre choix : ")

        if choice == '1':
            subprocess.run(["python3", "ipv4_address_checker.py"])
        elif choice == '2':
            subprocess.run(["python3", "subnet_mask_converter.py"])
        elif choice == '3':
            subprocess.run(["python3", "network_details_calculator.py"])
        elif choice == '4':
            subprocess.run(["python3", "range_to_cidr_calculator.py"])
        elif choice == '5':
            subprocess.run(["python3", "subnet_planner.py"])
        elif choice == '6':
            subprocess.run(["python3", "mac_address_checker.py"])  
        elif choice == '7':
            subprocess.run(["python3", "calculate_ipv6_range.py"])   
        elif choice == '8':
            subprocess.run(["python3", "communication_matrix_builder.py"]) 
        elif choice == '0':
            break
        else:
            print("Choix non valide, veuillez réessayer.")

if __name__ == "__main__":
    main_menu()
