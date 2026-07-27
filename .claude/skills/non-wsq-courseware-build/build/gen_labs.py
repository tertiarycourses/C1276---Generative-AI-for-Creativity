#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Generate the labs/ markdown from the SAME single source as the deck/LP/LG
(course_data.py + data_domainN.py), so labs stay 100% aligned with the other
artifacts. Emits labs/lab-NN-*.md, labs/README.md and refreshes nothing else
(tools.md and the brief pack are hand-authored). Enrichment sections
(Prerequisites, Troubleshooting, Challenge, Reflection, Deliverable) live in the
ENRICH table below, keyed by lab number.

Run:  python gen_labs.py
"""
import os, re, sys, glob, importlib

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import course_data as C


def find_repo(start):
    env = os.environ.get("COURSE_REPO")
    if env and os.path.isdir(env):
        return env
    d = start
    for _ in range(8):
        d = os.path.dirname(d)
        if os.path.isdir(os.path.join(d, "courseware")) and os.path.isdir(os.path.join(d, "labs")):
            return d
    return os.path.dirname(os.path.dirname(start))


REPO = find_repo(HERE)
LABS = os.path.join(REPO, "labs")

# ------------------------------------------------------------------ load labs
DOMS = []
for f in sorted(glob.glob(os.path.join(HERE, "data_domain[0-9]*.py"))):
    mod = importlib.import_module(os.path.splitext(os.path.basename(f))[0])
    key = [k for k in dir(mod) if k.startswith("DOMAIN")][0]
    DOMS.append((getattr(mod, key), getattr(mod, "SCENARIO", None)))

LABSLIST = []
SCENARIO = None
for dom, scen in DOMS:
    if scen and not SCENARIO:
        SCENARIO = scen
    LABSLIST.extend(dom)

TOPIC_TITLE = {t["num"]: t["title"] for t in C.TOPICS}

# ------------------------------------------------------------------ approx minutes per lab
# Derived from the schedule lab blocks so the labs match the Lesson Plan timing.
def lab_titles(nums):
    return "; ".join("" for _ in nums)


def approx_minutes():
    sched = C.SCHEDULE(lambda nums: "\x00".join(str(n) for n in nums))
    mins = {}
    for _day, (_theme, rows) in sched.items():
        for row in rows:
            if row[3] == "lab":
                nums = [int(x) for x in row[4].split("Hands-on: ")[-1].split("\x00")]
                per = round(row[2] / len(nums))
                for n in nums:
                    mins[n] = per
    return mins


MINS = approx_minutes()

# ------------------------------------------------------------------ per-lab enrichment
ENRICH = {
 1: dict(
    prereqs=[
        "A laptop with a modern web browser (Chrome, Edge, Safari or Firefox) and a reliable internet connection.",
        "An account for at least one chat assistant (ChatGPT, Claude, Gemini or Copilot) and one AI image tool.",
        "The supplied Lumina Botanicals brief to hand (labs/reference-pack/).",
    ],
    trouble=[
        "**A tool won't let you sign in or generate.** Try a different one — you only need one chat assistant and one image tool to follow the labs; tell the trainer what you have.",
        "**The AI image looks strange or has odd details.** That's expected from a one-line prompt — it's only a warm-up; you make real, on-brand images from proper prompts in Lab 7.",
        "**The two assistants give very different answers.** That's normal — they differ in imagination and range; the prompting and review skills you learn work across all of them.",
    ],
    challenge="Ask a third assistant the same naming prompt and rank the three answers — which was most imaginative, and why?",
    lo=1,
    deliverable="Keep your Island-Botanica-Campaign folder with your toolkit notes and the brief — it is the home for everything you build across the next labs.",
 ),
 2: dict(
    prereqs=[
        "Completed Lab 1 (your tools are set up and responding).",
        "The supplied Lumina Botanicals brief open (labs/reference-pack/).",
    ],
    trouble=[
        "**The AI's draft is generic and clichéd.** Add a role and real context (brand, audience, goal); a vague prompt always gives generic copy.",
        "**The AI invents awards or claims.** Tell it explicitly not to invent claims and to stay within the brief — you own every claim you publish.",
        "**The reply is the wrong length or format.** State the format you want (three options, a word limit, a numbered list) as a constraint and regenerate.",
    ],
    challenge="Write a structured prompt for a completely different creative project of your own using the same five parts, proving the template travels beyond Island Botanica.",
    lo=2,
    deliverable="Keep your reusable creative prompt library — you run its templates for ideation, copy, image prompts, adaptation and social in every later lab.",
 ),
 3: dict(
    prereqs=[
        "Completed Lab 2 (you can write structured creative prompts).",
        "The supplied Lumina Botanicals brief with the brand and voice notes to hand.",
    ],
    trouble=[
        "**The voice sounds generic.** Give the AI more specific brand cues (artisanal, botanical, wellness, quietly premium) and reject any attribute that could describe any brand.",
        "**On-voice and off-voice examples look too similar.** Ask the AI to exaggerate the difference, then dial the on-voice version back to where it feels right.",
        "**A rewrite still sounds off.** Tell the AI exactly what is wrong ('too salesy', 'not sensory enough') rather than just 'try again'.",
    ],
    challenge="Take a famous brand you admire, describe its voice in three attributes, and note how Lumina Botanicals' voice should be different.",
    lo=3,
    deliverable="Keep your tone, style and voice guide — every later lab holds its copy to it, so the whole campaign sounds like one brand.",
 ),
 4: dict(
    prereqs=[
        "Completed Lab 3 (you have a defined brand voice).",
        "Access to the AI image tool you plan to use, so you can check its usage rules.",
    ],
    trouble=[
        "**The checklist is vague.** Ask for plain-language, one-line rules with a concrete example of each risk, not abstract principles.",
        "**You're unsure whether an image is safe to use.** Check the tool's own terms on ownership and commercial use; when in doubt, avoid real logos, brand names and living artists' names in prompts.",
        "**Disclosure feels awkward.** Decide a simple rule now (for example a small 'created with AI assistance' note where it matters) so you're consistent all day.",
    ],
    challenge="Find one real news example of AI creative work going wrong (a copyright or disclosure issue) and note the one rule that would have prevented it.",
    lo=4,
    deliverable="Keep your responsible-use checklist and decisions — the ground rules that keep every later deliverable original, honest and safe to publish.",
 ),
 5: dict(
    prereqs=[
        "Completed Lab 4 (your responsible-use rules are set).",
        "Your brand voice guide from Lab 3 to paste into the assistant.",
    ],
    trouble=[
        "**The copy is full of clichés.** Ban the specific clichés in the prompt ('elevate', 'perfect gift') and ask for more sensory, specific lines.",
        "**Every option sounds the same.** Ask for a range — from poetic to plain, from short to longer — so you have real choices to curate.",
        "**The AI drifts off voice.** Paste the voice guide again and ask it to rewrite strictly to those attributes.",
    ],
    challenge="Take your busiest product description and cut it to a single, stronger sentence — often the most memorable version.",
    lo=5,
    deliverable="Keep the brand story, taglines and four product descriptions — the written spine you adapt, illustrate and pitch across the rest of the day.",
 ),
 6: dict(
    prereqs=[
        "Completed Lab 5 (you have hero copy and product descriptions).",
        "Any chat assistant open, with your voice guide to hand.",
    ],
    trouble=[
        "**Adaptations lose the core message.** Remind the AI to keep the message and voice and change only tone, length and framing.",
        "**Follow-ups aren't improving the draft.** Be specific and one-at-a-time ('warmer', then 'half the length') rather than asking for everything at once.",
        "**Pieces contradict each other.** Run the consistency-pass prompt so voice, message and key wording match across every piece.",
    ],
    challenge="Adapt your hero line for a completely different audience (say, corporate gifting for an office) and note how tone and framing shift while the message holds.",
    lo=6,
    deliverable="Keep the adapted, polished pieces by audience and channel — ready to pair with visuals in Labs 7 and 8.",
 ),
 7: dict(
    prereqs=[
        "Completed Lab 6 (you know the message each visual must support).",
        "An AI image tool (DALL·E in ChatGPT, Gemini, Copilot / Designer, Firefly or Canva).",
    ],
    trouble=[
        "**The image is off-brand.** Add style, mood and palette words from your moodboard to the prompt and regenerate; keep every image in the same style.",
        "**The image has garbled text or a fake logo.** Prompt 'no text, no logos' and regenerate; AI image text is unreliable — add real text on the slide instead.",
        "**You can't tell what changed the result.** Iterate one element at a time (only lighting, or only palette) so you learn what each word does.",
    ],
    challenge="Generate the same hero shot in a completely different style (say, flat illustration instead of photography) and decide which better fits Island Botanica.",
    lo=7,
    deliverable="Keep the moodboard and on-brand hero and lifestyle images (with their prompts) — the visual direction and key visuals for Lab 8.",
 ),
 8: dict(
    prereqs=[
        "Completed Lab 7 (you have on-brand images).",
        "An AI-enabled design tool (Canva, Copilot Designer or your image tool) for the launch visual.",
    ],
    trouble=[
        "**Captions feel inconsistent.** Run them all past the voice guide in one prompt and align tone and key wording.",
        "**The launch visual is cluttered.** Cut the text to a tagline plus one line; let the image carry the mood.",
        "**Text on the visual is hard to read.** Increase contrast, give the text room, and keep it short — legibility beats decoration.",
    ],
    challenge="Design a second version of your launch visual with a different layout or crop, and compare which stops the scroll better.",
    lo=8,
    deliverable="Keep the content calendar, captions, paired images, launch visual and presentation slide — the campaign's social and launch content.",
 ),
 9: dict(
    prereqs=[
        "Completed Lab 8 (the campaign has its copy and visuals).",
        "Any chat assistant open; optionally a mind-mapping or diagram tool.",
    ],
    trouble=[
        "**The ideas are all safe and similar.** Ask explicitly for bolder, more unexpected or more experiential ideas; defer judgement while you diverge.",
        "**The mind map is a flat list.** Ask the AI to group ideas under clear branches and add sub-branches, and to flag any gap.",
        "**You can't choose.** Score the clustered directions against the brief, audience and budget realism — let the criteria, not a hunch alone, guide the shortlist.",
    ],
    challenge="Add one 'impossible budget' idea and one 'zero budget' idea to your map — extremes often reveal a workable middle.",
    lo=9,
    deliverable="Keep the idea list, mind map and shortlisted lead concept and backup — the lead concept goes into Lab 10 to be challenged and strengthened.",
 ),
 10: dict(
    prereqs=[
        "Completed Lab 9 (you have a shortlisted lead concept).",
        "Any chat assistant open.",
    ],
    trouble=[
        "**The challenge outputs feel gimmicky.** Mine each for the one usable insight, and discard the rest — the value is the fresh angle, not the whole provocation.",
        "**You're stuck and nothing feels right.** Use the unblock move: ask for three directions, a starting sentence, and a constraint to react against, then just start.",
        "**The strengthened concept drifted off-brief.** Re-check it against the audience and season; keep the freshness but bring it back to the goal.",
    ],
    challenge="Force-combine two unrelated ideas from your Lab 9 map into one concept — unexpected mash-ups are a reliable source of originality.",
    lo=10,
    deliverable="Keep the challenge outputs and the strengthened, more original lead concept — the concept you present in Lab 11.",
 ),
 11: dict(
    prereqs=[
        "Completed Labs 1-10 (you have the full campaign pack and a strengthened concept).",
        "Somewhere you can rehearse the pitch aloud.",
    ],
    trouble=[
        "**The workflow is just a list of tools.** For each step name the input and the output, so it's a method you can actually re-run, not a toolbox.",
        "**The pitch is a description, not a story.** Open with the big idea and build a narrative; ask the AI to lead with the hook, not the brand history.",
        "**A generic or off-brief line slipped into the pitch.** Hold the whole pitch to the voice guide and the strengthened concept before you finalise.",
    ],
    challenge="Record yourself delivering the pitch once, then ask the AI to critique a transcript of it for clarity and filler words.",
    lo=10,
    deliverable="Keep the reusable workflow and the assembled, rehearsed Island Botanica campaign pack — the finished, pitch-ready campaign the course set out to build.",
 ),
}


def slug(title):
    s = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    if len(s) > 60:
        s = s[:60].rstrip("-")
    return s


def steps_md(steps):
    out = []
    for i, (instr, cmd) in enumerate(steps, 1):
        out.append(f"### Step {i}\n\n{instr}")
        if cmd:
            out.append("Prompt to use (paste into your AI assistant — ChatGPT, Claude, Gemini, Copilot or your image tool):\n\n```text\n" + cmd + "\n```")
    return "\n\n".join(out)


def lab_filename(lab):
    return f"lab-{lab['num']:02d}-{slug(lab['title'])}.md"


def build_lab(lab):
    e = ENRICH[lab["num"]]
    topic = lab["topic"]
    mins = MINS.get(lab["num"], 40)
    parts = []
    parts.append(f"# Lab {lab['num']} — {lab['title']}\n")
    parts.append(
        f"**Topic 0{topic}:** {TOPIC_TITLE[topic]}  |  **Day 1**  |  "
        f"**Approx. {mins} min**  |  **Course:** {C.TITLE}\n"
    )
    if SCENARIO:
        parts.append("## Scenario\n\n" + SCENARIO + "\n")
    parts.append("## Goal\n\n" + lab["objective"] + "\n")
    parts.append("## What you'll build\n\n" + lab["build"] + "\n")
    parts.append("**Tools and techniques:** " + lab["services"] + "\n")
    parts.append("## Prerequisites\n\n" + "\n".join("- " + p for p in e["prereqs"]) + "\n")
    parts.append("## Steps\n\n" + steps_md(lab["steps"]) + "\n")
    parts.append("## Test it\n\n" + lab["test"] + "\n")
    parts.append("## Troubleshooting\n\n" + "\n".join("- " + t for t in e["trouble"]) + "\n")
    parts.append("## Challenge\n\n" + e["challenge"] + "\n")
    lo = C.LEARNING_OUTCOMES[e["lo"] - 1]
    lo_text = lo.split(":", 1)[1].strip().rstrip(".")
    parts.append(f"## Reflection\n\nLO{e['lo']} — In your own words: {lo_text}?\n")
    parts.append("## Deliverable\n\n" + e["deliverable"] + "\n")
    parts.append("---\n")
    parts.append(
        f"*{C.TITLE} · {C.COURSE_CODE} · Version {C.VERSION} · © 2026 {C.ORG}*"
    )
    return "\n".join(parts) + "\n"


def build_readme(files):
    rows = []
    for lab in LABSLIST:
        fn = files[lab["num"]]
        rows.append(
            f"| 1 | 0{lab['topic']} | {lab['num']:02d} | [{lab['title']}]({fn}) |"
        )
    md = []
    md.append(f"# Labs — {C.TITLE}\n")
    md.append(f"**Course Code:** {C.COURSE_CODE}  |  **Version {C.VERSION} · {C.VERSION_DATE}**\n")
    md.append(
        "All 11 labs build one connected **Island Botanica launch campaign**, which you begin in Lab 1 and "
        "finish in Lab 11 — from a blank page, through ChatGPT, Claude, Gemini and Copilot for ideas, voice, "
        "story and copy, into an AI image tool for a moodboard and on-brand visuals, and out as a social and "
        "launch content kit, a strengthened campaign concept and a rehearsed creative pitch. A Lumina "
        "Botanicals brief with the brand facts you need is supplied in `reference-pack/`; use your own "
        "non-confidential creative project wherever you prefer. There is **no assessment** — each lab verifies "
        "itself with a 'Test it' step.\n"
    )
    md.append("| Day | Topic | Lab | Title |")
    md.append("|---:|---|---:|---|")
    md.extend(rows)
    md.append("")
    md.append("## Tools\n")
    md.append("See [tools.md](tools.md) for the accounts and tools used across the labs, and "
              "[reference-pack/](reference-pack/) for the Lumina Botanicals brief.")
    return "\n".join(md) + "\n"


def main():
    os.makedirs(LABS, exist_ok=True)
    # remove stale lab-*.md so renamed labs don't linger
    for old in glob.glob(os.path.join(LABS, "lab-*.md")):
        os.remove(old)
    files = {}
    for lab in LABSLIST:
        fn = lab_filename(lab)
        files[lab["num"]] = fn
        with open(os.path.join(LABS, fn), "w", encoding="utf-8") as fh:
            fh.write(build_lab(lab))
        print("wrote labs/" + fn)
    with open(os.path.join(LABS, "README.md"), "w", encoding="utf-8") as fh:
        fh.write(build_readme(files))
    print("wrote labs/README.md")


if __name__ == "__main__":
    main()
