"""Keep this snapshot's website/emulator links local and discourage indexing."""
import os
from pathlib import Path
import sys
from urllib.parse import urlsplit

output = Path(sys.argv[1])
base = os.environ['PREVIEW_BASE_URL'].rstrip('/')
production = 'https://ventilastation.protocultura.net'
count = 0
for path in output.rglob('*.html'):
    text = path.read_text()
    text = text.replace(production + '/', base + '/')
    # The new documentation pages are still on the unmerged review branch.
    text = text.replace('github.com/ventilastation/vsdk/blob/main/',
                        'github.com/ventilastation/vsdk/blob/docs/unified-documentation/')
    text = text.replace('github.com/ventilastation/vsdk/tree/main/',
                        'github.com/ventilastation/vsdk/tree/docs/unified-documentation/')
    text = text.replace('github.com/ventilastation/vsdk/edit/main/',
                        'github.com/ventilastation/vsdk/edit/docs/unified-documentation/')
    if '<head>' in text:
        text = text.replace('<head>', '<head><meta name="robots" content="noindex, nofollow">', 1)
    path.write_text(text)
    count += 1
(output / 'robots.txt').write_text('User-agent: *\nDisallow: ' + urlsplit(base).path + '/\n')
(output / 'CNAME').unlink(missing_ok=True)
for name in ('index.html', 'en/index.html', 'docs/index.html', 'emulator/index.html'):
    assert (output / name).is_file(), name
for name in ('index.html', 'en/index.html'):
    text = (output / name).read_text()
    prefix = urlsplit(base).path
    assert 'href="' + prefix + '/docs/"' in text, name
    assert 'href="' + prefix + '/emulator/"' in text, name
assert base + '/' in (output / 'docs/index.html').read_text()
print(f'Prepared {count} preview HTML pages at {base}/')
