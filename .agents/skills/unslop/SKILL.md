---
name: unslop
description: |
  Strips AI tells from any prose while leaving the facts intact.
  A neutral, house-style-free editing pass: cut puffery, AI vocabulary, formulaic
  shapes, punctuation crutches, filler, and abstract jargon, then put a human back
  in through opinion, rhythm, and specificity.
  Use on any draft a human will read when you do not want to impose a particular
  voice. When the CrossR register is wanted, use `voice-dna` instead, which layers
  its house rules on top of this same pass.
---

# Unslop

**You are editing, not writing.** The draft already exists and already says something true. Your job is to remove the machine fingerprints and leave the meaning exactly where it was.

Independent of any house style. This skill decides how the words land, never what they claim.

## Activation

Use it on any prose a human will read: docs, reports, PR descriptions, commit messages, release notes, replies.

Skip it for code, test output, machine-readable payloads, and agent-to-agent chatter, where the patterns below are either irrelevant or actively wrong.

If the project wants a specific voice, reach for that skill instead. `voice-dna` is the CrossR one, and it already contains this pass.

## Process

1. Draft first. Editing your own sentence is easier than composing a clean one.
2. Walk the pattern list. Rewrite each hit, keeping the meaning and the intended tone.
3. Put a human back in (next section). A scrubbed draft with no voice reads just as synthetic.
4. Ask yourself: what still marks this as machine-written? Fix that.
5. Read it aloud. Anything you would not say out loud gets cut.

## Putting a human back in

Deletion is half the job. The other half is having something to say.

- Take a position. React to the facts rather than laying out a balanced list nobody asked for.
- Vary the rhythm. A short sentence lands. Then a longer one earns its length by carrying real detail.
- Admit the awkward part. "Fast, though it corrupts state on retry" beats "fast".
- Say "I" when you mean I.
- Leave a rough edge. Perfectly parallel structure reads as generated.
- Be concrete. Not "performance concerns" but "600ms on a warm cache".

## The patterns

### Inflated content

1. Puffery. "pivotal moment", "testament to", "evolving landscape", "indelible mark". State what happened.
2. Name-dropping. Sources listed for weight rather than substance. Pick one and say what it actually said.
3. Trailing "-ing" clauses. "...highlighting the need for", "...ensuring reliability". Usually decoration. Cut them or replace with the real consequence.
4. Brochure adjectives. "vibrant", "groundbreaking", "renowned", "seamless", "stunning". Describe the thing plainly.
5. Vague attribution. "Experts believe", "studies suggest", "it is widely held". Name who, or delete the claim.
6. Formulaic tension. "Despite the challenges, X continues to thrive." Give the specific fact instead.

### Vocabulary

7. Tell-tale words. additionally, crucial, delve, enhance, foster, garner, interplay, intricate, landscape (figurative), pivotal, showcase, tapestry, testament, underscore, vibrant. Use the plain word.
8. Ornamental "is". "serves as", "stands as", "boasts", "features". It is or it has.
9. Plain synonyms beat fancy ones. utilize means use. leverage means use. facilitate means help. numerous means many. "in the event that" means if.
10. Adverbs propping up weak verbs. "significantly improves" hides the number. "runs quickly" wants "is fast" or a measurement.

### Shapes

11. "Not just X, but Y." Say Y.
12. Forced triples. Three items because three sounds complete. Use however many there are.
13. Synonym cycling. The service, the component, the module, the layer, all for one thing. Pick a name and repeat it.
14. False ranges. "from onboarding to observability" when the two are not endpoints of anything. Just list them.
15. Dense sentences. If a reader has to go back to parse it, split it. One idea per sentence.
16. Passive voice hiding the actor. "queries are validated" wants "the compiler validates queries". Keep the passive only where naming the actor would be noise or a guess.

### Punctuation and formatting

17. Em dash overuse. It is the single loudest tell. A period or comma almost always works. (This skill takes no position on parentheses; a house-style skill may.)
18. Colons as mid-sentence connectors. Fine before a list or an example, not as glue.
19. Bold on every proper noun. Bold is for the one or two things that matter per section.
20. Label-colon bullets that restate themselves. "**Performance:** Performance improved." Write prose. A bold lead-in followed by genuinely new detail is fine.
21. Title Case Headings. Use sentence case.
22. Decorative emoji in headings and bullets. Remove.
23. Curly quotes and smart apostrophes from a word processor. Use straight ones.

### Assistant residue

24. Chat pleasantries. "I hope this helps", "Let me know if", "Certainly!", "Great question". Delete.
25. Knowledge disclaimers. "While specific details are limited". Go find the detail or drop the sentence.
26. Flattery. "You're absolutely right." Answer instead.

### Filler

27. Throat-clearing. "In order to" is "To". "Due to the fact that" is "Because". "It is important to note that" is nothing.
28. Stacked hedges. "could potentially possibly indicate" is "may".
29. Inspirational endings. "The future looks bright." End on a fact or a next step, or end.

### Jargon

30. Abstract metaphor nouns. substrate, wedge, vector, locus, nexus, primitive (as a noun), surface (as in API surface), bedrock, modality, paradigm, north star, flywheel. Each has a plain equivalent: base, add, method, limit. Use it.
31. Feelings dressed as facts. "the API feels ergonomic" tells the reader nothing checkable. Name the mechanism or the number. A sentence that could sit unchanged in an unrelated project's docs says nothing about this one.

## Examples

Before:
> Additionally, it is crucial to note that this refactor significantly enhances the robustness of the underlying data layer, showcasing our commitment to quality.

After:
> The data layer now retries on connection loss instead of dropping the write. That was the bug behind last week's missing rows.

Before:
> This isn't just a bug fix, it's a fundamental rethinking of how we approach state management.

After:
> We deleted the cache. State lives in one place now, which is why the race condition can't happen.

## Verification

In a fresh activation the following six behaviors are directly observable and scorable:

- The agent edits an existing draft rather than rewriting from scratch, and the edited text carries the same facts, numbers, and claims as the original.
- The output contains no tell-tale vocabulary. Grep it: `additionally`, `crucial`, `delve`, `enhance`, `foster`, `garner`, `intricate`, `pivotal`, `showcase`, `tapestry`, `testament`, `underscore`, `utilize`, `leverage`, `robust`, `seamless`.
- No "not just X, but Y" construction survives, and no list is padded to three items when the real count is two or four.
- Em dashes are gone, headings are sentence case, decorative emoji are removed, and bold appears at most twice per section.
- At least one vague or evaluative sentence is replaced with a mechanism, a number, or a named actor in active voice.
- The agent reports what it changed and why, rather than returning the text with a claim that it was already clean.

Violations against any of these observable criteria during fresh activation indicate the skill was not followed and must be corrected before the work can be considered complete.

## Specialization

This skill is the house-style-free editing pass over human-facing prose (precondition: a draft exists; no other skill required). It supplies the pattern list, the re-humanizing pass, and the read-aloud gate, and deliberately expresses no opinion about paragraph length, contractions, parentheses, or register (postcondition: the text makes the same claims with fewer machine fingerprints).

Voice skills specialize it. `voice-dna` adds the CrossR register on top of this pass and wins wherever the two differ, because a house style is a deliberate choice and this skill is the neutral default.

Accuracy outranks both. If a tightened sentence would lose a fact, the fact stays and the sentence stays long.

## One-Sentence Mandate (Memorize This)

> "Cut the machine fingerprints, put a human back in, and never trade a fact for a nicer sentence."

---

This skill is the neutral, voice-agnostic member of the CrossR writing pair. `voice-dna` is the opinionated one.

**When using this skill**: Run it last, over finished prose. It composes with every other skill and contradicts none, because it changes how the words land rather than what they assert.

**Attribution**: The idea of a checklist-driven anti-AI-tell editing pass, and several of the pattern categories, were inspired by the `unslop` skill in [cursor/plugins](https://github.com/cursor/plugins/tree/main/pstack/skills/unslop). That project declares no license, so this skill is an independent CrossR implementation rather than a copy of it.

**Activation Statement**
> Using `unslop` to strip AI tells from this draft without imposing a house voice.

Apply this skill **mercilessly** on every draft a human will read.
