"""
SINGLE SOURCE OF TRUTH — C1276 Generative AI for Creativity (non-WSQ).

An intensive, one-day, hands-on course on using generative AI as a creative
partner — to ideate, write, illustrate and present original creative work.
Using general chat assistants (ChatGPT, Claude, Gemini and Microsoft Copilot)
and AI image tools, learners take one creative campaign — the Island Botanica
launch for a fictional Singapore home-fragrance brand, Lumina Botanicals — from
a blank page to a finished, pitch-ready creative pack: setting up an AI creative
toolkit and prompt library, defining a brand tone, style and voice, creating
responsibly, drafting the brand story and marketing copy, adapting it for
different audiences, generating visual concepts and images, building a social
and launch content kit, brainstorming big campaign ideas, breaking creative
blocks, combining tools into a repeatable workflow, and pitching the campaign.
Every artifact (PPT, LP, LG, LG.md) and every lab is generated from this module
+ data_domainN.py so they stay 100% aligned.

NON-WSQ RULES — the engine enforces these, do not reintroduce them here:
  * NO assessment of any kind (no WA/SAQ, no PP, no case study, no marking).
  * NO SSG / SkillsFuture / WSQ funding or subsidy content.
  * NO TRAQOM survey, NO digital attendance, NO 75% attendance rule.
  * NO TGS course reference — this course carries the plain code C1276.
"""

# ------------------------------------------------------------------ metadata
TITLE        = "Generative AI for Creativity (C1276)"
SHORT_TITLE  = "Generative AI for Creativity (C1276)"   # used in output filenames
COURSE_CODE  = "C1276"                                   # non-WSQ code — never a TGS- ref
VERSION      = "v1.0"
VERSION_DATE = "27 July 2026"
ORG          = "Tertiary Infotech Academy Pte Ltd"
UEN          = "UEN: 201200696W"
TRAINER      = "Dr. Alfred Ang"
DAYS         = 1
MODE         = "Instructor-led, hands-on practical labs"

DARK_THEME = False

# ------------------------------------------------------------------ outcomes
LEARNING_OUTCOMES = [
    "LO1: Explain how generative AI supports the creative process, and set up an AI creative toolkit — general chat assistants (ChatGPT, Claude, Gemini, Copilot) and an AI image tool — for creative work.",
    "LO2: Write effective, structured prompts for creative tasks and build a reusable creative prompt library.",
    "LO3: Use generative AI to define and lock a consistent brand tone, style and voice for a creative project.",
    "LO4: Apply responsible-use practices to AI creative work — originality, copyright, AI-image rights and transparent disclosure.",
    "LO5: Draft a brand story, taglines and marketing copy with AI, on a defined brand voice.",
    "LO6: Rewrite, polish and adapt creative copy for different audiences and channels, iterating with follow-up prompts.",
    "LO7: Generate visual concepts and on-brand images with AI image tools using effective image prompts.",
    "LO8: Create a social media content kit and presentation/launch visuals with AI.",
    "LO9: Brainstorm ideas and build a mind map with AI, then challenge conventional thinking and overcome creative blocks.",
    "LO10: Combine multiple AI tools into a repeatable creative workflow and present and pitch creative ideas with AI support.",
]
LO_TITLES = [
    "AI creative toolkit",
    "Creative prompting",
    "Tone, style & voice",
    "Responsible creativity",
    "Story & copy",
    "Adapt & iterate",
    "Visual concepts & images",
    "Social & launch content",
    "Ideation & mind maps",
    "Workflow & pitch",
]

# ------------------------------------------------------------------ topics
# `concepts` are plain strings ("Title — explanation.") so they render cleanly
# as both slide tiles and Learner-Guide bullets. `weighting` = share of course time.
TOPICS = [
    dict(num=1, code="01",
         title="Getting Started with Generative AI for Creative Work",
         subtitle="Overview of generative AI tools (ChatGPT, Claude, Gemini, Copilot) · How generative AI supports the creative process · Prompt engineering essentials for creative output · Setting tone, style and voice · Copyright, originality and responsible use",
         weighting="35%",
         concepts=[
            "Generative AI as a creative partner — a generative AI assistant is a tireless collaborator across the whole creative process: it brainstorms, drafts, rewrites, illustrates and critiques, turning a blank page into a fast first draft you shape into something original and your own.",
            "Where AI helps in the creative process — creativity moves through stages (gather inspiration, ideate, draft, refine, produce, present); AI can accelerate every stage, but the taste, intent, judgement and originality remain yours.",
            "Popular GenAI tools — ChatGPT, Claude, Gemini and Microsoft Copilot are general chat assistants that generate and refine text and ideas; AI image tools (DALL·E in ChatGPT, Midjourney, Adobe Firefly, Gemini, Canva, Copilot Designer) generate visuals from a prompt. The prompting skills you learn transfer across all of them.",
            "What AI is good (and not good) at — AI is strong at volume, variation, drafting and remixing; it is weak at knowing your brand, your audience and what is genuinely fresh, and it will confidently state things that are wrong, so you curate, verify and decide.",
            "The generate–review–refine loop — every creative AI task follows the same loop: you prompt, the AI generates options, you review them with a critical eye, and you refine with follow-up prompts and your own edits until it is right. This loop drives every lab.",
            "Prompting is the core creative skill — a strong creative prompt gives the AI a role, the context (brand, audience, goal), the exact task, the format you want back and clear constraints (tone, length, what to avoid); a vague ask gives generic output, a structured ask gives usable, on-brand output.",
            "A reusable creative prompt library — the same creative tasks recur on every project (ideation, copywriting, image prompts, adaptation, social captions), so you save your best prompts as reusable templates with clearly marked slots you fill in for any brief.",
            "Tone, style and voice — a brand or piece of work sounds like itself only when its voice is defined; you use AI to articulate the tone (the mood), the style (the craft of the writing) and the voice (the consistent personality), then hold every AI output to that guide.",
            "Copyright and originality — AI is trained on existing work and can echo it, so you never pass off AI output as wholly original without review; you avoid imitating a living artist's or a real brand's protected style, add your own creative direction, and treat AI output as raw material you transform.",
            "Responsible and transparent use — you keep confidential or unpublished material out of public AI tools, check facts and claims, respect the rights around AI-generated images, and are transparent about AI assistance where it matters, so the creative work is both original and trustworthy.",
         ]),
    dict(num=2, code="02",
         title="Creating Written and Visual Content with AI",
         subtitle="Drafting stories, scripts and marketing copy · Rewriting, polishing and adapting for different audiences · Generating images and visual concepts with AI image tools · Creating social media and presentation visuals · Iterating on drafts with follow-up prompts",
         weighting="40%",
         concepts=[
            "Drafting written content with AI — on a defined brand voice, AI drafts stories, scripts, taglines and marketing copy fast; you give it the brief and voice, generate several options, and choose and sharpen the strongest rather than accepting the first.",
            "Copy is a draft, not a deliverable — every AI draft is a starting point: you cut the clichés and filler, add the specific, true details only you know, and make the words genuinely yours before they go out.",
            "Rewriting and polishing — AI is excellent at rewriting: tightening, changing the reading level, fixing rhythm, or offering ten variations of a headline; you use it to iterate quickly and pick the best, not to settle for 'good enough'.",
            "Adapting for different audiences and channels — one core message becomes many pieces: a website paragraph, an email, an Instagram caption, a 15-second script, a gift-shopper line versus a wellness-seeker line. AI adapts tone, length and framing for each while keeping the message consistent.",
            "Iterating with follow-up prompts — the real power is the conversation: you refine with follow-ups ('make it warmer', 'half the length', 'more sensory', 'give me three bolder options'), steering the draft step by step instead of re-writing the prompt from scratch.",
            "Generating images and visual concepts — AI image tools turn a text prompt into visuals; a strong image prompt names the subject, the style, the composition, the lighting, the colour palette, the mood and the aspect ratio, and you iterate to get an on-brand result.",
            "Moodboards and visual direction — before hero images, you use AI to generate a moodboard — a set of reference visuals that set the look and feel — so the whole campaign shares one consistent visual language.",
            "Honest, on-brand visuals — AI images can invent garbled text, fake logos and impossible details, and can drift off-brand; you review every image, avoid imitating a real brand's or artist's protected look, and keep a consistent style across the set.",
            "Social media and presentation visuals — AI helps produce a social content kit (post concepts and captions per platform) and launch or presentation visuals that combine your copy and images, ready to schedule or present.",
            "Content that works together — written and visual content are strongest when they are made as a set: the copy, the images and the social posts share one voice, one look and one message, which is exactly what your campaign pack becomes.",
         ]),
    dict(num=3, code="03",
         title="AI-Assisted Ideation and Creative Workflows",
         subtitle="Brainstorming ideas and building mind maps · Using AI to challenge conventional thinking and explore alternatives · Overcoming creative blocks with AI prompting techniques · Combining multiple AI tools into a creative workflow · Presenting and pitching creative ideas with AI support",
         weighting="25%",
         concepts=[
            "Brainstorming at scale — AI removes the fear of the blank page: it generates dozens of ideas on demand, in different directions, so you start from abundance and curate down, rather than straining to produce a single idea.",
            "Divergent then convergent — good ideation first diverges (generate widely, defer judgement) and then converges (cluster, compare and shortlist); AI is a powerful partner for both — quantity first, then a structured cut to the best.",
            "Building a mind map with AI — you use AI to organise a flood of ideas into a mind map — a central theme with branches and sub-branches — so patterns, clusters and gaps become visible and the strongest territory stands out.",
            "Challenging conventional thinking — AI is a fast way to escape the obvious: you ask it for the opposite of the safe idea, unexpected analogies, 'what would a totally different brand do', or to combine two unrelated concepts, and you mine the surprises for something fresh.",
            "Provocation and lateral techniques — prompting techniques such as SCAMPER, random-stimulus, role-play ('pitch this as a filmmaker / a poet / a rival brand') and 'reverse the brief' push the AI — and you — past the first, safe answer into more original territory.",
            "Overcoming creative blocks — when you are stuck, AI is a way back in: it offers a starting sentence, three possible directions, a change of format, or a constraint to react against, so momentum returns and you have material to shape.",
            "Combining multiple AI tools into a workflow — real creative work chains tools: a chat assistant to ideate and write, an image tool to visualise, a design or slide tool to assemble; you learn to move content between them so the pieces build one coherent result.",
            "A repeatable creative workflow — once you have a chain that works — brief → ideate → draft → visualise → assemble → refine — you document it as a reusable workflow you can run for any future creative project, not just this one.",
            "Presenting and pitching with AI — a creative idea only lands if it is presented well; AI helps you structure the pitch, write the narrative, anticipate the client's questions and rehearse, so the concept is understood and bought.",
            "You are the creative director — across every technique, AI generates and suggests, but you set the brief, judge the options, protect the originality and make the final call; the tools amplify your creativity, they do not replace it.",
         ]),
]

# ------------------------------------------------------------------ day themes
DAY_THEMES = {
    1: "Build the Island Botanica launch campaign end to end with AI — set up a creative toolkit and brand voice, draft the story, copy and visuals, build the social and launch content, then ideate, refine and pitch the campaign.",
}

# ------------------------------------------------------------------ schedule
# NON-WSQ: no assessment blocks. The day totals exactly 480 scheduled minutes
# (excluding the 1-hour lunch); the 30 minutes of tea breaks sit inside that, so
# the instructional total is 7.5 hours.
def SCHEDULE(lab_titles):
    return {
     1: (DAY_THEMES[1], [
        ("9:00","9:20",20,"admin","Welcome, course introduction, ground rules, and setup: signing in to ChatGPT, Claude, Gemini and Microsoft Copilot and to an AI image tool, and confirming each tool is ready for the labs"),
        ("9:20","10:00",40,"topic","TOPIC 01 — Getting Started with Generative AI for Creative Work: overview of generative AI tools (ChatGPT, Claude, Gemini, Copilot); how generative AI supports the creative process; prompt engineering essentials for creative output; setting tone, style and voice; copyright, originality and responsible use (concepts + live demo)"),
        ("10:00","10:45",45,"lab","Hands-on: "+lab_titles([1])),
        ("10:45","11:00",15,"break","Tea break"),
        ("11:00","13:00",120,"lab","Hands-on: "+lab_titles([2,3,4])),
        ("13:00","14:00",60,"lunch","Lunch break"),
        ("14:00","14:30",30,"topic","TOPIC 02 — Creating Written and Visual Content with AI: drafting stories, scripts and marketing copy; rewriting, polishing and adapting for different audiences; generating images and visual concepts with AI image tools; creating social media and presentation visuals; iterating with follow-up prompts (concepts + live demo)"),
        ("14:30","16:00",90,"lab","Hands-on: "+lab_titles([5,6,7,8])),
        ("16:00","16:15",15,"break","Tea break"),
        ("16:15","16:40",25,"topic","TOPIC 03 — AI-Assisted Ideation and Creative Workflows: brainstorming ideas and building mind maps; challenging conventional thinking and exploring alternatives; overcoming creative blocks; combining multiple AI tools into a creative workflow; presenting and pitching creative ideas with AI support (concepts + live demo)"),
        ("16:40","17:50",70,"lab","Hands-on: "+lab_titles([9,10,11])),
        ("17:50","18:00",10,"recap","Course wrap-up, presenting the Island Botanica campaign, responsible-AI and originality recap, and next steps"),
     ]),
    }

# ------------------------------------------------------------------ deck content
COURSE_OVERVIEW = dict(
    section_title="Course Fundamentals",
    concepts_title="What Generative AI for Creativity Really Is",
    concepts=[
        "A partner for the whole creative process — you describe a creative task in words and AI returns usable first drafts (ideas, copy, images, a moodboard, a pitch) in seconds, which you then curate, refine and make your own.",
        "Two toolsets, one campaign — chat assistants (ChatGPT, Claude, Gemini, Copilot) generate the ideas and words; AI image tools generate the visuals. You learn to move creative work smoothly between them.",
        "Generate, review, own — the workflow is always the same: give a structured prompt, review the options with taste and judgement, and take ownership of the result. The AI generates; you direct, curate and decide.",
        "Originality is the craft — the point is not making creative work faster; it is using AI to escape the blank page and explore more widely, then bringing your own taste, intent and originality so the result is genuinely yours.",
    ],
    framework_title="The AI-Assisted Creative Workflow",
    framework=[
        ("Set the brief", "Get clear on the brand, the audience and the goal, and define the tone, style and voice — so every AI output is judged against a real creative brief, not generated in a vacuum."),
        ("Ideate", "Use AI to brainstorm widely and map the territory, challenge the obvious and break creative blocks, then converge on the strongest directions."),
        ("Create", "Draft the story and copy, generate visual concepts and images, and build the social and launch content — all on one voice and one look."),
        ("Refine", "Review every draft and image with a critical eye; cut clichés, fix off-brand or dishonest visuals, adapt for each audience, and make the work original and true."),
        ("Present", "Combine the pieces into a repeatable workflow, then build and rehearse the pitch and present the campaign with confidence — the creative direction is yours."),
    ],
    statement=dict(
        headline="Generative AI gives you a fast first draft of every part of a creative project — the craft is prompting well, exploring boldly, curating with taste, protecting originality, and directing the work yourself.",
        body="This course is hands-on: you take one creative campaign — the Island Botanica launch for Lumina Botanicals, a fictional Singapore artisanal home-fragrance brand releasing a limited-edition botanical collection — from a blank page to a finished, pitch-ready creative pack, using ChatGPT, Claude, Gemini, Microsoft Copilot and an AI image tool.",
        kicker="THE CREATIVE RULE",
    ),
    pillars_title="What You'll Build",
    pillars=[
        ("An AI creative toolkit", ["ChatGPT, Claude, Gemini, Copilot and an image tool set up", "A reusable creative prompt library", "A locked brand tone, style and voice guide"]),
        ("Written creative content", ["A brand story and hero taglines", "Product copy for the collection", "Copy adapted for every audience and channel"]),
        ("Visual creative content", ["A moodboard and visual direction", "On-brand hero and lifestyle images", "A social content kit and launch visuals"]),
        ("Ideas, workflow and a pitch", ["A brainstormed idea list and mind map", "A repeatable multi-tool creative workflow", "A rehearsed creative pitch for the campaign"]),
    ],
    arc_title="How Every Lab Works",
    arc=[
        "The trainer demonstrates the AI technique on the shared Island Botanica campaign example.",
        "You run it yourself in ChatGPT, Claude, Gemini, Copilot or your AI image tool using the supplied Lumina Botanicals brief.",
        "You verify the result against the lab's explicit 'Test it' check.",
        "You review and refine — curate the options, cut the clichés, fix anything off-brand, and make it original — until it meets the standard.",
        "You keep the reviewed output — each becomes the next part of your Island Botanica campaign pack.",
    ],
)

# ------------------------------------------------------------------ LG content
LG_INTRO = (
    "This Learner Guide accompanies the Generative AI for Creativity (C1276) course, conducted by "
    "Tertiary Infotech Academy Pte Ltd. It carries the full detail of all 11 hands-on labs, in the order you "
    "will run them, together with the concepts each lab depends on."
)
LG_INTRO2 = (
    "The labs build a single, connected deliverable — the Island Botanica launch campaign, a creative campaign "
    "for Lumina Botanicals, a fictional Singapore artisanal home-fragrance brand releasing a limited-edition "
    "botanical collection. You start in Lab 1 by setting up ChatGPT, Claude, Gemini, Microsoft Copilot and an AI "
    "image tool as a creative toolkit, then in every lab you take the campaign one stage further — a reusable "
    "creative prompt library, a locked brand tone, style and voice, a responsible-use check, the brand story and "
    "marketing copy, copy adapted for different audiences, visual concepts and on-brand images, a social and "
    "launch content kit, a brainstormed idea list and mind map, challenged and unblocked directions, a "
    "repeatable creative workflow, and finally a rehearsed creative pitch. A Lumina Botanicals brief with the "
    "brand facts you need is supplied in labs/reference-pack/; you may substitute your own non-confidential "
    "creative project wherever you prefer."
)
LG_SETUP = dict(
    needs=[
        "A laptop (Windows or Mac) with a modern web browser (Chrome, Edge, Safari or Firefox) and a reliable internet connection — every generative feature runs in the cloud.",
        "Access to at least one general chat assistant — ChatGPT (chat.openai.com), Claude (claude.ai), Gemini (gemini.google.com) or Microsoft Copilot (copilot.microsoft.com); a free account for each is enough to follow the labs, and the trainer will confirm what is available.",
        "Access to one AI image tool — the image feature in ChatGPT (DALL·E), Gemini, Microsoft Copilot / Designer, Adobe Firefly (firefly.adobe.com) or Canva (canva.com). A free option is enough to generate the visuals.",
        "A signed-in account for each tool you will use, tested before Lab 1 with a simple 'hello' prompt so you know it responds, plus somewhere to keep your work (a documents folder or notes app).",
        "The supplied Lumina Botanicals brief and fact sheet (brand story, the Island Botanica collection, audiences and voice notes) in labs/reference-pack/ — or a few notes and non-confidential facts from your own creative project to use instead.",
    ],
    verify_text="Before Lab 1, confirm you can sign in to at least one chat assistant and to an AI image tool, send a simple prompt and get a reply, and that you have the Lumina Botanicals brief to hand. If anything is missing, tell the trainer.",
    verify_code="Open chat.openai.com (ChatGPT) · claude.ai (Claude) · gemini.google.com (Gemini) · copilot.microsoft.com (Copilot)  ·  sign in  ·  send \"Hello, are you ready to help me build a creative campaign?\"  ·  confirm a reply",
    conventions=[
        "Placeholders such as <YOUR BRAND>, <YOUR AUDIENCE> or <PASTE COPY> are replaced with your own values before you send a prompt.",
        "Prompts to paste into ChatGPT, Claude, Gemini, Copilot or your AI image tool are shown in the 'Prompt to use' blocks — adapt the bracketed parts to your own project.",
        "Where a lab says 'any assistant', use whichever chat tool you prefer; the image steps use any AI image tool you have access to.",
        "Every lab ends with a 'Test it' step — an explicit check that the reviewed output meets the standard before you move on.",
        "Keep every reviewed output and prompt in one project folder (Island-Botanica-Campaign) so your campaign and its material stay together and consistent.",
    ],
)
LAB_NOTE = (
    "Use only ideas, data and material you are authorised to use. Do not paste confidential brand material, "
    "personal information, credentials or unpublished work into a public AI tool. Use the supplied Lumina "
    "Botanicals brief rather than real client material, treat every AI output — especially copy and images — as "
    "a first draft to be reviewed, fact-checked and made original, avoid imitating a living artist's or a real "
    "brand's protected style, and be transparent about AI assistance where appropriate before the work goes to "
    "a real audience."
)
LG_WRAPUP = dict(
    title="Wrap-Up",
    intro="You have taken one creative campaign — the Island Botanica launch — from a blank page to a finished, pitch-ready pack in a single day, using ChatGPT, Claude, Gemini, Microsoft Copilot and an AI image tool as creative partners while keeping the ideas, the voice, the originality and the creative direction your own.",
    sections=[
        dict(title="What you built", bullets=[
            "An AI creative toolkit — ChatGPT, Claude, Gemini, Copilot and an AI image tool set up, plus a reusable creative prompt library and a locked brand tone, style and voice.",
            "Written creative content — a brand story, hero taglines and product copy, adapted for every audience and channel, created responsibly and made original.",
            "Visual creative content — a moodboard and visual direction, on-brand hero and lifestyle images, and a social and launch content kit.",
            "Ideas, workflow and a pitch — a brainstormed idea list and mind map, challenged and unblocked directions, a repeatable multi-tool creative workflow, and a rehearsed creative pitch.",
            "One connected campaign pack that carries the whole idea — story, copy, visuals, social and pitch — ready to present.",
        ]),
        dict(title="What to do next", bullets=[
            "Rebuild a campaign for a real, non-confidential creative project of your own using the same workflow and prompt library.",
            "Introduce your saved prompts and brand-voice guide to your team so everyone creates on the same voice and look.",
            "Always start with the brief, the audience and the voice before you generate — AI makes exploring wider faster, it does not supply your taste or intent.",
            "Keep the originality habit: curate, cut clichés, transform AI output, respect others' work, and be transparent about AI assistance.",
        ]),
    ],
)
LG_NEXT_STEPS = [
    "First pass: complete every lab yourself, following the steps and verifying each 'Test it' check.",
    "Second pass: rebuild the campaign for your own real, non-confidential creative project, from brief and voice to a rehearsed pitch.",
    "Introduce your prompt library and the brief → ideate → create → refine → present workflow to your team so the practice sticks.",
    "Review each lab's detailed steps in this guide and re-create the campaign in your own AI tools.",
]
LG_GLOSSARY = [
    ("Generative AI assistant", "A general-purpose chat tool (ChatGPT, Claude, Gemini, Microsoft Copilot) that generates text, ideas and analysis from a prompt."),
    ("AI image tool", "A tool that generates images from a text prompt — DALL·E in ChatGPT, Midjourney, Adobe Firefly, Gemini, Microsoft Copilot / Designer or Canva."),
    ("ChatGPT / Claude / Gemini / Copilot", "The widely-used chat assistants used in this course to ideate, write, rewrite and refine creative content."),
    ("Prompt", "The instruction you give the AI; a structured prompt with role, context, task, format and constraints produces a far better result than a vague one."),
    ("Prompt library", "A saved, reusable set of prompt templates for the recurring creative tasks — ideation, copywriting, image prompts, adaptation, social captions."),
    ("Generate–review–refine loop", "The core creative AI workflow — prompt, review the options critically, then refine with follow-up prompts and your own edits until it is right."),
    ("Creative brief", "A short statement of the brand, the audience, the goal and the constraints that every creative decision and AI output is judged against."),
    ("Tone", "The mood or attitude of the writing — for example warm, playful, luxurious or calm — chosen to suit the audience and brand."),
    ("Style", "The craft of the writing — sentence length, rhythm, vocabulary and formatting — that gives the work a consistent feel."),
    ("Voice", "The consistent personality of a brand or creator that makes its content recognisably its own, across every piece."),
    ("Brand voice guide", "A short reference — voice attributes, sample on-voice and off-voice lines, and vocabulary — that keeps every AI output sounding like the brand."),
    ("Marketing copy", "Persuasive written content — taglines, product descriptions, captions, scripts — created to inform, engage and move an audience to act."),
    ("Tagline", "A short, memorable line that captures the essence or promise of a brand, product or campaign."),
    ("Adaptation", "Reworking one core message into different versions for different audiences and channels while keeping the message consistent."),
    ("Follow-up prompt", "A short instruction that refines the previous AI output ('make it warmer', 'half the length', 'three bolder options') instead of starting over."),
    ("Image prompt", "A text description for an AI image tool that names the subject, style, composition, lighting, colour palette, mood and aspect ratio."),
    ("Moodboard", "A set of reference visuals that establish the look and feel — colour, style, mood — of a creative project before the final visuals are made."),
    ("Aspect ratio", "The width-to-height shape of an image (for example 1:1 for a square post, 9:16 for a story, 16:9 for a slide)."),
    ("Social content kit", "A set of platform-ready post concepts and captions for a campaign, made to share one voice, look and message."),
    ("Brainstorming", "Generating many ideas quickly without judging them, to start from abundance rather than a blank page."),
    ("Divergent / convergent thinking", "Divergent thinking generates many options widely; convergent thinking clusters, compares and narrows them to the best."),
    ("Mind map", "A diagram with a central theme and branching sub-ideas, used to organise and see the structure of a flood of ideas."),
    ("SCAMPER", "An ideation technique — Substitute, Combine, Adapt, Modify, Put to another use, Eliminate, Reverse — used to push an idea in new directions."),
    ("Lateral / provocation techniques", "Prompting moves — opposites, random stimulus, analogies, role-play, reversing the brief — that push past the first, safe idea into fresher territory."),
    ("Creative block", "Being stuck or unable to start; AI helps by offering a starting point, alternative directions or a constraint to react against."),
    ("Creative workflow", "A repeatable chain of tools and steps — brief → ideate → draft → visualise → assemble → refine — that produces a coherent creative result."),
    ("Pitch", "Presenting a creative idea persuasively so an audience or client understands and buys it."),
    ("Originality", "The quality of being genuinely fresh and your own; AI output is raw material you transform and direct, not a finished original in itself."),
    ("Copyright", "The legal right protecting original creative work; you avoid copying protected work or imitating a real brand's or living artist's protected style."),
    ("AI-image rights", "The terms and usage rights that apply to images an AI tool generates — check each tool's rules before using an image commercially."),
    ("Human-in-the-loop", "Keeping a person responsible for reviewing, curating, correcting and approving every AI output before it is used."),
    ("Hallucination", "A confident but false or invented statement, fact or detail from an AI, which is why every output must be reviewed and checked."),
    ("Responsible AI use", "Using AI safely and ethically — protecting confidential material, respecting others' rights, keeping the work original, and being transparent about AI assistance."),
]

# ------------------------------------------------------------------ version history
VERSION_HISTORY = [
    ("1.0", VERSION_DATE, "Initial release — C1276 Generative AI for Creativity courseware.", TRAINER),
]
