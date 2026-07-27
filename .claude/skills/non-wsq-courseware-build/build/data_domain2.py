"""
Domain 2 — Creating Written and Visual Content with AI. Labs 5-8.

The connected Island Botanica campaign continues. Lab 5 drafts the brand story
and marketing copy on the locked voice; Lab 6 rewrites, polishes and adapts that
copy for different audiences and channels; Lab 7 generates the visual concepts
and on-brand images; Lab 8 turns copy and images into a social and launch
content kit. Each builds directly on the last, so the campaign gains its words
and its visuals here.
"""

PROJECT_NOTE = (
 "BUILDING BLOCK — what you create in this lab becomes part of your Island Botanica campaign pack, "
 "the connected campaign you assemble across all 11 labs."
)

DOMAIN2 = [
 dict(
 num=5, topic=2,
 title="Draft Your Brand Story and Marketing Copy",
 objective="Use AI, on the locked brand voice, to draft the Island Botanica brand story, hero taglines and product copy for the four scents — the written heart of the campaign.",
 desc="Now the campaign gets its words. In this lab you feed the AI the brand voice guide from Lab 3 and the "
 "brief, and draft the core written content: a short brand story for the Island Botanica collection, a set of "
 "hero tagline options, and a product description for each of the four scents (Frangipani Dawn, Pandan & "
 "Vetiver, Kaffir Lime Grove and Ylang Midnight). You generate several options for each, then curate and "
 "sharpen — cutting clichés, adding specific sensory detail, and holding every line to the voice guide. You "
 "keep the AI honest: no invented awards, ingredients or claims that are not in the brief. By the end you have "
 "the written spine of the campaign, on voice and ready to adapt, illustrate and pitch. " + PROJECT_NOTE,
 build="A short Island Botanica brand story, a shortlist of hero taglines, and a product description for each of the four scents — all on the Lumina Botanicals voice, curated from AI options and free of invented claims, saved in your project folder.",
 services="ChatGPT / Claude / Gemini / Copilot, brand storytelling, tagline generation, product copywriting, curating and sharpening AI drafts",
 steps=[
 ("Gather your inputs: the brand voice guide from Lab 3 and the Lumina Botanicals brief (collection story and the four scents). Paste the voice guide into your assistant so every draft is on voice.", ""),
 ("Draft the brand story for the collection. Paste the prompt below, then pick and refine the strongest version.",
  "Using the Lumina Botanicals voice guide above and this brief — Island Botanica is a limited-edition collection of four candle scents inspired by Southeast Asian flora, for the year-end gifting and Lunar New Year season — write two options for a 90-word brand story for the collection. Warm, sensory and quietly premium; on voice; no invented awards or claims."),
 ("Generate hero taglines. Paste the prompt below.",
  "Write ten short tagline options (six words or fewer) for the Island Botanica collection, on the Lumina Botanicals voice. Range from evocative and poetic to clear and benefit-led, so I can choose. Avoid clichés like 'light up your world'."),
 ("Write product copy for each scent. Paste the prompt below, filling in the scent as you go.",
  "For the scent '[SCENT NAME]' (one of the four Island Botanica scents), write a 35-word product description on the Lumina Botanicals voice: evoke the scent and mood, name the key botanical, and end with a subtle reason to gift or keep it. No invented ingredients or claims. Give me two options."),
 ("Curate and sharpen: choose one tagline and one description per scent, then cut every cliché, add one specific sensory detail to each, and read them aloud to check they sound like one brand.", ""),
 ("Fact-check the copy against the brief: remove anything the AI invented (awards, ingredients, origin claims) that is not in the Lumina Botanicals brief, and keep only what is true to the fictional brand.", ""),
 ("Save the brand story, chosen taglines and the four product descriptions in your project folder. This is the written spine you adapt in Lab 6, illustrate in Lab 7 and turn into social content in Lab 8.", ""),
 ],
 test="You have a curated Island Botanica brand story, a chosen hero tagline (from ten options), and a sharpened product description for each of the four scents — all on the Lumina Botanicals voice, with clichés cut, one sensory detail added to each, and every invented claim removed — saved in your project folder.",
 ),
 dict(
 num=6, topic=2,
 title="Rewrite, Polish and Adapt for Different Audiences",
 objective="Rewrite, polish and adapt the hero copy for different audiences and channels — iterating with follow-up prompts — so one core message reaches gift-shoppers and wellness-seekers across website, email, social and a short script.",
 desc="One message, many pieces. In this lab you take the copy from Lab 5 and use AI to adapt it — not rewrite "
 "it from scratch — for different audiences and channels while keeping the message and voice consistent. You "
 "generate a gift-shopper version and a wellness-seeker version of the hero copy, then adapt the collection "
 "line into a website intro, a launch email subject and opening, an Instagram caption, and a 15-second video "
 "or radio script. The core skill here is iterating with follow-up prompts: you steer each draft with short "
 "instructions ('warmer', 'half the length', 'more sensory', 'three bolder options') rather than starting "
 "over, and you polish the winners. By the end the campaign speaks to each audience in the right format "
 "without losing itself. " + PROJECT_NOTE,
 build="The Island Botanica hero message adapted into audience versions (gift-shopper and wellness-seeker) and channel versions (website intro, email subject + opening, Instagram caption, 15-second script) — refined through follow-up prompts and polished, all on one voice, saved in your project folder.",
 services="ChatGPT / Claude / Gemini / Copilot, rewriting and polishing, audience and channel adaptation, iterating with follow-up prompts, tone and length control",
 steps=[
 ("Bring your chosen hero copy and voice guide from Labs 3 and 5 into the assistant. Adaptation should keep that message and voice, only changing framing, tone and length.", ""),
 ("Adapt for two audiences. Paste the prompt below.",
  "Here is my hero copy for Island Botanica: '[PASTE HERO COPY]'. Rewrite it two ways on the same voice: (1) for a premium gift-shopper who wants a thoughtful present, and (2) for a wellness-seeker buying for their own calm and self-care. Keep each under 50 words and keep the core message the same."),
 ("Adapt for channels. Paste the prompt below.",
  "From that same message, give me: a 30-word website intro; a launch email subject line plus a 40-word opening; a 25-word Instagram caption with three tasteful hashtags; and a 15-second video/radio script. Keep everything on the Lumina Botanicals voice and consistent with each other."),
 ("Now iterate with follow-up prompts — this is the key skill. Do not re-write the prompt; steer with short instructions. Try the follow-ups below one at a time on a draft you want to improve.",
  "Make the Instagram caption warmer and more sensory. Now half its length. Now give me three bolder alternatives. Keep the best one."),
 ("Polish the winners: pick the strongest version of each piece, fix any repeated phrasing across them, and check every piece still carries the one core message and sounds like the same brand.", ""),
 ("Quick consistency pass. Paste the prompt below.",
  "Here are my final pieces for Island Botanica: [PASTE ALL PIECES]. Check they are consistent in voice, message and key wording, and flag anything that sounds off-brand or contradicts another piece. List only what to change."),
 ("Save all adapted and polished pieces, grouped by audience and channel, in your project folder — ready to pair with visuals in Labs 7 and 8.", ""),
 ],
 test="You have the Island Botanica message adapted into two audience versions and four channel versions (website, email, Instagram, 15-second script), refined through follow-up prompts and polished, with a consistency pass done so every piece shares one voice and one core message — saved in your project folder.",
 ),
 dict(
 num=7, topic=2,
 title="Generate Visual Concepts and Images with AI Image Tools",
 objective="Use AI image tools to generate a moodboard and on-brand hero images for Island Botanica, writing effective image prompts and iterating — giving the campaign its visual direction and key visuals.",
 desc="Now the campaign gets its look. In this lab you use an AI image tool to establish the visual direction "
 "and produce key visuals for Island Botanica. You first generate a moodboard — a set of reference visuals "
 "that fix the colour palette, style and mood — from the brand and collection. You learn to write a strong "
 "image prompt that names the subject, style, composition, lighting, colour palette, mood and aspect ratio, "
 "and you iterate: change one element at a time until the image is on-brand. You generate a hero product image "
 "and a lifestyle image, keeping a consistent style across the set. Throughout you apply Lab 4's responsible "
 "rules — you review every image for garbled text, fake logos and off-brand or impossible details, and you "
 "avoid imitating any real brand's or artist's protected look. " + PROJECT_NOTE,
 build="A visual concept moodboard and a small set of on-brand Island Botanica images (a hero product image and a lifestyle image) generated with an AI image tool, produced from well-structured image prompts, reviewed for honesty and consistency, saved in your project folder.",
 services="AI image tool (DALL·E / Gemini / Copilot / Firefly / Canva), image prompting (subject, style, composition, lighting, palette, mood, aspect ratio), moodboards, iterating and reviewing images",
 steps=[
 ("Set the visual direction with a moodboard prompt. Paste the prompt below into your AI image tool (or ask a chat assistant to describe the moodboard first, then generate).",
  "A moodboard for a premium artisanal candle collection inspired by Southeast Asian botanicals: soft natural light, warm earthy and botanical tones, marble and linen textures, frangipani and tropical foliage, calm and quietly luxurious, editorial product photography style. Square, 1:1."),
 ("Learn the anatomy of a strong image prompt: subject + style + composition + lighting + colour palette + mood + aspect ratio. Note how the moodboard prompt above names each of these.", ""),
 ("Generate a hero product image. Paste the prompt below, then iterate.",
  "A single artisanal candle in an amber glass vessel on a marble ledge, fresh frangipani blooms beside it, soft golden morning light, warm botanical colour palette, shallow depth of field, calm and premium, editorial product photography, 1:1."),
 ("Iterate one element at a time — change only the lighting, or only the palette, or only the composition, and regenerate — so you learn what each word does and steer the image on-brand. Keep the version closest to your moodboard.", ""),
 ("Generate a lifestyle image in the same style. Paste the prompt below.",
  "A serene Singapore home corner at dusk with the same amber candle lit, tropical plants softly blurred behind, warm ambient glow, wellness and calm mood, same editorial style and warm botanical palette as before, 4:5."),
 ("Review every image against Lab 4's rules: check for garbled text, fake logos or brand names, extra fingers or impossible details, and off-brand style; regenerate anything that fails, and add 'no text, no logos' to the prompt if needed. Keep the style consistent across the set.", ""),
 ("Save the moodboard and your chosen hero and lifestyle images (and the exact prompts that made them) in your project folder — the visual direction and key visuals for the social and launch content in Lab 8.", ""),
 ],
 test="You have a visual concept moodboard and at least two on-brand Island Botanica images (a hero product image and a lifestyle image) generated from structured image prompts, iterated one element at a time, reviewed for garbled text, fake logos and off-brand details, and kept consistent in style — all saved with their prompts in your project folder.",
 ),
 dict(
 num=8, topic=2,
 title="Create a Social Media and Launch Content Kit",
 objective="Combine your copy and images into a social media content kit and launch/presentation visuals for Island Botanica — platform-ready posts and visuals that share one voice, look and message.",
 desc="Now you assemble the words and pictures into things you could actually post. In this lab you use AI to "
 "turn the adapted copy from Lab 6 and the images from Lab 7 into a social media content kit and a set of "
 "launch visuals. You plan a short launch content calendar (a teaser, the reveal, the four scents, a "
 "gifting angle), then generate platform-ready captions for each post — Instagram, a story, and one more "
 "platform — each paired with the right image and aspect ratio. You use an AI-enabled design tool (Canva, "
 "Copilot Designer or your image tool) to combine copy and image into a launch/announcement visual and a "
 "simple presentation slide. Everything is held to the voice guide and the visual direction so the kit reads "
 "as one campaign. " + PROJECT_NOTE,
 build="A social media content kit for the Island Botanica launch — a short content calendar plus platform-ready captions paired with the right images and aspect ratios — and at least one combined launch/announcement visual and a presentation slide, all on one voice and look, saved in your project folder.",
 services="ChatGPT / Claude / Gemini / Copilot, an AI design tool (Canva / Copilot Designer / image tool), social content planning, platform captions, combining copy and image into launch visuals",
 steps=[
 ("Plan the launch content. Paste the prompt below.",
  "Plan a short Island Botanica launch social calendar of six posts on the Lumina Botanicals voice: a teaser, the collection reveal, one post for each of the four scents (Frangipani Dawn, Pandan & Vetiver, Kaffir Lime Grove, Ylang Midnight) folded across the remaining posts, and a gifting-season angle. For each post give the goal, the platform, and the visual to use."),
 ("Generate platform-ready captions. Paste the prompt below.",
  "For those posts, write the captions: an Instagram feed caption (under 30 words + three tasteful hashtags), an Instagram Story line (under 12 words), and one caption for another platform of your choice (e.g. Facebook or a marketplace listing). Keep every caption on voice and consistent with the others."),
 ("Pair each caption with the right image and shape: match your Lab 7 hero image (1:1) to feed posts and the lifestyle image (4:5 or 9:16) to stories, and note where you would generate one more image if a post needs its own visual.", ""),
 ("Combine copy and image into a launch visual. In an AI-enabled design tool (Canva, Copilot Designer or your image tool), place your chosen image, add the tagline and a short line of copy on-brand, and export a launch/announcement graphic. Keep text minimal and legible.", ""),
 ("Make one presentation slide for the pitch: a single clean slide that shows the collection — hero image, the collection name and the tagline — in the campaign's look. You reuse this in the Lab 11 pitch.", ""),
 ("Review the whole kit as a set: read the captions in order and view the visuals together, and fix anything off-voice or off-look so the kit clearly reads as one campaign.", ""),
 ("Save the content calendar, the captions, the paired images, the launch visual and the presentation slide in your project folder — the campaign now has its social and launch content.", ""),
 ],
 test="You have a six-post Island Botanica launch content calendar, platform-ready captions for each post paired with the right image and aspect ratio, at least one combined launch/announcement visual, and one presentation slide — all reviewed as a set so they share one voice and look — saved in your project folder.",
 ),
]
