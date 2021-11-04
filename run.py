from datetime import datetime, timedelta
from decouple import config


def get_list_of_blocked_websites():
    """
    This function returns list of blocked websites.
    """
    with open("blocked_sites.txt", "r") as f:
        blocked_websites = f.readlines()

    return blocked_websites


end_date = datetime.now() + timedelta(days=365)
sites_to_block = get_list_of_blocked_websites()

hosts_path = config("HOSTS_PATH")
redirect_to = config("REDIRECT_TO")
