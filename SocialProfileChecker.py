import requests
import os

class TextColor:
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    END: str = '\033[0m'

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_social_profile(platform, username):
    url_formats = {
        "instagram": f"https://www.instagram.com/{username}/",
        "twitter": f"https://twitter.com/{username}/",
        "youtube": f"https://www.youtube.com/user/{username}/",
        "linkedin": f"https://www.linkedin.com/in/{username}/",
        "facebook": f"https://www.facebook.com/{username}/",
        "snapchat": f"https://www.snapchat.com/add/{username}/",
        "reddit": f"https://www.reddit.com/user/{username}/",
        "tiktok": f"https://www.tiktok.com/@{username}/",
        "pinterest": f"https://www.pinterest.com/{username}/",
        "ifunny": f"https://ifunny.co/user/{username}/",
        "whatsapp": f"https://wa.me/{username}/",
        "twitch": f"https://www.twitch.tv/{username}/",
        "github": f"https://github.com/{username}/",
        "gitlab": f"https://gitlab.com/{username}/",
        "bitbucket": f"https://bitbucket.org/{username}/",
        "medium": f"https://medium.com/@{username}/",
        "quora": f"https://www.quora.com/profile/{username}/",
        "stackoverflow": f"https://stackoverflow.com/users/{username}/",
        "discord": f"https://discord.com/users/{username}/",
        "spotify": f"https://open.spotify.com/user/{username}/",
        "soundcloud": f"https://soundcloud.com/{username}/",
        "vimeo": f"https://vimeo.com/{username}/"
    }
    url = url_formats.get(platform)
    if url:
        response = requests.get(url)
        if response.status_code == 200:
            return url
        elif response.status_code == 404:
            return 404

def main():
    clear_terminal()

    text = "      _   ____     ____    ___     ___    ____    _____\n"\
           "     | | |  _ \\   / ___|  / _ \\   / _ \\  |  _ \\  |__  /\n"\
           "  _  | | | |_) | | |     | | | | | | | | | | | |   / / \n"\
           " | |_| | |  __/  | |___  | |_| | | |_| | | |_| |  / /_ \n"\
           "  \\___/  |_|      \\____|  \\___/   \\___/  |____/  /____|\n"

    print(TextColor.BLUE + text + TextColor.END)
    print(TextColor.BLUE + "Criado por JpCooDz" + TextColor.END)
    print(TextColor.BLUE + "Dica: Evite inserir espaços no nome de usuário." + TextColor.END)
    print(TextColor.BLUE + "Version 2.0" + TextColor.END)
    print(TextColor.BLUE + "___________________________________________________")

    platforms = ["instagram", "twitter", "youtube", "linkedin", "facebook", "snapchat", "reddit", "tiktok", "pinterest",
                 "ifunny", "whatsapp", "twitch", "github", "gitlab", "bitbucket", "medium", "quora", "stackoverflow",
                 "discord", "spotify", "soundcloud", "vimeo"]

    username = input(TextColor.YELLOW + "Digite o nome de usuário: " + TextColor.END)
    profile_found = False

    for platform in platforms:
        result = check_social_profile(platform, username)

        if result == 404:
            print(TextColor.RED + f"Perfil não encontrado no {platform.capitalize()} (Status 404)" + TextColor.END)
        elif isinstance(result, str):
            print(TextColor.GREEN + f"Perfil encontrado no {platform.capitalize()}: {result}" + TextColor.END)
            profile_found = True

if __name__ == "__main__":
    main()
