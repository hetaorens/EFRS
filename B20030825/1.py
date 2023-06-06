import hashlib

def generate_search_token(keyword):
    sha1_hash = hashlib.sha1(keyword.encode())
    search_token = sha1_hash.hexdigest()
    return search_token


search_token_map = {}

def search_token_by_keyword(keyword, search_token_map):
    if keyword in search_token_map:
        return search_token_map[keyword]
    else:
        return None


keyword = "keyword2"
search_token = search_token_by_keyword(keyword, search_token_map)
if search_token:
    print(f"Search Token for '{keyword}': {search_token}")
else:
    print(f"No Search Token found for '{keyword}'")

