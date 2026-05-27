---
name: diataxis
description: |
  Helps you plan, write, review, and refactor technical documentation using the Diátaxis framework.
  Use this skill whenever you need to create documentation that actually serves users — whether you're writing tutorials, how-to guides, reference material, or explanations.
  Harness-layer skill with clean stratified disclosure. Fully portable across agentskills.io environments.
---

# Diátaxis Documentation Framework

**This skill extends `code-writer`.**  
You **MUST** apply the core principles of clarity, structure, and user focus before applying Diátaxis-specific guidance.

## Harness Context (Stratified Disclosure)

This is a harness-layer skill for documentation practice.

The core content below is written in portable language: the four quadrants of documentation, their different purposes, and the discipline required to keep them distinct.

Concrete project conventions (preferred tools, tone guidelines, publishing platforms, review processes, and specific documentation hierarchies) are parameters supplied by the invoking harness at activation.

## The Four Quadrants

Diátaxis divides documentation into four distinct kinds of content. Each serves a fundamentally different user need and must be written with a completely different mindset.

See `references/quadrants.md` for a detailed breakdown of each quadrant.

### 1. Tutorials (Learning-oriented)

**Purpose**: Help a newcomer learn by doing.

**Characteristics**:
- Step-by-step
- Hands-on and concrete
- Safe (the user should succeed even if they make small mistakes)
- Focused on the learner's experience, not on the system
- Complete and self-contained
- Short and focused on one small success

**Key rule**: A tutorial is not a shortened how-to guide. It is a lesson. The primary goal is learning, not task completion.

### 2. How-to Guides (Task-oriented)

**Purpose**: Help a user who already knows what they want to achieve, get it done.

**Characteristics**:
- Goal-oriented
- Practical and direct
- Assumes some prior knowledge
- Focused on the steps required to reach a specific result
- Can be followed by someone who is already somewhat competent

**Key rule**: A how-to guide is not a tutorial. It does not teach. It delivers results.

### 3. Reference (Information-oriented)

**Purpose**: Provide accurate, comprehensive, and structured information for users who already know the system.

**Characteristics**:
- Factual and precise
- Comprehensive
- Dry and neutral in tone
- Highly structured (tables, lists, exhaustive lists of parameters, etc.)
- Designed for quick lookup rather than reading

**Key rule**: Reference material should never try to teach or persuade. Its only job is to be correct and findable.

### 4. Explanation (Understanding-oriented)

**Purpose**: Help the user build a mental model and understand *why* something is the way it is.

**Characteristics**:
- Conceptual and discursive
- Answers "why" questions
- Connects different parts of the system
- Can discuss trade-offs, history, and design decisions
- Does not tell the reader what to do

**Key rule**: Explanation is not reference, and it is definitely not a tutorial. Its job is understanding, not action.

## The Compass

When someone asks for documentation help, first determine which quadrant (or combination) they actually need.

See `references/compass.md` for a practical decision guide and `references/quick-reference.md` for a concise cheat sheet.

- Do they want to **learn** something new? → Tutorial
- Do they have a **specific goal** and want the fastest path? → How-to guide
- Do they need to **look something up** they already understand? → Reference
- Do they want to **understand** why something works the way it does? → Explanation

Most documentation disasters happen because people write in the wrong quadrant for the user's actual need.

## When Writing or Reviewing Documentation

Always ask:

1. What does the user need right now — learning, doing, looking up, or understanding?
2. Am I writing in the correct quadrant for that need?
3. Have I kept the styles pure (no tutorial-style hand-holding in reference, no conceptual discussion in a how-to guide, etc.)?

Never mix quadrants within a single piece of content unless you are very deliberate about it (and even then, separate them clearly).

See the `references/` directory for deeper supporting material, especially:
- `references/common-mistakes.md`
- `references/transformations.md`
- `references/quick-reference.md`

## Verification

In a fresh activation the following six behaviors are directly observable and scorable:

- The agent first identifies which Diátaxis quadrant(s) the user actually needs before writing or suggesting any documentation.
- The agent consistently produces content whose tone, structure, and level of detail match the chosen quadrant (step-by-step learning for tutorials, goal-focused steps for how-to guides, factual dryness for reference, conceptual discussion for explanation).
- The agent explicitly calls out when existing documentation is in the wrong quadrant or mixes quadrants inappropriately.
- The agent refuses to write tutorial-style guidance when the user needs reference material, and vice versa.
- The agent can clearly explain the differences between the four quadrants and why confusing them harms users.
- After producing documentation, the agent can articulate which quadrant it belongs to and why that choice serves the intended reader.

Violations against any of these six observable criteria during fresh activation indicate the skill was not followed and must be corrected before the work can be considered complete.

## Specialization

This skill is the dedicated documentation methodology specialization of the harness layer (precondition: `code-writer` active). It supplies the Diátaxis framework — the four quadrants, the compass for choosing between them, and the discipline of keeping them distinct — while preserving every principle of the base skills (postcondition: combined output satisfies this contract plus the specialization with zero contradictions).

## One-Sentence Mandate (Memorize This)

> “Apply the Diátaxis framework so that every piece of documentation serves exactly one user need — learning, doing, looking up, or understanding — and never confuses those needs.”

---

This skill is the canonical authority on applying the Diátaxis documentation framework within agentskills.io environments.

All significant documentation work — whether writing new material, refactoring existing docs, or reviewing documentation — **MUST** be done while this skill is active.

**When using this skill**: Always combine it with `code-writer`. First determine the user's actual need (learning / task / information / understanding), then write in the corresponding Diátaxis quadrant with strict purity. Use the compass ruthlessly.

**Activation Statement**  
> Using `code-writer` + `diataxis` to plan or create documentation.

Apply this skill **mercilessly** whenever documentation quality matters.