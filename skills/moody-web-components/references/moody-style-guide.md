# Moody web style reference

Source: [Moody Style Guide](https://moody.utexas.edu/style-guide). Checked October 7, 2026. Recheck for exact current styling.

- Use the current catalog's approved colors and surface pairings; older references include retired bright/teal choices. Do not infer approval from an old class name.
- Type sizes: `ut-text-xs`, `sm`, `base`, `lg`, `xl`, `2xl`, `3xl`, `4xl`, `5xl`. Weights: `ut-font-weight-{light,normal,medium,semibold,bold,black}`. Fonts: `ut-font-{sans,serif}`.
- Responsive prefixes are viewport-based: `sm:` 576px, `md:` 768px, `lg:` 992px, `xl:` 1200px. Hero/Card Builder use separate container breakpoints: 600px and 900px.
- Layout includes `ut-display-*`, `ut-cols-{1..6}`, `ut-split-*`, flex, alignment and sizing utilities. These CSS grids are distinct from Layout Builder section regions.
- Spacing uses `ut-{p,m,...}-{0..32}` at .25rem per step; margins also support `auto`. Use documented gap values.
- Media utilities control crop/fit, aspect and position. Apply to the actual image, or use managed Media controls.
- Surfaces: `ut-surface-{white,paper,charcoal,orange}`. Current components use square corners.

Expand class-family notation into actual names. Read the live exact-class table before generating markup; these utilities require the site's stylesheet. See [Layout Builder context](layout-builder.md) for structured components and section widths.
