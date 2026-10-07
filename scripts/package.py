"""Validate and package the plugin using only Python's standard library."""
import json
import subprocess
import sys
import zipfile
from pathlib import Path

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / 'plugin.json').read_text())
legacy = json.loads((root / '.codex-plugin/plugin.json').read_text())
assert manifest['name'] == legacy['name'] == 'moody-web-builder'
assert manifest['version'] == legacy['version']
interface = manifest['extensions']['com.openai']['interface']
assert len(interface['shortDescription']) <= 30
assert interface['defaultPrompt'] == legacy['interface']['defaultPrompt']
for key in ('logo', 'composerIcon', 'logoDark', 'composerIconDark'):
    asset = (root / interface[key]).resolve()
    assert asset.is_relative_to(root) and asset.is_file()
subprocess.run([sys.executable, str(root / 'skills/moody-web-components/scripts/test_check_moody_html.py')], check=True)
files = [root / 'plugin.json', root / '.codex-plugin/plugin.json']
for directory in ('assets', 'skills'):
    files.extend(p for p in (root / directory).rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix not in ('.pyc', '.pyo'))
for path in files:
    assert not path.is_symlink()
    assert path.suffix in ('.json', '.svg', '.md', '.py'), path
archive = root / 'dist' / f"{manifest['name']}-{manifest['version']}.zip"
archive.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as z:
    for path in sorted(files):
        z.write(path, str(Path(manifest['name']) / path.relative_to(root)))
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    assert len(z.namelist()) == len(files)
print(archive)
