# Training-style Morph PPT with Images

Use this pattern by default when the user gives a topic without a stricter visual requirement.

## Default output

Create a training-style deck with:
- 4–6 slides
- Morph transition on every slide after the first
- Stable information hierarchy
- Mixed layouts chosen by content
- One generated illustration per slide
- Chinese copy unless the user asks otherwise

## Planning requirement

Before generating any slide or image, create `brief.md` first.

`brief.md` must define:
- audience
- scenario
- purpose
- slide count
- style direction
- narrative
- per-slide key message
- per-slide layout
- per-slide image topic
- per-slide image prompt

Do not generate images before the per-slide image plan is written down.

## Recommended layout mix

Avoid using the same layout on every slide.
A good default training deck often mixes:
1. `hero-cover`
2. `left-text-right-image`
3. `process-flow` or `three-cards`
4. `top-text-bottom-image` or `faq-troubleshooting`
5. `summary-takeaway`

## Image prompt pattern

For each slide, generate one illustration with a consistent style:
- modern technology training illustration
- clean, not flashy
- unified color system across slides
- suitable for internal training or explainers
- aspect ratio 16:9

Prompt template:

`现代科技培训风插图，主题是 <slide topic>，统一蓝青色系，信息清晰，简洁专业，适合培训课件，16:9`

Adjust wording for non-tech topics, but keep the same constraints: clean, explainable, consistent.

## Morph guidance

Use repeated names for these persistent elements across slides:
- title
- subtitle
- body
- hero-image

You do not need flashy motion. Prefer readable continuity:
- title moves slightly
- body block grows or shifts
- image changes position or scale slightly

## Fallback

If image generation fails:
- still finish the PPT
- leave the layout image-ready
- tell the user image generation failed and the deck is text-first for now
