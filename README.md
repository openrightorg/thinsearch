# Thin Search

Thin Search is a **single‑file, server‑less search UI** that lives in a single HTML file.  It works entirely in the browser — no backend, no build step, no hosting required.  Drop the file on a local drive or host it on any static‑file server and you have a fast, privacy‑friendly search bar.

## Core Features

- **Bang‑style searches** — type `!g cats` or `google cats` to instantly redirect to a search on the target site.
- **Built‑in bangs** — the bundled JSON contains dozens of common sites (Amazon, DuckDuckGo, YouTube, etc.) with aliases for quick access.
- **Category‑aware suggestions** — when you start typing a query, the UI looks for a matching category (e.g. *calculate* ➜ AI or *recipe* ➜ food) and shows only bangs that belong to that category.
- **Custom bangs** — users can edit, add, or delete bangs via the Settings page.  Bangs are stored in `localStorage`, so they persist across reloads and are private to each browser.
- **Keyboard navigation** — use the arrow keys to cycle through suggestions, press `Enter` to apply the highlighted bang, or `Escape` to dismiss the popup.
- **Offline‑ready** — all assets are embedded; no external requests are needed to run the page.
- **Safe expression evaluation** - can locally evaluate math expressions and unit conversions.

## Usage

1. **Open `index.html`** in any modern browser.
2. In the search box, type a query or a bang. Examples:
   - `!a headphones` ➜ Amazon search for headphones
   - `google cats` ➜ Google search for cats
   - `recipe lasagna` ➜ Shows food‑related bangs (AllRecipes, Epicurious, etc.)
3. Hit **Enter** to perform the search.
4. Click **⚙️ Settings** to edit your list of bangs.

## Extending

The bangs JSON is embedded in `index.html` under the `<script id="data-json" type="application/json">`.  To add new bangs, modify that block or add them via the Settings UI.  Each bang must include:

```json
{
  "keyword": "<site keyword>",
  "alias": "<short alias> (optional)",
  "name": "<display name>",
  "url": "<search URL with %s placeholder>",
  "category": "<category> (optional)"
}
```

The `%s` placeholder is replaced with the URL‑encoded query.

## License

This project is released under the MIT License.

