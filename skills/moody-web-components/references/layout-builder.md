# Moody Layout Builder: LLM authoring context

Implementation reference captured October 7, 2026. This is a supported-component reference, not a guarantee that every block is enabled on every site or available to every editor.

## What is authoritative

Use the target site's enabled Layout Builder Browser entries and access-filtered available blocks first, then its current block forms, field schemas and templates. This reference is a fallback. Installed modules, install-time YAML and the historical 26-component guide do not prove current availability. The browser also discovers enabled Views displays and accessible reusable blocks; their lists vary by site and permissions.

Distinguish these kinds of blocks:

- **Inline content blocks** (`inline_block:...`): structured Drupal content fields, authored for a page placement.
- **Configurable plugin blocks**: native block settings such as selected stories, columns, filters, images or slides.
- **Views blocks** (`views_block:...`): dynamic listings driven by existing Drupal content and View configuration.
- **Reusable blocks** (`block_content:...`): shared content; editing it affects every placement. Moving or configuring one placement is a separate action.

Prefer an available purpose-built component over recreating it in Basic block HTML. Preserve the user's explicitly selected component. Resolve actual Media, nodes, taxonomy terms, destinations and anchor targets; never invent IDs, testimonials, dates, statistics or people. If current availability cannot be checked, make recommendations conditional and identify the missing information.

## Section width: edges, margins and reading measure

Width and column count are separate section settings. A one-column section can be narrow, contained or full width. A four-column section can also use any offered width.

| UI choice | Stored setting | Effect | Best fit |
| --- | --- | --- | --- |
| Full width of page | `section_width: container-fluid` | Allows the section content to use the viewport width rather than the centered page container. | Edge-to-edge hero/media, immersive stories and large visual bands. |
| Container width | `section_width: container` | Uses the theme's centered responsive container (`container-xl` in the inspected UTDK implementation), retaining side margins at wider sizes. | Most card collections, listings and general landing-page content. |
| Readable width | `section_width: readable` | Constrains the reading measure; inspected UTDK CSS limits it to 830px. Theme overrides can differ. | Long prose, FAQs, instructions and editorial introductions. |

**“Full width of page” means full width, not the contained page width.** In casual requests, “page width” may mean the normal centered content area; translate that to Container width only when that is the intended result. Use the target site's actual UI labels rather than inventing another Page width setting.

Full width removes the outer container constraint; it does not automatically remove block padding, column gutters, text measure or a component's own maximum width. For true edge-to-edge imagery, inspect section spacing and the component's width controls as well. Remove padding only when the design needs it; keep text away from viewport edges.

Background width and content width may differ. Where the target site offers a constrain-content style, a full-width background can retain contained text. Existing documentation describes this combination for one-column layouts; do not promise the same effect for multiple columns without checking the current styles and rendered output. A block-level readable-width style is also distinct from the section width.

The inspected UTDK defaults are Readable width for new one-column sections and Container width for two-, three- and four-column sections. Existing saved sections keep their settings; do not claim a default change rewrites them.

## Section columns: one through four

| Section layout | Appropriate content | Available proportions in inspected UTDK |
| --- | --- | --- |
| One column | A hero, article body, substantial component or a block that already manages its own collection. | One region. |
| Two columns | Two parallel topics, media beside copy, or a main area plus sidebar. | 50/50, 33/67, 67/33, 25/75, 75/25. |
| Three columns | Three compact, parallel choices; a primary region with two supporting areas. | 33/34/33, 25/50/25, 25/25/50, 50/25/25. |
| Four columns | Short links, compact facts or small parallel panels. Avoid long prose in each region. | Four equal regions. |

Use the responsive behavior supplied by the selected layout. Check mobile stacking and reading order rather than forcing four desktop columns onto a phone.

**Section columns are not block columns.** A two-column Editors Picks grid placed in one half of a two-column section produces two cards within that half; it does not make two page-wide columns. Usually place a collection block in a one-column Container width section and configure its own grid. Do not impose a universal 1–4 limit on all components: Flex Grid supports up to six; Gallery has its own pattern; some Views determine their own grid.

### Editors Picks column contract

Feature Pages – Editors Picks (`moody_feature_page_feature_pages_editors_picks`) supports an ordered mixture of existing Feature Pages and custom cards, an image-style override, and a **Columns** selector from 1 to 4. Recent published-story choices and autocomplete help resolve existing stories; custom cards supply their own media, subheads, title, summary and destination.

Default and missing/invalid column settings use **2**, rendering `col-12 col-sm-6`. The same selection applies to legacy selected-node rendering and the ordered/custom-item renderer.

| Selection | Responsive row classes |
| --- | --- |
| 1 | `col-12` |
| 2 (default) | `col-12 col-sm-6` |
| 3 | `col-12 col-sm-6 col-md-4` |
| 4 | `col-12 col-sm-6 col-md-4 col-lg-3` |

Use the native Columns control. Changing the underlying View alone does not override the ordered/custom block's chosen columns. A block setting changes presentation, not the page's section layout or story-selection semantics.

## Structured content blocks

The table gives the implementation ID, useful features, and editorial fit. Labels can vary. Offer only entries available on the target site.

| Component / plugin ID | Features | Ideal use and placement recommendation |
| --- | --- | --- |
| Basic block / `inline_block:basic` | Formatted body, semantic headings, links and lists. | Ordinary prose; Readable width for lengthy text. |
| Featured Highlight / `inline_block:utexas_featured_highlight` | One media item, headline, copy, date and destination/CTA. | A timely highlight or featured opportunity; Container width or a broad visual band. |
| Flex Content Area / `inline_block:utexas_flex_content_area` | Repeatable media-and-copy rows with headings, related links and CTAs. | Structured explanatory content; Container width, with each row focused on one topic. |
| Image Link / `inline_block:utexas_image_link` | Image linked to a destination, with accessible link text. | One visual navigation tile; choose the region width and crop intentionally. |
| Promo List / `inline_block:utexas_promo_list` | Compact repeatable image, headline, copy and link units. | Several related promotions or resources; contained content or supporting region. |
| Promo Unit / `inline_block:utexas_promo_unit` | Larger repeatable promotional items with group heading, media, copy and links. | Prominent related destinations; broad contained region. |
| Moody Accordion / `inline_block:moody_accordion` | Repeatable titled panels with formatted content. | FAQs and predictable grouped details; keep essential introductory information visible. |
| Moody Ambient Video / `inline_block:ambient_video` | External video, poster/fallback imagery, headline, CTA and presentation controls. | An intentional video-led introduction; broad/full-width section with usable static fallback. |
| Moody Contact Info / `inline_block:moody_contact_info` | Headline, subheadline, copy and contact/CTA link. | Office contact details and next steps; supporting region or closing contact band. |
| Moody Flex Color Blocks / `inline_block:moody_flex_color_blocks` | Up to four short linked panels with headline, subheadline and provided color choices. | Parallel navigation choices; a wide region. Labels must carry meaning independently of color. |
| Moody Flex Grid / `inline_block:moody_flex_grid` | Repeatable cards with media, headline, body, links/buttons and display options; 1–6 items per row. | Programs, topics and resource collections; normally a one-column Container width section. |
| Moody Focus Areas / `inline_block:moody_focus_areas` | Overall title/CTA, repeatable image, heading, copy and link items; 2–4 per row. | A small parallel set of disciplines or mission areas; broad region. |
| Moody Hero / `inline_block:moody_hero` | Image, heading, subheading, caption/credit, CTA and site-provided view modes. | Primary page introduction; full width for edge-to-edge imagery or contained for a restrained introduction. |
| Moody Impact Facts / `inline_block:moody_impact_facts` | Prominent fact and supporting text units; 2–4 per row and provided styles. | Verified outcomes and statistics, with units, timeframe and source context. |
| Moody Promotion / `inline_block:moody_promotion` | Media, headline, date, copy and CTA. | One image-led campaign, announcement or opportunity; broad region. |
| Moody Showcase / `inline_block:moody_showcase` | Repeated image/video and substantial copy/CTA; optional sticky or pinned-reveal presentation. | Editorial storytelling; wide section. Use motion only when it adds meaning. |
| Moody Quotation / `inline_block:moody_quotation` | Quote, author, attribution, style, optional media and link. | A verified testimonial or pull quote; preserve exact quotation and clear attribution. |
| Moody Newsletter / `inline_block:moody_newsletter` | Heading, subscription/destination link and provided style. | A concise newsletter CTA, often in a supporting region. |
| Photo Content Area / `inline_block:utexas_photo_content_area` | Photo-led content component, where offered. | Image-led material; inspect current fields and view mode. Some historical catalogs exclude it. |

## Configurable plugins and dynamic listings

| Component / plugin ID | Features | Ideal use and placement recommendation |
| --- | --- | --- |
| Moody Hero Builder / `moody_hero_builder` | Structured visual composition, heading/text/buttons, managed images and device-specific layout; optional supported Vimeo/YouTube decorative background video with poster. | A highly controlled page introduction. Use native responsive previews; keep essential content in text. Full width when edge-to-edge is intended. |
| Moody Card Builder / `moody_card_builder` | Up to 12 cards, up to 8 structured rows per card, 1–3 cells per row; responsive collection layouts, managed media, image share/placement, links and buttons. | Rich manually curated collections. Usually one broad section; configure the collection internally instead of nesting another multi-column section. |
| Editors Picks / `moody_feature_page_feature_pages_editors_picks` | Ordered existing stories/custom cards, recent choices, autocomplete, image-style override, 1–4 columns; default 2. | Curated news or feature-story selections; Container width and one section region. |
| News and Announcements / `moody_feature_page_news_and_announcements` | Repeatable category, optional date/date format, formatted body, URL and link text. | Short editorial updates with direct destinations; contained region. |
| Moody Media Mentions / `moody_feature_page_media_mentions` | Repeatable media source, headline, external destination and date. | Verified external coverage; use descriptive destination context. |
| Moody Events V2 / `moody_events_moody_events_v2` | Upcoming events; 1–20 results, excluded IDs, host filtering and image display. | A live events listing. Prefer over the legacy slider when both fit and are offered. |
| Events Slider – Filterable / `moody_events_moody_events_slider_filterable` | Legacy event slider with included-host and excluded-event filters. | Existing pages that specifically need the legacy presentation; verify controls and static access. |
| Subsite Blog Grid / `moody_subsite_subsite_blog_grid` | Dynamic posts selected by an existing subsite Directory Structure term. | A subsite's live blog listing; resolve the term rather than copying posts manually. |
| Faculty Bio / `views_block:faculty_bio_view-block_1` | Published faculty listing with the site's exposed filters, ordering and pager settings. | A live directory; edit content/the View instead of duplicating people in manual cards. |
| Faculty Emeritus / `views_block:faculty_bio_view-block_4` | Faculty View display with its configured emeritus/title filters. | A dynamic emeritus directory; confirm the display's current filters. |
| Moody Chart / `moody_charts_block` | Bar, line, pie, doughnut, radar or polar-area chart; CSV/XLSX data, title, provided palette, legend/grid toggles and aspect ratio. | A verified comparative dataset; provide adjacent summary or accessible data. Uploaded data takes precedence over pasted CSV. |
| Moody Focal Point / `moody_focal_point_block` | One image and up to 10 focal points with captions, positions, emphasis and border/arrow controls. | Guided inspection of one meaningful image; also explain each detail in text. |
| Moody Image Gallery / `moody_image_gallery_block` | Up to 12 images with crop focus/captions and gutter controls; its own image layout pattern. | A curated image collection, often wide/full width. Caption and Media alt text serve different purposes. |
| Moody Scroll Reveal Media / `moody_scroll_reveal_media_block` | Up to 6 ordered media/text slides, fade/slide motion, inline/overlay text and supported video; optional independent responsive title/body placement. | A sequential visual story. Broad section; content must remain understandable without motion. |
| Moody Mini Nav / `moody_mini_nav` | Up to 8 links or page-block anchors, mobile toggle label and provided typography/colors. | In-page or subsection navigation; verify every anchor and order links with the page. |
| Moody Dynamic Flip Grid / `moody_flip_things_dynamic_flip_grid` | Repeatable front/back media, headings, copy, CTAs and provided presentation choices; 1–4 items per row. | Deliberate paired front/back content. Prefer ordinary cards when flipping adds no meaning. |
| Flip Image Grid / `moody_flip_things_flip_image_grid` | Exactly three image-backed items with heading, body and URL. | Three parallel items when the offered flip interaction serves the content. |
| Moody Image Grid / `moody_image_grid_image_grid` | Three image/headline/link items, overall heading and image-style choice. | Three simple visual destinations, only where this plugin is offered. |
| Shorthand Story / `moody_shorthand_zip_shorthand_zip_story` | Reviewed Shorthand ZIP export or an existing managed story location. | A complete imported story; usually one Full width of page section. Do not fabricate package paths. |
| Flipbook / `moody_flipbook_example` | Historical catalog describes an automatic feature-page collection; implementation is site-specific and absent from the shared mirror. | Inspect the target site implementation first; use Editors Picks for manually chosen stories. |
| Moody Interactive Featurette / `moody_interactive_featurette_moody_interactive_featurette` | Three image/color visual slots with headings, copy and links. | A deliberately layered presentation, only where offered; preserve nonvisual reading order. |
| Moody Special Quote / `moody_special_quote_special_quote` | Heading, two quote fields and an image. | A verified quote-led feature, where offered. Distinct from Moody Quotation. |
| Learn Through Experience / `learn_through_experience_block` | Fixed site-specific experience presentation without author content settings. | Only when that built-in site behavior matches the brief. |

Moody AI Assistant (`moody_ai_assistant_block`) is application UI, not a page-content component to recommend.

## Authoring decisions and output

Use the native editor's offered palettes, fonts, spacing and presentation choices. Do not revive retired palette choices from older documentation, or promise rounded corners where current components render square. Hero/Card Builder responsive layouts use their own container dimensions; do not substitute the theme's viewport breakpoints.

Keep meaningful images described, links descriptive, headings logical, charts understandable in text, and videos captioned when they carry information. Essential information and controls must remain available with keyboard, touch and reduced motion. Never claim accessibility verification based only on a component's existence.

For a requested page plan, identify visitor goal and give each section's width, region count/proportions, component name and implementation ID, block-level collection settings, approved content and unresolved references. Explain why the component fits. Recommend mobile behavior and list checks that actually remain; do not silently create or publish content from planning instructions.

Example plan (planning notation, **not** importable Drupal YAML):

```yaml
page_goal: Help visitors discover current stories and the department's strengths.
sections:
  - width: Full width of page
    section_columns: 1
    block: Moody Hero Builder
    plugin_id: moody_hero_builder
    purpose: Introduce the department with one approved image and message.
    unresolved: [Select accessible Media and confirm the CTA destination.]
  - width: Readable width
    section_columns: 1
    block: Basic block
    plugin_id: 'inline_block:basic'
    purpose: Provide a short orientation and key next steps.
  - width: Container width
    section_columns: 1
    block: Feature Pages - Editors Picks
    plugin_id: moody_feature_page_feature_pages_editors_picks
    block_columns: 2
    purpose: Display editor-selected stories using the native collection.
    unresolved: [Resolve the actual Feature Page nodes and their order.]
```

## Maintenance sources

- [UTDK section-width implementation](https://github.com/utdk/utdk_profile/blob/e01b6cd81a487ed639d665467e07af4baae406bd/modules/custom/utexas_layouts/src/Traits/SectionWidthTrait.php): exact three width choices. Neighboring layout plugins define proportions; the installed profile version is recorded in each site's Composer lock.
- [Moody Style Guide](https://moody.utexas.edu/style-guide): current theme utilities; check the live guide for exact classes.

Refresh from the target site's filtered catalog and current implementations when behavior differs. Keep implementation settings separate from editorial placement recommendations; do not describe the historical catalog as a freshly audited fleet inventory.


