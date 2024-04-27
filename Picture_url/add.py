import re
import read

# url = read.filtered_url()

def modify_url(url):
    print(url)
    pattern = r'https://wallhaven.cc/w/(.*)'
    match = re.search(pattern, url)
    if match:
        code = match.group(1)
        first_two_letters = code[:2]
        return f'https://w.wallhaven.cc/full/{first_two_letters}/wallhaven-{code}.jpg'
    else:
        return None
    


# print(modify_url(url))
