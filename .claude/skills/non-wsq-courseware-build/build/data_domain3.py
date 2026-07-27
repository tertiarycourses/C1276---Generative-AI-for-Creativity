"""
Domain 3 — AI-Assisted Ideation and Creative Workflows. Labs 9-11.

The connected Island Botanica campaign is completed and elevated here. Lab 9
brainstorms a wide set of bigger campaign ideas and organises them into a mind
map; Lab 10 challenges the obvious and breaks creative blocks to strengthen the
lead concept; Lab 11 combines every tool used across the day into a repeatable
creative workflow and builds and rehearses the creative pitch. This is where the
campaign pack becomes a presented, pitch-ready whole.
"""

PROJECT_NOTE = (
 "BUILDING BLOCK — what you create in this lab becomes part of your Island Botanica campaign pack, "
 "the connected campaign you assemble across all 11 labs."
)

DOMAIN3 = [
 dict(
 num=9, topic=3,
 title="Brainstorm Big Campaign Ideas and Build a Mind Map",
 objective="Use AI to brainstorm a wide set of bigger Island Botanica campaign concepts and activation ideas, organise them into a mind map, then cluster and shortlist the strongest direction.",
 desc="With the copy and visuals made, you now lift your sights from individual posts to the campaign's big "
 "idea. In this lab you use AI to diverge — to generate a large, varied set of launch campaign concepts and "
 "activation ideas (themes, hooks, events, collaborations, content series, in-store moments) — starting from "
 "abundance rather than a single safe idea. You then use AI to organise the flood into a mind map: a central "
 "theme with branches and sub-branches, so clusters, patterns and gaps become visible. Finally you converge: "
 "you cluster the ideas, weigh them against the brief, audience and budget realism, and shortlist one lead "
 "campaign concept plus a backup. This is divergent-then-convergent thinking with AI as the engine and you as "
 "the judge. " + PROJECT_NOTE,
 build="A wide brainstormed list of Island Botanica campaign concepts and activation ideas, organised into a mind map (central theme, branches, sub-branches), then clustered and narrowed to one shortlisted lead concept and a backup, saved in your project folder.",
 services="ChatGPT / Claude / Gemini / Copilot, divergent brainstorming, mind mapping with AI, clustering and shortlisting, convergent selection",
 steps=[
 ("Diverge first — generate widely without judging. Paste the prompt below.",
  "You are a campaign ideas generator. For the Island Botanica candle collection launch (year-end gifting and Lunar New Year, premium gift-shoppers and wellness-seekers), brainstorm 25 varied campaign concepts and activation ideas — themes, hooks, content series, events, collaborations, in-store or online moments. Be bold and varied; do not filter yet. One line each."),
 ("Push for range so you are not stuck near the obvious. Paste the prompt below.",
  "Give me ten more ideas that are deliberately different from the first list — more unexpected, more playful, or more experiential — for the same Island Botanica launch."),
 ("Organise the flood into a mind map. Paste the prompt below.",
  "Organise all these Island Botanica campaign ideas into a mind map in indented text (or Markdown) form: a central theme in the middle, then branches for the main directions (for example Story & Theme, Content, Events & Activations, Partnerships, In-store, Gifting), and the specific ideas as sub-branches under each. Add a branch for any gap you notice."),
 ("Render the mind map visually if you like: paste the indented text into a mind-mapping tool, or ask an AI image/diagram tool to draw it, so you can see the structure at a glance. Keep the text version too.", ""),
 ("Converge — cluster and evaluate. Paste the prompt below.",
  "From this mind map, cluster the ideas into three or four campaign directions. For each direction, give it a name, describe it in two lines, and note its main strength and its main risk for a small brand with a modest budget."),
 ("Make the call: shortlist one lead campaign concept and one backup. Write one line on why the lead fits the Island Botanica brief, audience and season best — this is your judgement, not the AI's.", ""),
 ("Save the full idea list, the mind map (text and any visual), the clustered directions, and your shortlisted lead concept and backup in your project folder — the lead concept goes into Lab 10 to be challenged and strengthened.", ""),
 ],
 test="You have a wide brainstormed idea list (35+ ideas) for the Island Botanica launch, a mind map organising them into a central theme with branches and sub-branches, the ideas clustered into three or four evaluated directions, and one shortlisted lead concept plus a backup with a one-line rationale — all saved in your project folder.",
 ),
 dict(
 num=10, topic=3,
 title="Break Creative Blocks and Challenge the Obvious",
 objective="Use AI prompting techniques — provocations, opposites, analogies, SCAMPER and role-play — to challenge conventional thinking, push past creative blocks, and strengthen your lead campaign concept into something fresher.",
 desc="A shortlisted idea is a starting point, not the finish. In this lab you deliberately push your lead "
 "concept past the obvious using AI as a provocation engine. You ask for the opposite of your safe idea, "
 "unexpected analogies, and 'what would a completely different brand do', and you run structured techniques — "
 "SCAMPER (substitute, combine, adapt, modify, put to another use, eliminate, reverse), random-stimulus, and "
 "role-play (pitch it as a filmmaker, a poet, a rival brand) — to surface fresher angles. You also practise "
 "the unblock move for when you are stuck: ask AI for three directions, a starting sentence, or a constraint "
 "to react against. Then you converge again — you take the best of what the challenge surfaced and fold it "
 "into a strengthened, more original version of your lead concept. " + PROJECT_NOTE,
 build="A set of challenged and alternative directions for your lead Island Botanica concept — from opposites, analogies, SCAMPER and role-play prompts — and one strengthened, more original version of the lead concept that incorporates the best of them, saved in your project folder.",
 services="ChatGPT / Claude / Gemini / Copilot, challenging conventional thinking, provocation and lateral techniques (SCAMPER, random stimulus, analogy, role-play), overcoming creative blocks",
 steps=[
 ("State your lead concept from Lab 9 in one line so the AI has something concrete to challenge.", ""),
 ("Challenge the obvious with opposites and analogies. Paste the prompt below.",
  "Here is my lead campaign concept for Island Botanica: '[PASTE LEAD CONCEPT]'. Challenge it: (1) describe the opposite approach; (2) give three unexpected analogies from unrelated fields (nature, music, architecture); (3) tell me how a completely different kind of brand — a streetwear label, a luxury hotel, a museum — would run this launch. Mine each for one fresh angle."),
 ("Run SCAMPER on the concept. Paste the prompt below.",
  "Apply SCAMPER to my Island Botanica lead concept — Substitute, Combine, Adapt, Modify, Put to another use, Eliminate, Reverse. For each, give one concrete way it could change the campaign. Keep the genuinely interesting ones."),
 ("Practise the unblock move (use whenever you stall). Paste the prompt below.",
  "I'm stuck on the launch's hero moment. Give me three completely different directions in one line each, a single opening sentence I could build from, and one creative constraint to react against."),
 ("Role-play for a fresher voice. Paste the prompt below.",
  "Re-pitch my Island Botanica lead concept three ways: as a filmmaker would frame it, as a poet would express it, and as a bold rival brand would provoke with it. One short paragraph each."),
 ("Converge again — curate, don't hoard. Choose the two or three strongest angles the challenge surfaced, discard the rest, and rewrite your lead concept as one strengthened, more original version that keeps the brief but is no longer the obvious idea.", ""),
 ("Save the challenge outputs and your strengthened lead concept in your project folder — this is the concept you present in Lab 11.", ""),
 ],
 test="You have challenged your lead concept with opposites, analogies, SCAMPER and role-play prompts, practised the unblock move, and produced one strengthened, more original version of the Island Botanica lead concept that folds in the two or three best angles surfaced — all saved in your project folder.",
 ),
 dict(
 num=11, topic=3,
 title="Combine Your Tools into a Creative Workflow and Pitch the Campaign",
 objective="Assemble every tool used across the day into one repeatable creative workflow, then use AI to build and rehearse a creative pitch that presents the complete Island Botanica campaign.",
 desc="The final lab turns the day's pieces into a repeatable method and a presented result. First you "
 "document the creative workflow you actually used — chat assistant to ideate and write, image tool to "
 "visualise, design tool to assemble, chat assistant again to adapt and pitch — as a reusable chain (brief -> "
 "ideate -> draft -> visualise -> assemble -> refine -> present) you can run for any future project. Then you "
 "use AI to build the creative pitch: a short narrative that presents the strengthened concept, the brand "
 "story and copy, the visuals and the social kit, framed persuasively for the client. You have AI anticipate "
 "the client's likely questions and draft crisp answers, and you rehearse — asking AI to critique your pitch "
 "for clarity and impact. By the end you have both a workflow you keep and a rehearsed pitch that presents the "
 "whole Island Botanica campaign. " + PROJECT_NOTE,
 build="A documented, repeatable multi-tool creative workflow, plus a creative pitch for the Island Botanica campaign — a short persuasive narrative, a Q&A crib of likely client questions and answers, and a rehearsal critique — assembling the whole campaign pack, saved in your project folder.",
 services="ChatGPT / Claude / Gemini / Copilot, combining multiple AI tools into a workflow, pitch structuring and storytelling, anticipating client questions, rehearsing with AI",
 steps=[
 ("Document the workflow you used. Paste the prompt below, then adjust it to what you actually did.",
  "Help me write a reusable creative workflow for AI-assisted campaigns, based on this sequence: define the brief and brand voice, ideate and mind-map, draft copy, generate images, assemble social and launch content, refine, and pitch. For each step, name the tool I'd use, the input and the output, so I can run this workflow for any future project. Present it as a numbered workflow."),
 ("Gather the campaign pack: your brand story and copy (Labs 5-6), visuals and social kit (Labs 7-8), and the strengthened concept (Lab 10). List what you will show in the pitch and in what order.", ""),
 ("Build the pitch narrative. Paste the prompt below.",
  "You are a creative director presenting to a client. Using my Island Botanica materials — concept: '[PASTE CONCEPT]', brand story, taglines, key visuals and social plan — write a short, persuasive pitch narrative (about 250 words) that opens with the big idea, walks through the story, the look and the launch plan, and closes with why it will work for the year-end season. On the Lumina Botanicals voice."),
 ("Anticipate the client's questions. Paste the prompt below.",
  "For this Island Botanica pitch, list the eight questions a client is most likely to ask (about budget, originality and AI use, timing, channels, and how it stands out), and draft a crisp two-to-three-sentence answer to each."),
 ("Rehearse with AI as a critic. Paste the prompt below and act on the feedback.",
  "Critique my Island Botanica pitch for clarity, flow and persuasive impact. What is the weakest part, what should I cut, and what one change would make it land better? Be specific and direct."),
 ("Assemble the final campaign pack: put the strengthened concept, brand story and copy, adapted pieces, moodboard and images, social kit and launch visuals, the pitch narrative and Q&A crib, and your workflow document together in one place, in a clear order.", ""),
 ("Save the workflow, the pitch narrative, the Q&A crib and the assembled campaign pack in your project folder — the finished, pitch-ready Island Botanica campaign the course set out to build.", ""),
 ],
 test="You have a documented, reusable multi-tool creative workflow, a persuasive Island Botanica pitch narrative, a Q&A crib of eight likely client questions with answers, a rehearsal critique you have acted on, and the whole campaign pack assembled in order — all saved in your project folder.",
 ),
]
