# Layout Recipes

Starting points built only from catalog classes. The first four come straight from the style guide; the rest combine the same classes. Adapt them freely.

## Responsive card grid (style guide)
```html
<div class="ut-display-grid ut-cols-1 md:ut-cols-2 lg:ut-cols-3 ut-gap-6">
  <article class="ut-surface-paper ut-p-6"><h3>First card</h3><p>Card copy.</p></article>
  <article class="ut-surface-paper ut-p-6"><h3>Second card</h3><p>Card copy.</p></article>
  <article class="ut-surface-paper ut-p-6"><h3>Third card</h3><p>Card copy.</p></article>
</div>
```

## Stack on mobile, split on desktop (style guide)
```html
<div class="ut-display-grid ut-cols-1 lg:ut-split-halves ut-gap-6 ut-items-center">
  <div><h3>Heading</h3><p>Introductory copy.</p></div>
  <div class="ut-text-start lg:ut-text-end"><a class="ut-cta-link" href="/">Explore our site</a></div>
</div>
```

## Reading width and responsive spacing (style guide)
```html
<div class="ut-measure-standard ut-mx-auto ut-p-4 md:ut-p-8">
  <h3>Readable text</h3>
  <p>A centered, bounded reading width with comfortable padding.</p>
</div>
```

## Hero-like content panel (style guide)
For real heroes with media, overlays and managed buttons, use the Moody Hero block instead (see `blocks.md`).
```html
<section class="ut-surface-charcoal ut-p-6 lg:ut-p-12">
  <div class="ut-measure-standard ut-ml-auto">
    <h2 class="ut-text-2xl lg:ut-text-4xl">A clear introduction</h2>
    <p>Supporting copy.</p>
  </div>
</section>
```

## Callout / announcement
```html
<aside class="ut-surface-orange ut-p-6 md:ut-p-8 ut-my-8">
  <h2 class="ut-text-2xl ut-mt-0">Applications open Sept. 1</h2>
  <p>Short supporting sentence.</p>
  <a class="ut-btn ut-btn--secondary" href="/apply">Start your application</a>
</aside>
```

## Image + text media object
```html
<div class="ut-display-grid ut-cols-1 md:ut-split-one-two ut-gap-6 ut-items-center">
  <img class="ut-w-full ut-aspect-landscape ut-object-cover" src="/sites/default/files/example.jpg" alt="Describe the image">
  <div>
    <h3>Title</h3>
    <p>Body copy.</p>
    <a class="ut-cta-link ut-cta-link--angle-right" href="/link">Read more about the topic</a>
  </div>
</div>
```

## Stats row
```html
<ul class="ut-list-unstyled ut-display-grid ut-cols-1 sm:ut-cols-2 lg:ut-cols-4 ut-gap-6 ut-text-center">
  <li class="ut-surface-paper ut-p-6"><span class="ut-display-block ut-text-5xl ut-font-weight-black text-ut-burntorange">7</span>departments</li>
  <li class="ut-surface-paper ut-p-6"><span class="ut-display-block ut-text-5xl ut-font-weight-black text-ut-burntorange">5,000+</span>students</li>
</ul>
```
(Burnt orange on paper is fine here only because the number is 48px black weight. Keep small text charcoal.)

## People / faculty list
```html
<ul class="ut-list-unstyled ut-display-grid ut-cols-1 md:ut-cols-2 lg:ut-cols-3 ut-gap-8">
  <li>
    <img class="ut-w-full ut-aspect-square ut-object-cover ut-object-center-top" src="/sites/default/files/person.jpg" alt="Portrait of Jane Doe">
    <h3 class="ut-text-xl ut-mt-4 ut-mb-1">Jane Doe</h3>
    <p class="ut-text-sm ut-mt-0">Associate Professor, School of Journalism and Media</p>
  </li>
</ul>
```

## Button group
```html
<div class="ut-display-flex ut-flex-wrap ut-gap-4">
  <a class="ut-btn" href="/apply">Apply now</a>
  <a class="ut-btn ut-btn--secondary" href="/visit">Schedule a visit</a>
</div>
```

## Link list / resources
```html
<h2>Student resources</h2>
<ul>
  <li><a href="/advising">Academic advising</a></li>
  <li><a class="ut-cta-link ut-cta-link--external" href="https://utdirect.utexas.edu">UT Direct (opens external site)</a></li>
</ul>
```
