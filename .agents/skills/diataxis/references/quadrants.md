# The Four Quadrants of Diátaxis

Diátaxis divides technical documentation into four distinct kinds of content. Each serves a fundamentally different user need and requires a completely different mindset when writing.

The four quadrants are arranged along two axes:

- **Practical** vs **Theoretical**
- **Study** (learning) vs **Work** (getting things done)

## 1. Tutorials

**Quadrant**: Practical + Study

**Purpose**: Help a newcomer learn by doing.

**Core characteristics**:
- Step-by-step
- Hands-on and concrete
- Safe (the learner should succeed even with small mistakes)
- Focused on the *learner's experience*, not on the system itself
- Complete and self-contained
- Short and focused on achieving one small, meaningful success

**Tone**: Supportive, encouraging, patient. The writer acts as a guide.

**Key rule**: A tutorial teaches *how to do something specific* while the user learns. It is not a shortened how-to guide.

**Common failure modes**:
- Being too abstract or conceptual
- Skipping steps ("obvious" steps are not obvious to a beginner)
- Mixing in reference-style information

## 2. How-to Guides

**Quadrant**: Practical + Work

**Purpose**: Help someone who already knows roughly what they want to achieve, actually achieve it.

**Core characteristics**:
- Goal-oriented
- Practical and direct
- Assumes the reader has some relevant knowledge
- Focused purely on the steps required to reach a specific result
- Can be followed successfully by someone who is already somewhat competent with the system

**Tone**: Direct, efficient, no-nonsense. "Do this, then this."

**Key rule**: A how-to guide delivers a result. It does not teach concepts or explain why things work.

**Common failure modes**:
- Starting with long explanations
- Including tutorial-style hand-holding
- Turning into reference material

## 3. Reference

**Quadrant**: Theoretical + Work

**Purpose**: Provide accurate, comprehensive, and well-structured information for users who already know the system and need to look something up.

**Core characteristics**:
- Factual and precise
- Comprehensive (aims to cover the topic exhaustively)
- Dry and neutral in tone
- Highly structured (tables, exhaustive lists, parameter descriptions, etc.)
- Designed for quick lookup rather than sequential reading

**Tone**: Neutral, authoritative, concise. No encouragement or conceptual discussion.

**Key rule**: Reference material should never try to teach, persuade, or tell stories. Its only job is to be correct and findable.

**Common failure modes**:
- Adding explanatory text that belongs in Explanation
- Using tutorial language ("First, you should...")
- Being incomplete or inconsistently structured

## 4. Explanation

**Quadrant**: Theoretical + Study

**Purpose**: Help the reader build a mental model and understand *why* the system is the way it is.

**Core characteristics**:
- Conceptual and discursive
- Answers "why" questions
- Connects different parts of the system
- Discusses trade-offs, history, design decisions, and underlying principles
- Does **not** tell the reader what to do

**Tone**: Thoughtful, exploratory, connective.

**Key rule**: Explanation is not a place to give instructions. Its job is understanding.

**Common failure modes**:
- Slipping into tutorial steps
- Turning into reference material
- Being too vague or philosophical without connecting back to the actual system

## Summary Table

| Quadrant     | Orientation     | Primary User Need     | Key Tone          | Must Avoid                     |
|--------------|-----------------|-----------------------|-------------------|--------------------------------|
| Tutorial     | Practical + Study | Learning by doing    | Supportive        | Abstraction, skipping steps    |
| How-to       | Practical + Work  | Achieving a goal     | Direct            | Teaching concepts, fluff       |
| Reference    | Theoretical + Work| Looking things up    | Neutral & factual | Explanations, instructions     |
| Explanation  | Theoretical + Study | Building understanding | Discursive     | Steps, "how to" language       |

Understanding and respecting these distinctions is the foundation of good technical documentation according to Diátaxis.