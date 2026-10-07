# Moody Style Guide: HTML Reference

Condensed from https://moody.utexas.edu/style-guide (captured 2026-10-07). The full machine-readable allowlist, with the CSS each class produces, is `scripts/allowed_classes.json`. If the live guide disagrees with this file, the live guide wins.

## Contents
1. Brand colors
2. Typography
3. Base HTML elements
4. Color classes
5. Surfaces
6. Layout utilities
7. Sizing & spacing
8. Media
9. Position
10. Components: buttons, CTA links, tables, figures
11. Don'ts

## 1. Brand colors

| Name | Hex | Typical use |
|---|---|---|
| Burnt Orange | `#bf5700` | Primary accent, buttons, CTA. Use with white text only on large/bold text; prefer `ut-surface-orange` (`#a04400`) for text blocks, which passes contrast |
| Dark Burnt Orange | `#9d4700` / `#a04400` | Hover states, orange surface |
| Charcoal | `#333f48` | Default body text, dark surface |
| Limestone | `#d6d2c4` | Neutral accent background |
| Paper | `#f2f1ed` | Light card / panel background |
| Moody Gray | `#9daeb7` | Accent; too light for body text on white |
| Black / White | `#000` / `#fff` | |

## 2. Typography

- Sans: `ut-font-sans` (LibreFrank, Arial fallback): default UI/body.
- Serif: `ut-font-serif` (CharisSil, Georgia fallback): editorial accents, pull quotes.
- Size: `ut-text-{xs 12px, sm 14px, base 16px, lg 18px, xl 20px, 2xl 24px, 3xl 30px, 4xl 36px, 5xl 48px}`
- Weight: `ut-font-weight-{light 300, normal 400, medium 500, semibold 600, bold 700, black 900}`
- Align: `ut-text-{left,center,right,start,end}`
- Reading width: `ut-measure-{narrow 45ch, standard 65ch, wide 80ch, none}`. Use `ut-measure-standard` for long-form copy.

Change visual size with classes, not by picking a different heading level. Heading levels carry document structure for screen readers.

## 3. Base HTML elements (already styled, no classes needed)

h1–h6, p, a (underlined in copy), ul, ol, blockquote (left border), pre, code, img, table, button.

## 4. Color classes

Text: `text-ut-black`, `text-ut-charcoal`, `text-ut-white`, `text-ut-burntorange`, `text-ut-limestone`, `text-ut-moody-gray`

Background: `bg-ut-black`, `bg-ut-white`, `bg-ut-burntorange`, `bg-ut-limestone`, `bg-ut-moody-gray`

Extended neutral backgrounds (`utexas-bg-<hex>`):
- Cool grays (light→dark): `f9fafb e6ebed c4cdd4 7d8a92 5e686e 3e4549`
- Grays: `ebeced c2c5c8 858c91 1f262b`
- Warm/limestone (light→dark): `fbfbf9 f2f1ed e6e4dc aba89e 807e76 56544e`
- Dark orange: `9d4700`

Approved pairings (the style guide demos these):
- Dark text (`text-ut-black` / charcoal) on: white, limestone, and the light `utexas-bg-*` (f9fafb, e6ebed, c4cdd4, ebeced, c2c5c8, fbfbf9, f2f1ed, e6e4dc, aba89e)
- White text on: black, burnt orange, moody gray (large text only), and the dark `utexas-bg-*` (7d8a92, 5e686e, 3e4549, 9d4700, 858c91, 1f262b, 807e76, 56544e)

Avoid `text-ut-burntorange` for small body text on paper/limestone, and `text-ut-moody-gray` or `text-ut-limestone` on white, since contrast is too low.

## 5. Surfaces (preferred for colored blocks)

Each sets an approved foreground/background pair in one class:

| Class | Background | Text |
|---|---|---|
| `ut-surface-white` | #fff | #333f48 |
| `ut-surface-paper` | #f2f1ed | #333f48 |
| `ut-surface-charcoal` | #333f48 | #fff |
| `ut-surface-orange` | #a04400 | #fff |

## 6. Layout utilities

All support `sm:` `md:` `lg:` `xl:` prefixes (mobile-first; later breakpoints override earlier ones regardless of class order). Use one value per property per breakpoint.

- Display: `ut-display-{block,inline-block,flex,inline-flex,grid,none}`. `ut-display-none` also hides content from screen readers, so never hide essential content.
- Grid columns: `ut-cols-{1..6}` (equal columns)
- Splits (two/three-column grids): `ut-split-{halves,thirds,one-two,two-one,one-three,three-one}`
- Flex: `ut-flex-{row,column,wrap,nowrap}`
- Align: `ut-items-{start,center,end,stretch}`, `ut-self-{start,center,end,stretch,auto}`
- Justify: `ut-justify-{start,center,end,between,around}`
- Gap (on the grid/flex parent): `ut-gap-{0,1,2,3,4,6,8,12,16}` (×0.25rem)

Note: viewport breakpoints are different from Hero/Card Builder container queries (tablet 600px, desktop 900px). Don't mix them up.

## 7. Sizing & spacing

- Width: `ut-w-{auto,full,half,third,two-thirds,quarter,three-quarters}`, `ut-min-w-0`
- Height: `ut-h-{auto,full}` (full needs a parent with a defined height)
- Padding (inside): `ut-{p,pt,pr,pb,pl,px,py}-{0..32}`, each step 0.25rem (ut-p-4 = 1rem, ut-p-8 = 2rem)
- Margin (outside): `ut-{m,mt,mr,mb,ml,mx,my}-{0..32}`, plus `-auto` (e.g. `ut-mx-auto` to center)
- Overflow: `ut-overflow-{visible,hidden,auto}`

## 8. Media

Put these on the `<img>` itself, not a `drupal-media` wrapper (for nested managed media, use the Media settings instead).
- Fit: `ut-object-{cover,contain,fill,none}`
- Focal point: `ut-object-{left,center,right}-{top,center,bottom}`
- Aspect: `ut-aspect-{square 1:1, landscape 4:3, wide 16:9, portrait 3:4, auto}`

## 9. Position

`ut-position-{static,relative,absolute,sticky}`, `ut-{top,right,bottom,left,inset}-{0,half,auto}`, `ut-translate-{center,none}`, `ut-layer-{0,1,2}`.
Prefer grid/flex for text. Never use positioning to obscure navigation or change visual reading order.

## 10. Components

**Buttons** (on `<a>` for links, `<button>` for actions):
- `ut-btn` primary burnt orange; `ut-btn ut-btn--secondary` outline; size modifiers `ut-btn--small`, `ut-btn--large`
```html
<a class="ut-btn" href="/admissions/apply">Apply to Moody</a>
<a class="ut-btn ut-btn--secondary" href="/visit">Plan a visit</a>
```

**CTA links**: uppercase, bold text link:
- `ut-cta-link`, with an optional icon modifier: `ut-cta-link--angle-right`, `ut-cta-link--external` (off-site), `ut-cta-link--lock` (login required), `ut-cta-link--darker`
```html
<a class="ut-cta-link ut-cta-link--angle-right" href="/news">More Moody news</a>
```

**Tables**:
```html
<table class="tablesaw tablesaw-stack">
  <caption>Fall 2026 application deadlines</caption>
  <thead><tr><th scope="col">Program</th><th scope="col">Deadline</th></tr></thead>
  <tbody><tr><td>M.A. Journalism</td><td>Dec. 1</td></tr></tbody>
</table>
```
Add `ut-fit-table` to shrink a narrow table to its content width.

**Figures**: `align-left` / `align-right` float the figure at 48% width (full width under 768px); `align-center` centers it.
```html
<figure class="align-right">
  <img src="/sites/default/files/example.jpg" alt="Students editing video in the Moody newsroom">
  <figcaption>Students in the Moody newsroom.</figcaption>
</figure>
```

**Blockquote**: plain `<blockquote><p>…</p></blockquote>`; add attribution in a following `<p>` or `<footer>` inside it.

**Borders**: `ut-border-width-{none,thin,medium,thick}`, `ut-border-burntorange`.

## 11. Don'ts

- Inline `style=""`, `<style>`, `<script>`, `<iframe>` embeds not provided by the editor
- Classes not in the catalog (Tailwind/Bootstrap names like `rounded`, `shadow`, `btn-primary`, `col-md-6`, `container`)
- Rounded corners (`ut-border-radius-*` other than `none`) and the retired teal/bright palette
- Hero/Card Builder internals (`mhb-*`, `mcb-*`): not standalone utilities
- Skipping heading levels, `<h1>` in body content, "click here" link text, images without `alt`
