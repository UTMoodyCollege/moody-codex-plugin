"""Run with python3 test_check_moody_html.py; no extra dependencies."""
from check_moody_html import Checker

def issues(html):
    checker = Checker()
    checker.feed(html)
    checker.close()
    return checker.issues

assert not issues('<h2>Resources</h2><div class="ut-display-grid ut-cols-1 md:ut-cols-2 ut-gap-6"><p><a class="ut-btn" href="/apply">Apply to Moody</a></p><img src="/photo.jpg" alt="Students in the newsroom"></div>')
for html, message in [
    ('<p class="ut-made-up">Copy</p>', 'unknown class'),
    ('<p style="color:red">Copy</p>', 'inline style'),
    ('<script>alert(1)</script>', 'not allowed'),
    ('<img src="/photo.jpg">', 'missing alt'),
    ('<p class="ut-border-radius-lg">Copy</p>', 'rounded corners'),
    ('<p class="xx:ut-cols-2">Copy</p>', 'unknown breakpoint'),
]:
    assert any(level == 'ERROR' and message in text for level, _, text in issues(html)), html
assert any(level == 'WARN' and 'stripped' in text for level, _, text in issues('<section aria-label="Details"><h2>Details</h2></section>'))
print('PASS: valid fragment, invalid classes/styles/tags/images, and CKEditor warning.')

