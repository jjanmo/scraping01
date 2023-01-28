from pathlib import Path


def set_path(url):
    splited = url.split('://')[1].split('.')
    path = splited[0] if len(splited) == 2 else splited[1]
    Path(f'screenshots/{path}').mkdir(parents=True, exist_ok=True)
    
    return path
