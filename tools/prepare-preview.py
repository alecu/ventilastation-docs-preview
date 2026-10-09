"""Keep this snapshot's website/emulator links local and discourage indexing."""
import os
import re
from pathlib import Path
import sys
from urllib.parse import urlsplit

output = Path(sys.argv[1])
base = os.environ['PREVIEW_BASE_URL'].rstrip('/')
production = 'https://ventilastation.protocultura.net'
prefix = urlsplit(base).path
count = 0
for path in output.rglob('*.html'):
    text = path.read_text()
    text = text.replace(production + '/', base + '/')
    # Content Markdown contains root-relative links; Jekyll only rebases the
    # Liquid template links. Keep both kinds under this project site's path.
    def rebase(match):
        name, quote, value = match.groups()
        if value == prefix or value.startswith(prefix + '/'):
            return match.group(0)
        return name + '=' + quote + prefix + value + quote
    text = re.sub(r'''\b(href|src|action)=([\"'])(/(?!/)[^\"']*)\2''', rebase, text)
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
    assert 'href="' + prefix + '/docs/"' in text, name
    assert 'href="' + prefix + '/docs/guides/desktop.html"' in text, name
    assert 'href="' + prefix + '/emulator/"' not in text, name
    assert 'href="' + prefix + '/docs/guides/browser.html"' not in text, name
    assert 'href="/docs/' not in text, name
assert base + '/' in (output / 'docs/index.html').read_text()
print(f'Prepared {count} preview HTML pages at {base}/')
