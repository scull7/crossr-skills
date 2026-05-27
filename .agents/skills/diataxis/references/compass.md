# The Diátaxis Compass

When you need to create or improve documentation, the first and most important decision is: **Which quadrant(s) does the user actually need right now?**

This decision is the "compass" of Diátaxis.

## The Fundamental Question

Before writing anything, ask:

> What is the user trying to do right now?

- Do they want to **learn** something new?
- Do they have a **specific goal** and want the fastest way to achieve it?
- Do they need to **look something up** they already roughly understand?
- Do they want to **understand why** something works the way it does?

The answer maps directly to a quadrant (or combination of quadrants).

## Quick Decision Guide

| User Situation                              | Primary Quadrant(s)     | Notes |
|---------------------------------------------|-------------------------|-------|
| "I have never done this before"             | **Tutorial**            | Focus on guided success |
| "I need to accomplish X right now"          | **How-to guide**        | Direct steps to the goal |
| "What are the options for Y?" / "What does this parameter do?" | **Reference**     | Facts only |
| "Why does the system work this way?" / "Why did they design it like this?" | **Explanation** | Concepts and reasoning |

## Common Real-World Patterns

Most documentation needs fall into these patterns:

- **New user onboarding** → Heavy on **Tutorials** + light **Explanation**
- **Everyday productive use** → Mostly **How-to guides** + **Reference**
- **Troubleshooting / advanced usage** → **How-to guides** + **Reference**
- **Architectural decisions / onboarding senior engineers** → **Explanation** + **Reference**
- **Migration or major version changes** → Mix of **How-to guides** + **Explanation**

## Mixing Quadrants Deliberately

You can (and often should) combine quadrants, but you must be intentional about it:

- Good: A how-to guide that contains a small "Background" explanation section (clearly separated).
- Bad: A tutorial that drifts into reference material or starts explaining design decisions in the middle of steps.

**Rule of thumb**: When you change quadrants, make it obvious to the reader (new heading, visual separation, explicit transition).

## Anti-Patterns to Avoid

- Writing a tutorial when the user just needs a quick how-to.
- Burying critical reference information inside a long tutorial.
- Turning an explanation into a series of steps ("First you should understand X, then you should...").
- Writing "reference" that tries to teach or persuade.

The compass exists to prevent these mistakes.

## Practical Workflow

When someone asks you to create or improve documentation:

1. Clarify the user's immediate need (learning / task / lookup / understanding).
2. Decide which quadrant(s) best serve that need.
3. Write (or refactor) in the style of the chosen quadrant(s).
4. Explicitly separate different quadrants if you combine them.

This compass is the single most powerful tool in the Diátaxis framework.