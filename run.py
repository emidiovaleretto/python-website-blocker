from datetime import datetime, timedelta
from decouple import config


def get_list_of_blocked_websites():
    """
    This function returns list of blocked websites.
    """
    with open(config("BLOCKED_SITES"), "r") as f:
        blocked_websites = f.readlines()

    return blocked_websites


def website_blocker():
    """
    This is the main function.
    It denies access to websites permanently
    or by schedule time.
    """
    if datetime.now() < end_date:
        print("Access denied")
        with open(hosts_path, "r+") as file:
            content = file.read()
            for site in sites_to_block:
                if site not in content:
                    file.write(redirect_to + " " + site + "\n")

    else:
        print("Access granted")
        with open(hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in sites_to_block):
                    file.write(line)
            file.truncate()


end_date = datetime.now() + timedelta(days=365)
sites_to_block = get_list_of_blocked_websites()

hosts_path = config("HOSTS_PATH")
redirect_to = config("REDIRECT_TO")

if __name__ == "__main__":
    website_blocker()
