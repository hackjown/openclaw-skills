---
name: morph-ppt
description: Generate Morph-animated PPTs with officecli, including training-style, business-style, or dark-style decks with per-slide generated images. Use when the user asks to make a PPT, presentation, slides, training deck, courseware, business deck, or a topic-based deck that should include Morph transitions, structured slide layouts, selectable visual styles, or auto-generated illustrations.
---

# Morph PPT

Generate topic-based PPTs with `officecli`.

Default workflow: build a structured Morph deck with **selectable style + per-slide generated illustrations + per-slide layout planning**.

## Workflow

### 1. Analyze the topic first

Do not jump straight into slide generation.

Before building anything, read these references:
- `reference/decision-rules.md`
- `reference/brief-template.md`
- `reference/layout-patterns.md`
- `reference/style-training.md`
- `reference/style-business.md`
- `reference/style-dark.md`
- `reference/training-with-images.md`
- `reference/officecli-pptx-min.md`

Create `brief.md` first. It must include:
- topic
- audience
- scenario
- purpose
- language
- target slide count
- style direction
- visual tone
- narrative structure
- one-sentence deck conclusion
- slide-by-slide outline
- layout for each slide
- image topic and image prompt for each slide

If the user only gives a topic, infer the missing fields conservatively.

Default assumptions:
- audience: general business / training audience
- scenario: training or internal explanation
- purpose: explain clearly, not persuade aggressively
- language: match user language
- slide count: 4–6
- style: training if unspecified

### 2. Choose style and layouts deliberately

Do not use one fixed template for every deck.

Supported default style directions:
- `training`
- `business`
- `dark`
- `minimal`

Pick style based on the request:
- training / onboarding / explainers -> `training`
- formal reporting / customer / executive topics -> `business`
- AI / tech / platform / product launch feeling -> `dark`
- if user explicitly wants fewer elements -> `minimal`

Then choose layouts per slide using `reference/layout-patterns.md`.

Rule:
- every slide in `brief.md` must specify a layout
- avoid repeating the same layout on every slide unless requested

### 3. Prepare images

Generate one image per slide based on the `Image prompt` fields in `brief.md`.

Use the local image workflow:

```bash
python3 skills/morph-ppt/scripts/grok-imagine-download.py "图片提示词" output/topic-images/slide1.jpg
```

Guidelines:
- keep style consistent across slides
- align the image style with the chosen `style direction`
- save into `output/<topic>-images/`
- if generation fails, continue building the deck without images

### 4. Build the PPT

Use `officecli` to create the `.pptx`.

Rules:
- use the layout plan from `brief.md`, not one static layout
- use Morph on every slide after the first; using Morph on slide 1 is acceptable if the CLI supports it consistently
- reuse these shape names across slides when possible:
  - `title`
  - `subtitle`
  - `body`
  - `hero-image`
- prefer readable continuity over flashy motion

Examples of layout usage:
- cover -> `hero-cover`
- explanation -> `left-text-right-image`
- workflow -> `process-flow`
- pillars -> `three-cards`
- comparison -> `comparison`
- closing -> `summary-takeaway`

### 5. Validate

Always run:

```bash
officecli validate <file>.pptx
officecli view <file>.pptx outline
```

If images were added, make sure the file still validates.

### 6. Deliver

Return:
- the `.pptx` file
- the image folder if useful
- `brief.md`
- a brief note on whether images were included successfully

## Notes

- Prefer Chinese output for this workspace unless the user asks for another language.
- Prefer practical, reusable slides over marketing copy.
- If the user asks for a stronger training style, increase clarity and explainability first.
- If the user asks for a stronger business style, increase discipline and hierarchy first.
- If the user asks for a stronger dark style, increase contrast and tech feeling without hurting readability.
- Reuse this workflow directly for future topic-based decks.
