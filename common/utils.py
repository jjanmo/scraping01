from pathlib import Path


def set_path(keyword):
    if 'https' in keyword or 'http' in keyword:
        splited = keyword.split('://')[1].split('.')
        path = splited[0] if len(splited) == 2 else splited[1]
    else:
        path = keyword

    Path(f'screenshots/{path}').mkdir(parents=True, exist_ok=True)

    return path
