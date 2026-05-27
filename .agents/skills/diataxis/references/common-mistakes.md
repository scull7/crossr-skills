# Common Diátaxis Mistakes

Most poor documentation does not suffer from lack of effort — it suffers from **mixing the four quadrants**.

Here are the most frequent and damaging mistakes, with how to recognize and fix them.

## 1. The "Tutorial That Isn't"

**Symptoms**:
- Long conceptual explanations at the beginning
- "First, you should understand how X works..."
- Assumes the reader already knows a lot of terminology
- Skips steps because "it's obvious"

**Why it fails**: The reader wanted to *learn by doing*. Instead they got a lecture.

**Fix**: Remove almost all explanation. Focus on the smallest possible sequence of actions that leads to a visible success. Save understanding for a separate Explanation document.

## 2. The "How-to Guide That Teaches"

**Symptoms**:
- Long "Background" or "Concepts" sections before the steps
- Explaining *why* each step works instead of just giving the step
- Turning into a tutorial halfway through

**Why it fails**: The reader has a job to do. They don't want a lesson right now.

**Fix**: Move conceptual material to an Explanation. Keep the how-to ruthlessly focused on "do this, then this."

## 3. Reference That Tries to Explain

**Symptoms**:
- Long paragraphs explaining the history or philosophy of a feature
- "It is important to understand that..."
- Mixing usage examples with deep conceptual discussion

**Why it fails**: Reference should be scannable and factual. Explanatory text destroys its utility.

**Fix**: Keep reference entries short and structured. Move all "why" content to Explanation documents.

## 4. Explanation That Gives Instructions

**Symptoms**:
- "You should always..."
- "First, do X. Then do Y."
- Turning into a how-to guide

**Why it fails**: Explanation is meant to build mental models, not to tell people what to do.

**Fix**: Remove all imperative language. Focus on describing relationships, trade-offs, and underlying ideas.

## 5. Mixing Quadrants in One Document

**Symptoms**:
- A single page that starts as a tutorial, becomes a how-to, then turns into reference, and ends with philosophy.

**Why it fails**: Different parts of the document serve different users at different moments. The reader gets lost.

**Fix**: Split the content. One document = one primary quadrant. Use clear headings and links to the other quadrants when needed.

## 6. Using the Wrong Quadrant for the Audience

**Common example**: Writing reference material for complete beginners, or writing tutorials for experienced users who just need to look something up.

**Diagnostic question**: "What does this person already know, and what do they need *right now*?"

## 7. "Everything Is a Tutorial"

Some teams default to writing everything as tutorials because they feel more friendly. This leads to:
- Extremely long onboarding docs
- Information that is hard to find later
- Maintenance burden (tutorials go stale faster than reference)

**Better approach**: Use tutorials only for initial learning. Everything else should live in the appropriate other quadrant.

## 8. "Everything Is Reference"

The opposite problem — teams that only write dry reference material because it's faster to produce. This leads to:
- High cognitive load for newcomers
- People who don't understand the system even after using it for months

## Diagnostic Checklist

When reviewing documentation, ask:

- Is the tone and structure appropriate for the claimed purpose?
- Does the document try to do more than one job?
- Would a reader in a hurry be helped or hindered by this content?
- Would a complete newcomer be helped or hindered?

If the answers reveal mixing of quadrants, split or rewrite the material.