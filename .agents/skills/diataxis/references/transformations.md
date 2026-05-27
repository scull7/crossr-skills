# Documentation Transformations

One of the most powerful uses of Diátaxis is taking existing messy documentation and refactoring it into the correct quadrants.

Below are common transformation patterns with before/after examples.

## 1. Turning a "Mixed" Document into Proper Quadrants

**Before** (typical bad document):

```
# Working with Users

Users are represented by the User model. The model has these fields: id, email, name, created_at.

To create a user, go to the admin panel and click "New User". Fill in the email and name. Then click Save.

It is important to understand that users are the central concept in the system. Everything else (posts, comments, permissions) is connected to a user. This design was chosen because...

When you create a user, the system will send a welcome email automatically.
```

**Problems**: This document mixes Reference, How-to, and Explanation with no separation.

**After** (properly split):

**Reference** (`reference/users.md`):
```
# Users

## Fields
- `id` (integer, primary key)
- `email` (string, unique, required)
- `name` (string)
- `created_at` (timestamp)

## Relationships
- A user has many posts
- A user has many comments
- ...
```

**How-to guide** (`how-to-guides/create-a-user.md`):
```
# Create a user

1. Log into the admin panel.
2. Click "New User".
3. Enter the user's email address and name.
4. Click **Save**.

The system will automatically send a welcome email.
```

**Explanation** (`explanation/user-model-design.md`):
```
# Why users are the central concept

Users sit at the root of the permission and content model. This design decision was made because...
```

## 2. Turning a Long "Tutorial" into a Real Tutorial + Supporting Material

**Before**: A 40-page "Getting Started" guide that tries to teach everything at once.

**After**:
- One short, focused **Tutorial** that gets the reader to a meaningful success in 15-20 minutes.
- Several **How-to guides** for common next steps.
- **Reference** sections for the detailed information.
- **Explanation** articles for the conceptual background.

## 3. Turning Conceptual Rambling into Explanation

**Before**:
"First you need to understand the event system. Events are fired when... Then you should listen for events using... It is recommended that you..."

**After** (Explanation):
```
# The event system

The framework uses an event bus to decouple components. When component A needs to notify other parts of the system that something happened, it publishes an event rather than calling other components directly.

This design has two main consequences:
1. ...
2. ...
```

## 4. Turning a "Reference" That Explains Too Much

**Before**:
```
## The `timeout` parameter

The `timeout` parameter controls how long the system will wait before giving up. This is useful because networks are unreliable. You should usually set it to 30 seconds for most operations, but for file uploads you might want to use a higher value...
```

**After** (pure Reference):
```
## `timeout`

- Type: integer (seconds)
- Default: 30
- Maximum: 3600

Controls the maximum time the client will wait for a response.
```

Move the advice and rationale to a How-to guide or Explanation.

## General Transformation Heuristics

- **Does this sentence tell the reader what to do?** → Probably belongs in a Tutorial or How-to.
- **Does this sentence explain why or how the system works?** → Probably belongs in Explanation.
- **Is this sentence purely factual information about the system?** → Probably belongs in Reference.
- **Is this written as a lesson for someone learning?** → Probably belongs in a Tutorial.

When in doubt, split the content rather than trying to make one document do multiple jobs.