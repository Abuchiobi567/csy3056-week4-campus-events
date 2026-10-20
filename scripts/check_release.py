import sys
import zipfile
from pathlib import Path

REQUIRED = ['app.py', 'static/style.css']
FORBIDDEN = ['instance/bookings.sqlite3']


def has_member(names, target):
    return any(n == target or n.endswith('/' + target) for n in names)


def main():
    zips = sorted(Path('dist').glob('*.zip'))
    if not zips:
        print('FAIL: no release ZIP found in dist/')
        return 1
    failed = False
    for zip_path in zips:
        with zipfile.ZipFile(zip_path) as z:
            names = [n.replace('\\', '/') for n in z.namelist()]
        problems = []
        for item in REQUIRED:
            if not has_member(names, item):
                problems.append(f'missing {item}')
        for item in FORBIDDEN:
            if has_member(names, item):
                problems.append(f'contains forbidden file {item}')
        if problems:
            failed = True
            print(f'FAIL: {zip_path.name}: ' + '; '.join(problems))
        else:
            print(f'OK: {zip_path.name} passed release integrity checks')
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main())