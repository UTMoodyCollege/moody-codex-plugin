# Moody Layout Builder Blocks

Reference for the custom blocks editors add in Layout Builder (**Layout → Add block**) on moody.utexas.edu. Sources: the add-block forms on the test site, rendered markup on production pages, and the Moody block usage report (`/admin/reports/moody-block-reports`), all captured 2026-10-07. Usage counts are placements across the site and show which patterns are well-tested.

Every block has a required admin **Title**, which isn't shown unless **Display title** is checked. When it is checked, the title renders as `<h2 class="block-headline-h2 ut-h3">` above the block. This is the most reliable way to give a block a real section heading. Every block also offers the same **Block Styles**: borders (with or without background), readable width, and add/remove/increase top and bottom margin.

## Contents
1. Sections (the container blocks sit in)
2. Basic block
3. Moody Hero
4. Moody Flex Grid
5. Moody Showcase
6. Utexas Promo Unit
7. Utexas Featured Highlight
8. Moody Flex Color Blocks
9. Moody Accordion
10. Moody Contact Info
11. Moody Quotation
12. Utexas Flex Content Area
13. Utexas Promo List
14. Utexas Image Link
15. Moody Focus Areas
16. Call to Action (legacy)
17. Page-template field blocks
18. Shared link options

---

## 1. Sections

Blocks live inside sections. Choose the section first.

| Layout | Column proportions |
|---|---|
| One column | — |
| Two column | 50/50, 33/67, 67/33, 25/75, 75/25 |
| Three column | 25/50/25, 33/34/33, 25/25/50, 50/25/25 |
| Four column | equal |

Section options:
- **Section width:** Readable, Container or Full width of page.
- **Background:** a color or an image (1500×500 recommended, optional blur). Color options are Transparent, Limestone Light `#f2f1ed`, Light shading `#e6ebed`, Charcoal `#c2c5c8`, Limestone Dark `#807e76`, Dark shading `#5e686e`, Burnt Orange `#9d4700`, plus Turtlepond, Turquoise and Bluebonnet.
- **Spacing and width:** no padding between columns, increase or reduce top margin, constrain content to container, and disable background accent filtering.

Recommend only the neutral and burnt-orange backgrounds. Turtlepond, Turquoise and Bluebonnet are the bright accent palette the style guide says not to use.

## 2. Basic block (`inline_block:basic`) · 860 placements on 332 pages

- **Input:** one Body field (CKEditor 5, Flex HTML). View modes "full" and "default" render the same.
- **Output:** `.ut-copy` with whatever HTML you write. Everything in `style-guide.md` and `recipes.md` applies.
- **Use for:** long-form copy, mixed content, custom layouts built from `ut-*` utilities (stat rows, callouts, link lists, tables), and anything no structured block fits.
- **Avoid when** a structured block fits: a hero, card grid, image + text row, or FAQ. Structured blocks give editors managed images, keep the design consistent site-wide, and are easier for non-technical editors to update.

## 3. Moody Hero (`inline_block:moody_hero`) · 150 placements

**Inputs**
- **Image:** one item, required. Cropped to 87:47; upload at least 2280×1232. There's a "Disable image size optimization" checkbox for GIFs.
- **Text:** Heading, Subheading (140 characters at most), Caption and Credit.
- **Call to action:** URL, link text, new-window option and icon. See §12.
- **Text color** (styles 6, 7 and 8): white, orange or charcoal.
- **Image overlay** (styles 6, 7 and 8): none, orange, charcoal, darker orange or darker charcoal.
- **Text position** (styles 7 and 8): centered, top-left, top-right, bottom-left or bottom-right.

**View modes.** Every style is also offered as `_left` / `_right` / center image anchoring, which sets the focal side of the cropped background.

| View mode | Look | Shows | Uses |
|---|---|---|---|
| `moody_hero_8` | Homepage design. Tall photo (350px on mobile, 500px on desktop), extra-bold white headline pinned bottom-left | heading (h2), subheading, CTA, overlay, text color | **83**, the house standard |
| `moody_hero_7` | Homepage design. Tall photo, headline placed by Text Position | heading (h2), subheading, CTA (`ut-btn--hero`), overlay, text color, position | 25 |
| `moody_hero_1` | Bold heading and subheading on a burnt-orange panel beside the photo | heading, subheading, CTA | 15 |
| `moody_hero_6` | Tall photo, extra-bold headline | heading, subheading, overlay, text color | 6 |
| `moody_hero_6_short` | Same as 6, shorter (right-anchored) | as 6 | 2 |
| `default` | Large image only, with caption and credit underneath. No text on the image | caption, credit | 10 |
| `moody_hero_2` | Bold heading on a dark gradient across the base of the photo | heading, CTA. **Subheading hidden** | 4 |
| `moody_hero_3` | White bottom pane with heading, subheading and a burnt-orange CTA | heading, subheading, CTA | 2 |
| `moody_hero_4` | Centered image with a dark bottom pane holding heading, subheading and CTA | heading, subheading, CTA | 1 |
| `moody_hero_5` | *Legacy* half-and-half. Still used on 1 page but **no longer selectable** | — | 1 |

**Output:** the `.moody-hero` wrapper plus a style class (`moody-homepage-hero style-8`, `hero--photo-orange-insert`, `hero--photo-gradient`, `hero--photo-white-notch`, `extrabold-headline`, `moody-hero-short`). The photo is a CSS background, and its alt text is rendered as `span.sr-only`. Styles 7 and 8 render the heading as `<h2>`. **Styles 1–6 render it as a `<div>`**, so it isn't a real heading. Use those styles under a heading, or prefer 7/8.

**Choosing:**
- **Landing or top-level page:** style 8. Use 7 when you need the text somewhere other than bottom-left.
- **Program or minor page that needs the name and a one-line pitch:** style 1.
- **Photo story that needs credit or caption, with no text over the image:** default.
- **Busy photo:** add a charcoal overlay with white text (styles 6–8).
- **Keep heroes to one per page,** at the top. Use the Showcase for image rows further down.

## 4. Moody Flex Grid (`inline_block:moody_flex_grid`) · 52 placements

**Block-level inputs**
- **Headline:** renders as a `<div>`. Use the block's *Display title* if you need a real `<h2>`.
- **Items per row:** one to six.
- **Overlay Text:** puts the text over the image with a gradient. Works with the standard and rectangular displays.

**Per-item inputs** (add as many items as you need)
- **Image:** cropped 1:1, 500×500 ideal. Rectangular style uses 3:2.
- **Item Headline** (h3), with optional **Headline Color** (burnt orange, charcoal, white or black) and **headline alignment** (left, center or right).
- **Copy:** rich text.
- **URL:** links the headline and image.
- **Link Button Text:** shows a `ut-btn` when there's a URL, with button alignment.

| View mode | Look | Best for | Uses |
|---|---|---|---|
| `flex_grid_circular_style` | Round photos (250px max), centered name and short copy. The whole item is a link | **People**: leadership, staff, faculty spotlights | 24 |
| `default` (standard) | Square image, headline, copy | Coaches, projects, general galleries | 13 |
| `flex_grid_promo_style` | Image with an overlaid headline tile that links | Navigation to programs and sub-pages | 11 |
| `flex_grid_card_style` | Cards with image, headline, copy and a button (`person-card`) | Feature cards with a CTA | 3 |
| `flex_grid_rectangular_style` | 3:2 media cards, or text-only tiles if there's no image | Wider media, links to applications or resources | 1 |
| `flex_grid_flip_style` | Flip card that reveals a burnt-orange back with copy on hover | Teasers that reveal detail. New; **not used anywhere yet** | 0 |

**Common column counts:** 3 is used most (7 blocks), then 4 (6). On mobile, six columns collapse to three.

## 5. Moody Showcase (`inline_block:moody_showcase`) · 51 placements

**Per-row inputs** (add as many rows as you need)
- **Media:** an image or an external video. Image size is 900×970, or 1000×666 for the Marketing style.
- **Text:** Headline (h3) and Copy (rich text).
- **Call to action:** URL, link text and icon. Renders as `ut-btn--homepage`.
- **Effects:**
  - *Lock media while copy scrolls:* the media stays sticky.
  - *Make media fill the full area.*
  - *Use pinned image reveal effect:* images only.

| View mode | Look | Uses |
|---|---|---|
| `default_33_66_display` | Media 1/3, text 2/3 | 24 |
| `default` | Image + text side by side (50/50) | 20 |
| `moody_showcase_style_three` (Marketing) | Centered 400px image, large burnt-orange headline, 30–50px padding, alternating gray row backgrounds | 4 |
| `moody_showcase_style_two` | Media 2/3, text 1/3 (66-33) | 3 |

- **Use for:** alternating image + story rows, program highlights, "why Moody" marketing sequences, report or feature promos. Use Marketing style for 3 or more persuasive rows on a recruiting page. Use 33/66 when the copy is the point, and 66/33 when the image is.
- An empty Headline still outputs an empty `<h3>`, so always fill it in.
- Reference page: `/support/moody-showcase-examples`.

## 6. Utexas Promo Unit (`inline_block:utexas_promo_unit`) · 110 placements

**Inputs**
- **Promo Unit Headline:** the block heading, rendered as `<h2>`.
- **Items** (add as many as you need), each with:
  - **Image:** at least 1600px wide, with the ratio matching the view mode.
  - **Item Headline:** h3. It becomes a link when there's a URL.
  - **Copy:** rich text.
  - **URL and Link text:** an optional second link.

| View mode | Image | Uses |
|---|---|---|
| `default` | Landscape 220×140 (11:7) beside the text | 55 |
| `utexas_promo_unit_4` | Stacked Landscape 1.6:1, image above text | 35 |
| `utexas_promo_unit_2` | Portrait 150×188 (4:5) beside the text | 11 |
| `utexas_promo_unit_3` | Square 140×140 beside the text | 8 |
| `utexas_promo_unit_5` / `_6` | Stacked Portrait / Stacked Square. Available but **unused** | 0 |

- **Use for:**
  - Lists of resources or programs with a thumbnail and a short blurb.
  - Award winners and people with a bio line: portrait or square.
  - Link clusters: no image, links in the copy (e.g. `/human-resources`).
- Put stacked promo units in a 2–3 column section to make a card row.

## 7. Utexas Featured Highlight (`inline_block:utexas_featured_highlight`) · 42 placements

- **Inputs:**
  - **Media:** optional, at least 600px wide.
  - **Text:** Headline (h2, links to the CTA URL), Copy and an optional Date.
  - **Call to action:** URL, link text and icon. Renders as `ut-btn`.
- **View modes:**
  - `default` Limestone (light) `#d6d2c4`
  - `utexas_featured_highlight_2` "Bluebonnet" (medium) `#005f86`. Used 17 times, the most common.
  - `utexas_featured_highlight_3` Charcoal (dark) `#333f48`
- **Use for:** one spotlighted item, such as a resource, report, program or news item, as a full-width colored band with image, text and a single CTA. Prefer Limestone or Charcoal. Bluebonnet is outside the core Moody palette.

## 8. Moody Flex Color Blocks (`inline_block:moody_flex_color_blocks`) · 170 placements

- **Inputs:** 1 to 4 items, each with:
  - **Headline:** a textarea, rendered as `<h2>`.
  - **Subheadline:** optional.
  - **URL:** the whole tile becomes the link.
  - **Link icon**
  - **Color scheme:** Gray (charcoal `#333f48`) or Orange (`#bf5700`). Hover darkens the tile.
- **Output:** a centered, padded, solid-color tile linking out, `a.flex-color-blocks-wrapper.{gray|orange}`. Several items in one block sit side by side.
- **How it's used in practice:** usually **one item per block** (22 of 37 sampled), with several blocks placed across the columns of a 2–4 column section to make a row of big link tiles. Subheadlines are rare.
- **Use for:** prominent navigation tiles ("Speakers", "Location", "See all awards"), or a bold CTA band at the end of a page. Alternate gray and orange, or keep one color per row. Keep headlines to 2–6 words.

## 9. Moody Accordion (`inline_block:moody_accordion`) · 126 placements

- **Inputs:** panels (add as many as you need), each with a Panel title and Panel contents (rich text).
- **View modes:**
  - `default`: full-size panels. Used 110 times.
  - `moody_accordion_condensed`: smaller 1.25rem titles, tighter padding, burnt-orange collapsed state. Used 16 times.
- **Output:** Alpine.js (`x-data`, `x-show`). Each panel has a `button.accordion-btn` and an `.accordion-content`.
- **Use for:** FAQs, policies, requirements, course lists, and any long reference content that readers scan. Use condensed for dense lists, such as language requirements by region. Don't hide the main message of a page in an accordion. Give the block a *Display title* heading.

## 10. Moody Contact Info (`inline_block:moody_contact_info`) · 30 placements

- **Inputs:**
  - **Text:** Headline (h2), Subheadline (large, limestone colored) and Copy (rich text).
  - **Link:** URL, link text and icon.
- **Output:** `.moody-contact-block` / `.moody-contact-info-wrapper`, a styled contact panel.
- **Use for:** "Visit us" or "Contact us" panels with an address, hours, phone, email and an appointment link. Usually near the end of a page or in a sidebar column.

## 11. Moody Quotation (`inline_block:moody_quotation`) · 60 placements on 23 pages

**Inputs**
- **Text:** Quote, Author, and Attribution details (optional, shown after the author).
- **Image:** optional. Used by the Split style; at least 1200px wide.
- **Link:** optional URL, link text and icon.
- **Style:** pick one of the five styles below. The block has a single view mode (`full`), so the look is set by this field, not by a view mode.
- **Split quote appearance** (Split style only):
  - **Text and background color:** white on UT blue, white on burnt orange, white on charcoal, or charcoal on white.
  - **Text size:** small, medium or large.
  - **Text alignment:** left, center or right.
  - **Image position:** left or right.

| Style | Look | Live usage (sampled) |
|---|---|---|
| `orange` | White quote text on a burnt-orange panel, author in burnt orange below | **most common** (20 of 27) |
| `grey` | White text on a charcoal panel with a burnt-orange left border | 4 of 27 |
| `split` | Photo fills one half, quote and caption the other half (`figure` / `blockquote` / `figcaption`) | 3 of 27 (new, added Sept 2026) |
| `default` | Dark text, no background, indented | rare |
| `feature` | Large burnt-orange quote, centered, max width 74rem | rare |

**Output**
- Orange, grey, default and feature render `div.quotation-wrapper.{style}`, with the quote in `p.quote` and the author in `p.author > strong`.
- Split renders proper `<figure><blockquote>…</blockquote><figcaption>`.

**Use for**
- **Student, alumni or faculty voices** on program, center and news pages. A quote between copy sections breaks up long pages well.
- **Split** when you have a good portrait of the speaker.
- **Feature** for a single standout line, such as a mission statement or headline quote.
- Prefer the orange or charcoal palettes; UT blue is outside the core Moody palette.

**Writing tips:** keep quotes to 1–3 sentences, and put the person's role and class year in Attribution details.

## 12. Utexas Flex Content Area (`inline_block:utexas_flex_content_area`) · 43 placements on 25 pages

**Inputs** (add as many items as you need), each with:
- **Media:** an image, cropped 3:2 (1000×666 ideal), or an embedded video.
- **Headline:** h3. Links to the item's Call to Action URL.
- **Copy:** rich text.
- **List of links:** any number of extra links.
- **Call to Action:** URL, link text and icon.

**View modes:** `full` (30) and `default` (12) render identically. `utexas_flex_content_area_3` (1) is legacy. The add form has **no view-mode selector**, so new blocks use the default.

**Output:** `.ut-flex-content-area-wrapper` is a CSS grid. In a one-column, container-width section it lays items out **2 per row** on desktop and 1 per row on mobile. Each item has `.image-wrapper`, then `.content-wrapper` (`h3.ut-headline`, `.ut-copy`, links).

**Use for**
- Two-up (or more) feature items that each have an image or video, a heading, a paragraph and a few links. Examples: "Focus areas", program tracks, initiative summaries.
- Prefer Flex Grid **card** style when you want 3–4 per row or button CTAs. Use Flex Content Area when items need a **list of links** or an **embedded video**.

## 13. Utexas Promo List (`inline_block:utexas_promo_list`) · 29 placements on 23 pages

**Inputs**
- **List Headline:** renders as `h3.ut-headline--underline`, with a Bluebonnet-blue underline.
- **Items** (add as many as you need), each with:
  - **Image:** square 1:1, 170×170 ideal.
  - **Item Headline:** h3. Links when there's a URL.
  - **Copy:** rich text.
  - **URL:** links both the headline and the image.

| View mode | Layout | Uses |
|---|---|---|
| `default` | Single list, 1 item per row: small square image beside the text | 26 |
| `utexas_promo_list_2` | Single list, 2 items per row on wider screens | 3 |
| `utexas_promo_list_4` | Single list, stacked (image above text) | 0 |
| `utexas_promo_list_3` | Two lists side by side | 0 |

**Use for**
- Compact lists of people, partners, guests or resources, each with a small square thumbnail and a short blurb. Examples: center people pages, guest speakers, partner organizations.
- For headshot-led people grids, prefer Flex Grid circular. Promo List suits longer bios beside a small photo.
- The list headline and the item headlines are both `<h3>`. Turn on *Display title* to get a proper `<h2>` above them.

## 14. Utexas Image Link (`inline_block:utexas_image_link`) · 22 placements on 13 pages

**Inputs**
- **Image:** fills the width of its region.
- **Link:** URL, link text, new-window option and icon.

**Output:** `div.utexas-image-link > a > picture > img`. The **Link text is not rendered**, so the image's **alt text is the link's only accessible name**. Write the alt text to describe the destination, for example "Photo album: Tainted Blood screening panel", not just the image.

**Use for:** a clickable image such as a report cover, event poster, photo album, or partner logo linking out. It's usually placed in a narrow column next to text.

## 15. Moody Focus Areas (`inline_block:moody_focus_areas`) · 16 placements on 15 pages

**Inputs**
- **Focus Areas Items Title:** optional.
- **Items per row:** two, three or four.
- **Space between items** and **space between rows:** touching, small, medium or max.
- **Block call to action:** URL, link text and icon.
- **Items** (add as many as you need), each with:
  - **Image:** square 1:1, 280×280 ideal. It displays as a small (~100px) centered icon-style image.
  - **Item Headline:** h3.
  - **Copy**
  - **URL**

**Output:** `.focus-areas-wrapper .focus-areas-items.{n}-per-row.gap-{size}.gap-row-{size}`. Each item is centered, with the small image above a centered headline and copy (220px wide at most).

**Use for**
- At-a-glance program facts or pillars with icons or small images. Examples: "Two Year Program · Online · Cohort-based", writing-center services, certificate highlights.
- **3 per row** with medium spacing is the most common setup.
- Best with short headlines (1–4 words) and an optional one-line copy. For bigger photos, use Flex Grid.

## 16. Call to Action (`inline_block:call_to_action`) · 14 placements · legacy

**Inputs:** one or more links (URL, link text, icon), rendered as `a.button.ut-btn`.

**Status:** it's **no longer offered** in the Add block list. Existing placements still render. To add a button now, use a Basic block with `<a class="ut-btn" href="…">`, or a CTA field on a structured block.

## 17. Page-template field blocks

Moody Feature Page (news) templates place node fields as blocks: Subtitle, Body, Author, Created date and Links. Standard pages place Metatags and Links, and Subsite pages place Metatags. These come from the content type's template. Edit their content on the node **Edit** tab, not in Layout, and leave them in place.

## 18. Shared link options

Every block with a link (Hero, Flex Grid, Showcase, Promo Unit, Promo List, Featured Highlight, Flex Color Blocks, Flex Content Area, Focus Areas, Quotation, Image Link, Contact Info) shares the same link fields:
- **URL:** autocomplete for internal content, or a path or external URL.
- **Link text**
- **Open in new window/tab:** use sparingly.
- **Link appearance:** no icon, `ut-cta-link--lock` (sign-in required), `ut-cta-link--external` (off-site) or `ut-cta-link--angle-right` (caret).
