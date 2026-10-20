import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from app_version import APP_VERSION


def git_commit():
    commit = os.environ.get('GIT_COMMIT')
    if commit:
        return commit
    try:
        result = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=ROOT,
                                capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except Exception:
        return 'unknown'


def main():
    lines = [
        f'Application version: {APP_VERSION}',
        f"Build number: {os.environ.get('BUILD_NUMBER', 'local')}",
        f'Git commit: {git_commit()}',
        f"Build date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
    ]
    (ROOT / 'build-info.txt').write_text('\n'.join(lines) + '\n')
    print('\n'.join(lines))


if __name__ == '__main__':
    main()