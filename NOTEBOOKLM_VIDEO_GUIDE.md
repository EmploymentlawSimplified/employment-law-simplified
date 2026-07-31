# NotebookLM Cinematic Video Overview — One Video a Day Guide

**Goal:** turn the site's content into a daily series of narrated, animated explainer videos using Google's NotebookLM — one topic per day, 23 topics in total, covering the full 13-stage tribunal journey, the 3 strategy articles, all 5 templates, a recap, and the flagship guide.

I can't drive NotebookLM directly — there's no API/connector for it, and Cinematic Video Overviews only generate from inside Google's own interface. This is the exact sequence to do it yourself, repeated once a day.

## The source files

All 23 scripts live in `video/stage-sources/`, named `stage-01-source.md` through `stage-23-source.md`. Each one is:
- Written as clean narrative prose (not tables or fillable fields), which is what NotebookLM's video generator narrates best
- Already fact-checked against the site's own verified content — no new claims, just reformatted for narration
- Followed by its own **suggested NotebookLM focus prompt**, tailored to that specific topic's tone and content priorities

`video/progress.json` tracks which stage was most recently delivered, so a daily reminder always points you to the next one in order:

1–13: the tribunal journey stage by stage (matching the site's own 13-stage hub)
14–16: the three strategy articles (signs of a case being built against you, litigation tactics, and the "won't play fair" readiness briefing)
17–21: the five templates (Grievance Letter, SAR, ET1, Schedule of Loss, Witness Statement)
22: a recap video covering all 13 stages at once
23: a closing promotional overview of the flagship Complete Process & Time Limits Guide

## Before you start

- [ ] You'll need a **Google AI Pro or Google AI Ultra** subscription — Cinematic Video Overviews aren't available on the free NotebookLM tier.

## Each day

1. Open `video/progress.json`, check `last_delivered_stage`, and open the next file: `video/stage-sources/stage-NN-source.md`.
2. Go to **notebooklm.google.com** and sign in with the Google account on your AI Pro/Ultra subscription.
3. Click **New notebook** (or reuse one notebook and just swap the source each day — either works).
4. Click **Add source**, and upload or paste in that day's `stage-NN-source.md` content.
5. Once the source is added, find the **Studio** panel (usually on the right) and select **Video Overview**.
6. Choose **Cinematic** as the video type (as opposed to the shorter vertical "Short Video Overview" format).
7. When prompted for a **focus / customization prompt**, copy in the "Suggested NotebookLM focus prompt" line from the bottom of that day's source file — each one is tailored to its topic's tone and priorities.
8. Generate the video. Cinematic Video Overviews take longer to render than the short format — expect several minutes, not seconds.
9. Preview it fully before exporting. Check specifically for:
   - Any date, deadline, or figure stated on screen — verify it matches the source exactly (the 1 October 2026 time-limit change, the 42-day appeal window, Vento bands, the one-month SAR deadline, etc.). AI narration can occasionally paraphrase numbers inaccurately.
   - That it doesn't present anything as legal advice — if it ever sounds like a legal opinion rather than general information, regenerate with the prompt's tone note emphasized more strongly.
10. Export/download the video file, and update `last_delivered_stage` in `progress.json` to today's stage number.

## Once you have each video file

Send it back (or drop it in `video/`) and I can:
- Embed it on the matching page (the relevant article, template card, or the stages hub for the recap/overview videos)
- Add proper `VideoObject` structured data for SEO
- Write a matching short/teaser description for social sharing

## If a result isn't right

Cinematic Video Overviews are still a newer, less predictable feature than NotebookLM's older audio overviews. If the tone, pacing, or accuracy isn't good enough on the first attempt:
- Regenerate with a shorter, more concrete version of that day's focus prompt
- Try feeding in *only* that day's source file, with nothing else added — extra sources sometimes dilute the focus
- If it still doesn't land, the Short Video Overview format (60-second vertical) is a lower-risk starting point for that topic — faster to generate and easier to sanity-check before trying Cinematic again
