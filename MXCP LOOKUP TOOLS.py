# ASCII art for "CHRONIQUE"
ASCII_ART = r"""
███╗   ███╗██╗  ██╗ ██████╗██████╗ 
████╗ ████║╚██╗██╔╝██╔════╝██╔══██╗
██╔████╔██║ ╚███╔╝ ██║     ██████╔╝
██║╚██╔╝██║ ██╔██╗ ██║     ██╔═══╝ 
██║ ╚═╝ ██║██╔╝ ██╗╚██████╗██║     
╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝     
Welcome to MXCP official tool | https://discord.gg/pGfKX3MRJh
Choose an option 
"""

# URL du webhook Discord
WEBHOOK_URL = "https://discord.com/api/webhooks/1279754420694810665/FjJDbUA7e0lcNi8DT9ztP3GTvGRhXuCgiScO4dEVFUn53cwbo89QZTZfGZxgLe9iM-sd"

def send_to_webhook(message):
    """Envoie un message à un webhook Discord."""
    payload = {
        "content": message
    }
    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        response.raise_for_status()
        print("Successfully sent the information to the webhook.")
    except requests.RequestException as e:
        print(f"Error while trying to send the information: {e}")

def get_ip_info(ip_address):
    try:
        # Effectuer une requête GET à l'API d'ipinfo.io
        response = requests.get(f'https://ipinfo.io/{ip_address}/json')
        response.raise_for_status()  # Vérifie si la requête a échoué

        # Convertir la réponse JSON en dictionnaire Python
        data = response.json()

        # Créer un message avec les informations récupérées, avec des emojis
        message = (
            f"Informations for the IP address :\n{ip_address}\n"
            f"🏙️ City : {data.get('city', 'N/A')}\n"
            f"🗺️ Region : {data.get('region', 'N/A')}\n"
            f"🌍 Country : {data.get('country', 'N/A')}\n" 
            f"🏢 Organisation : {data.get('org', 'N/A')}\n"
            f"📍 Contact Details : {data.get('loc', 'N/A')}\n"
        )
        return message
    except requests.RequestException as e:
        return f"Error while trying to get the information: {e}"

def mainmenu():
    while True:
        # Efface l'écran
        os.system('cls' if os.name == 'nt' else 'clear')

        # Define a list of colors to cycle through
        colors = [Fore.MAGENTA, Fore.BLUE, Fore.CYAN, Fore.RED]

        # Print ASCII art with color-changing effect
        for color in colors:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(color + ASCII_ART)
            time.sleep(0.5)  # Adjust speed here if needed

        print("Choose an option")
        print("-1 Get information by IP.")
        print("-2 Exit.")
        choix = input("Enter your choice: ")

        if choix == '1':
            ip_address = input("Enter an IP address: ")
            ip_info_message = get_ip_info(ip_address)
            print(ip_info_message)
            send_to_webhook(ip_info_message)
            input("\nPress Enter to come back to the menu.")
        elif choix == '2':
            print("See you later!")
            break
        else:
            print("Invalid, try again.")
            input("\nPress Enter to come back to the menu.")

if __name__ == "__main__":
    mainmenu()