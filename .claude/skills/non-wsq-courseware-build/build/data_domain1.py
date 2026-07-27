"""
Domain 1 — Getting Started with Generative AI for Creative Work. Labs 1-4.

THE CONNECTED PROJECT STARTS HERE, IN LAB 1.

Every lab in this course takes one connected deliverable — the Island Botanica
launch campaign for Lumina Botanicals, a fictional Singapore artisanal
home-fragrance brand — one stage further. Lab 1 sets up the AI creative toolkit;
Lab 2 builds a reusable creative prompt library; Lab 3 defines and locks the
brand's tone, style and voice; Lab 4 sets the responsible-use ground rules for
the whole campaign. A Lumina Botanicals brief with the brand facts you need is
supplied; use your own non-confidential creative project instead wherever you
prefer.
"""

SCENARIO = (
 "Lumina Botanicals is a fictional Singapore artisanal home-fragrance and wellness brand — small-batch candles, "
 "reed diffusers and room mists scented with Southeast Asian botanicals. After five years building a loyal "
 "following, it is launching a limited-edition signature collection, Island Botanica: four scents inspired by "
 "regional flora — Frangipani Dawn, Pandan & Vetiver, Kaffir Lime Grove and Ylang Midnight — timed for the "
 "year-end gifting and Lunar New Year season. You are the creative lead preparing the launch campaign — the "
 "Island Botanica campaign pack — which must tell the collection's story and sell it: a brand story, hero "
 "taglines and product copy, copy adapted for different audiences, a visual moodboard and on-brand images, a "
 "social and launch content kit, a set of bigger campaign ideas, and a creative pitch to present it all. Across "
 "this course you take that campaign from a blank page to a finished, pitch-ready pack using ChatGPT, Claude, "
 "Gemini, Microsoft Copilot and an AI image tool. Use this scenario only if you cannot use a real, "
 "non-confidential creative project of your own; your own brief is always welcome."
)

PROJECT_NOTE = (
 "BUILDING BLOCK — what you create in this lab becomes part of your Island Botanica campaign pack, "
 "the connected campaign you assemble across all 11 labs."
)

DOMAIN1 = [
 dict(
 num=1, topic=1,
 title="Set Up Your AI Creative Toolkit",
 objective="Sign in to ChatGPT, Claude, Gemini, Microsoft Copilot and an AI image tool, run your first creative prompts, and learn the generate–review–refine loop and where AI helps across the creative process — the foundation every later lab uses.",
 desc="This lab gets you comfortable with the tools before any real creative work begins. You open the chat "
 "assistants (ChatGPT, Claude, Gemini and Microsoft Copilot), confirm you are signed in, and run a simple "
 "creative prompt so you see how each generates ideas, then run the same prompt in a second assistant to feel "
 "how they differ. You open an AI image tool, sign in, and generate a quick throwaway image from a one-line "
 "prompt so you can see what image generation does. You map where AI genuinely helps across the creative "
 "process (inspiration, ideation, drafting, refining, producing, presenting) and where it needs you (taste, "
 "intent, originality, judgement). By the end you understand the generate -> review -> refine loop that is the "
 "heart of every lab. " + PROJECT_NOTE,
 build="Your AI creative toolkit set up and tested — at least one chat assistant and one AI image tool signed in and responding — a first throwaway AI-generated idea list and image, and a clear, written map of where AI helps across the creative process and the generate–review–refine loop.",
 services="ChatGPT, Claude, Gemini, Microsoft Copilot, an AI image tool, account sign-in, first creative prompts, comparing assistants, the generate–review–refine loop",
 steps=[
 ("Create a project folder on your machine called 'Island-Botanica-Campaign' so every file and note you make today stays together. Open ChatGPT (chat.openai.com), Claude (claude.ai), Gemini (gemini.google.com) and Microsoft Copilot (copilot.microsoft.com) in browser tabs and confirm you are signed in to at least one.", ""),
 ("In one chat assistant, run a simple first creative prompt to see how it generates ideas. Paste the prompt below and read the reply.",
  "You are a brand creative director. Give me eight short, evocative name ideas for a limited-edition candle scent inspired by Singapore's frangipani flowers at dawn. Keep each to two or three words."),
 ("Run the exact same prompt in a second assistant and compare the two replies. Notice differences in tone, imagination and range — the skill you learn transfers across all of them, so use whichever you prefer for a given task.",
  "You are a brand creative director. Give me eight short, evocative name ideas for a limited-edition candle scent inspired by Singapore's frangipani flowers at dawn. Keep each to two or three words."),
 ("Open your AI image tool (DALL·E in ChatGPT, Gemini, Microsoft Copilot / Designer, Adobe Firefly or Canva), sign in, and generate a quick throwaway image from a one-line prompt so you can see what image generation produces. Paste the prompt below.",
  "A luxury artisanal candle on a marble surface with fresh frangipani flowers, soft morning light, calm and elegant, product photography."),
 ("Look at what the image tool produced — a generated visual from a text description, in seconds. Note that it is a fast starting point, not a finished asset, and that AI images can invent odd details. You will not keep this one; it is only to feel the tool.", ""),
 ("Map where AI helps across the creative process. In one line each, note how AI could help at inspiration, ideation, drafting, refining, producing and presenting — and where it needs you (it does not know the Lumina Botanicals brand, your audience, or what is genuinely original). This good/not-good picture guides how you use AI all day.", ""),
 ("Open the supplied Lumina Botanicals brief (labs/reference-pack/): the brand story, the Island Botanica collection and its four scents, the audiences, and the brand voice notes. Skim it so you know the campaign you are about to build.", ""),
 ("Save your notes into your Island-Botanica-Campaign folder. Write one line, in your own words, describing the generate -> review -> refine loop — you rely on it in every later lab.", ""),
 ],
 test="You have signed in to at least one chat assistant and to an AI image tool, run the same prompt in two assistants and compared them, generated a throwaway image, written a one-line map of where AI helps across the creative process and what it is not good at, skimmed the Lumina Botanicals brief, and described the generate–review–refine loop in your own words — all saved in your Island-Botanica-Campaign folder.",
 ),
 dict(
 num=2, topic=1,
 title="Master Creative Prompting",
 objective="Turn a vague creative ask into a strong, structured prompt (role, context, task, format, constraints) for creative tasks, and save a reusable creative prompt library for the work you repeat on every project.",
 desc="A good creative result starts with a good prompt, not a lucky one. In this lab you read the Lumina "
 "Botanicals brief and write a deliberately vague prompt first, so you see how generic the result is. You then "
 "rebuild it with five clear parts — a role for the AI, the context (brand, audience, goal), the exact task, "
 "the format you want back, and clear constraints (tone, length, what to avoid) — and watch the output become "
 "genuinely usable and on-brand. You run small single-change edits to feel how each part matters, then save "
 "your best versions as a reusable creative prompt library with clearly marked slots, covering the tasks you "
 "repeat on every creative project: ideation, copywriting, image prompts, adaptation and social captions. " + PROJECT_NOTE,
 build="A structured creative prompt built from role, context, task, format and constraints, plus a reusable creative prompt library with clearly marked slots for the recurring creative tasks, saved in your project folder.",
 services="ChatGPT / Claude / Gemini / Copilot, the structured prompt framework (role, context, task, format, constraints), prompt iteration, a reusable creative prompt library",
 steps=[
 ("Open the Lumina Botanicals brief and note two things you will reuse in every prompt: who the audience is (premium gift-shoppers and wellness-seekers) and the goal (launch the Island Botanica collection).", ""),
 ("Write a deliberately vague first prompt in any assistant and generate, so you can see the generic result. Paste the prompt below and read how unfocused and clichéd the reply is.",
  "Write some marketing copy for a candle."),
 ("Rebuild the prompt with a role and the context, and regenerate. Paste the prompt below and compare it with the vague version.",
  "You are a senior copywriter for premium lifestyle brands. Context: Lumina Botanicals is a Singapore artisanal home-fragrance brand launching Island Botanica, a limited-edition collection of four botanical scents for the year-end gifting season, aimed at premium gift-shoppers and wellness-seekers. Draft a short hero description for the collection."),
 ("Now add the exact task, the format you want back, and clear constraints, and regenerate. Paste the prompt below.",
  "As the same copywriter, write three options for a 40-word hero description of the Island Botanica collection. Make it warm, sensory and elegant; avoid clichés like 'elevate your space' and 'the perfect gift'; do not invent awards or claims. Present them as a numbered list."),
 ("Put the vague result and the structured result side by side. Note in one line how much more usable and on-brand the structured prompt was — this is the core lesson of the day.", ""),
 ("Run two or three single-change edits to feel how each part steers the result — for example change the audience to 'young first-time candle buyers', or change the tone to 'playful and modern' — and note which you would keep for Island Botanica.", ""),
 ("Save a reusable creative prompt library in your project folder: templates for ideation, copywriting, image prompts, audience adaptation and social captions, each with clearly marked slots — [ROLE], [CONTEXT], [AUDIENCE], [TASK], [FORMAT], [CONSTRAINTS] — that you fill in for any future creative project.", ""),
 ],
 test="You have compared a vague prompt with a structured one built from role, context, task, format and constraints, seen how much better and more on-brand the structured prompt performs, run single-change edits to feel each part, and saved a reusable creative prompt library with marked slots for the recurring creative tasks in your project folder.",
 ),
 dict(
 num=3, topic=1,
 title="Define Your Brand's Tone, Style and Voice",
 objective="Use AI to define and lock a clear brand tone, style and voice for Island Botanica — the guide every later lab's copy and content is held to — so the whole campaign sounds like one brand.",
 desc="A campaign only sounds like itself when its voice is defined. In this lab you use a chat assistant to "
 "articulate the Lumina Botanicals voice from the brief: the tone (the mood — for example warm, sensory, "
 "calm and quietly luxurious), the style (the craft — sentence length, rhythm, vocabulary), and the voice "
 "(the consistent personality). You generate a set of voice attributes and, crucially, sample on-voice and "
 "off-voice lines side by side so the guide is usable, plus a short 'words we use / words we avoid' list. You "
 "then test the guide by asking the AI to rewrite a flat line in the defined voice, and refine the guide until "
 "the rewrite genuinely sounds like the brand. This voice guide governs every word you generate for the rest "
 "of the day. " + PROJECT_NOTE,
 build="A brand tone, style and voice guide for Island Botanica — three to five voice attributes, sample on-voice vs off-voice lines, and a short 'words we use / words we avoid' list — tested by rewriting a flat line in the voice, saved in your project folder.",
 services="ChatGPT / Claude / Gemini / Copilot, defining tone, style and voice, voice attributes, on-voice vs off-voice examples, a brand-voice guide",
 steps=[
 ("Open the Lumina Botanicals brief and read the brand story and voice notes — the brand is artisanal, botanical, rooted in Southeast Asia, wellness-minded and quietly premium. These are the raw material for the voice.", ""),
 ("Ask AI to articulate the voice from the brief. Paste the prompt below.",
  "You are a brand voice strategist. Based on this brand — Lumina Botanicals, a Singapore artisanal home-fragrance brand: small-batch, botanical, rooted in Southeast Asian flora, wellness-minded and quietly premium — define its brand voice. Give me: (1) three to five voice attributes, each with a one-line description; (2) the tone and the writing style; (3) the kind of personality it should feel like. Keep it concise."),
 ("Make the guide usable with concrete examples. Paste the prompt below.",
  "For that Lumina Botanicals voice, write three short example lines that are ON voice and, next to each, a version that is OFF voice (too generic, too salesy or too casual), and one line explaining the difference. Then give me a short 'words and phrases we use' and 'words and phrases we avoid' list."),
 ("Test the guide on a real line. Paste the prompt below and judge whether the rewrite truly sounds like the brand.",
  "Here is a flat product line: 'Our new candles smell great and make a good gift.' Rewrite it in three ways that fully match the Lumina Botanicals voice you defined, keeping each under 25 words."),
 ("Judge and refine: if a rewrite still sounds generic or off, tell the AI exactly what is wrong ('too salesy', 'not sensory enough', 'drop the exclamation') and regenerate until it lands. Tighten your voice attributes based on what you learn.", ""),
 ("Sanity-check the guide against the audiences: confirm the same voice can flex for premium gift-shoppers and for wellness-seekers without becoming a different brand. Note any adjustment.", ""),
 ("Save the final tone, style and voice guide — attributes, on-voice/off-voice examples, and the words-we-use/avoid list — in your project folder. Every later lab holds its copy to this guide.", ""),
 ],
 test="You have a brand tone, style and voice guide with three to five voice attributes, side-by-side on-voice and off-voice example lines, and a words-we-use/words-we-avoid list — tested by rewriting a flat line so it genuinely sounds like Lumina Botanicals — saved in your project folder.",
 ),
 dict(
 num=4, topic=1,
 title="Create Responsibly: Originality, Copyright and Ethics",
 objective="Set the responsible-use ground rules for the whole campaign — protect originality, avoid copying real brands or living artists, understand AI-image rights, and be transparent about AI assistance — before you generate any deliverable.",
 desc="Before you produce the campaign, you agree how you will produce it responsibly. In this lab you use AI "
 "to build a practical responsible-use checklist for a creative project, then apply it to Island Botanica. You "
 "probe where AI creative work goes wrong — echoing an existing brand or a living artist's protected style, "
 "presenting AI output as wholly original, using invented 'facts' or fake awards in copy, ignoring an image "
 "tool's usage rights, or hiding AI assistance where it matters — and you decide the brand's position on each. "
 "Crucially, you practise the originality habit: you take a sample AI line and note how you would transform it "
 "into something genuinely the brand's own. By the end you have the ground rules that keep every later lab's "
 "output original, honest and safe to publish. " + PROJECT_NOTE,
 build="A responsible-use checklist for the campaign — covering originality, copyright and imitation, AI-image rights, honesty of claims, confidential material and disclosure — applied to Island Botanica, plus a short note on how you will transform AI drafts into genuinely original work.",
 services="ChatGPT / Claude / Gemini / Copilot, responsible AI use, originality and copyright, AI-image rights, transparency and disclosure",
 steps=[
 ("Ask AI to draft a responsible-use checklist for an AI-assisted creative campaign. Paste the prompt below.",
  "You are a creative ethics advisor. I am using generative AI to create a product launch campaign (copy and images) for a small brand. Give me a practical, plain-language checklist for using AI responsibly — covering originality, copyright and imitating existing brands or living artists, the rights around AI-generated images, honesty of claims, keeping confidential material out of public tools, and being transparent about AI assistance. Keep each point to one line."),
 ("Stress-test the risks with a critical question. Paste the prompt below and read the answer carefully.",
  "For an AI-generated candle brand campaign, what are the most common ways it could accidentally copy an existing brand's identity or a living artist's style, or make a claim it can't back up — and how do I avoid each?"),
 ("Decide Lumina Botanicals' position on the key questions: Will you imitate any real brand's look or voice? (No.) How will you handle AI-generated images — check the tool's usage rights and avoid real logos and artist names? Will you disclose AI assistance, and where? Write a one-line answer for each.", ""),
 ("Practise the originality habit. Paste the prompt below, then note in your own words how you would change the line to make it specifically Lumina Botanicals' own.",
  "Give me one deliberately generic candle tagline that could belong to any brand. Then explain what would make it un-original, and what a brand would need to add to make it genuinely its own."),
 ("Note the confidential-material rule: you will use only the supplied fictional Lumina Botanicals brief (or your own non-confidential material), never real client secrets, unpublished financials or personal data, in a public AI tool.", ""),
 ("Check your image-tool's rules: open the AI image tool you plan to use and find its statement on ownership and commercial use of generated images. Note in one line what it allows, so Lab 7's images are safe to use.", ""),
 ("Save your responsible-use checklist, Lumina Botanicals' decisions, and your originality note in your project folder. These ground rules apply to every deliverable you create for the rest of the day.", ""),
 ],
 test="You have a responsible-use checklist applied to Island Botanica — covering originality, copyright and imitation, AI-image rights, honesty of claims, confidential material and disclosure — a decided position on each key question, a note on how you will transform AI drafts into original work, and a one-line record of your image tool's usage rules, all saved in your project folder.",
 ),
]
