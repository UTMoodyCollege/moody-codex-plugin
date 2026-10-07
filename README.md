# Moody Web Builder

A skills-only Codex plugin for designing and reviewing web components for Moody College of Communication at The University of Texas at Austin. It recommends Drupal Layout Builder blocks, provides field-by-field specifications, and checks Basic block HTML against the Moody utility catalog.

Independent guidance; not an official university certification. The plugin requires the target site's styles to render its HTML. Its checker is editorial lint, not a sanitizer or accessibility certification.

## Source and parity

The Claude equivalent is [UTMoodyCollege/moody-claude-skills](https://github.com/UTMoodyCollege/moody-claude-skills). This release incorporates its v1.3.0 snapshot at commit `2248bc42062ca495f082beb21c49e9d346670662`. See [provenance and limitations](skills/moody-web-components/references/upstream.md). The Codex version also retains a broader Layout Builder catalog and checks site availability before recommending blocks.

Use [AGENTS.md](AGENTS.md) when maintaining this repository. Updates are deliberate snapshots; neither the Claude repository nor GitHub commits automatically update the account-installed plugin.

## Use

Download the ZIP from [Releases](https://github.com/UTMoodyCollege/moody-codex-plugin/releases). It contains one `moody-web-builder/` plugin directory. For an account installation, use the plugin import/update flow available in your host. The existing account plugin's access and sharing are separate from this public source repository.

Example requests:

- “Plan a Moody program page with the appropriate blocks and view modes.”
- “Write a Basic block callout using Moody's documented classes.”
- “Review this HTML for styling and editor compatibility.”

## Check and package

Requires Python 3; no additional dependencies.

```sh
python3 skills/moody-web-components/scripts/test_check_moody_html.py
python3 scripts/package.py
python3 skills/moody-web-components/scripts/check_moody_html.py fragment.html
```

The package script validates manifests and referenced icons, runs the checker regression test, and writes `dist/moody-web-builder-VERSION.zip`. Only manifests, assets and skills are included. GitHub releases and OpenAI plugin-directory submissions are separate; this repository does not claim directory approval or submission readiness.

## Maintenance

Compare the latest Claude skill, review what changed, update appropriate references and scripts, and record the upstream commit. Verify current site behavior where possible. Run checks, review files for sensitive information, bump both manifests, and publish a tagged release. Report live checks that were not performed.

No license has been selected for this repository. Source visibility does not itself grant an open-source license.
