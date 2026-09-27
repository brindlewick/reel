# raw: the wiki's evidence

Everything the wiki's claims rest on, exactly as it was recorded or found, committed with the
pages that cite it. A citation nobody can follow is not a citation.

**Nothing here is edited, corrected or deleted.** A page in `wiki/` may say a record is wrong. It
may not change the record.

**Adding a record is a decision to publish it**, so these checks come first, every time:

- **No secrets.** Nothing that carries a key, a token or a private address.
- **Nothing that identifies a person or a machine.** No names, hostnames or paths outside this
  repository. A trial names a phone by its model, OS version and browser version, which is what
  a reader needs to repeat it.
- **Respect what is not ours.** For documentation or an article, capture what may lawfully be
  redistributed: the citation, the retrieval date and the passages relied on, not a wholesale
  copy.

If a record cannot pass these, it does not go in, and the claim it would have supported stays
unverified.

## What lands here

```
raw/trials/<slug>/        an experiment on a real phone or browser
  method.md               what was run, on which phone, OS and browser version, and what was measured
  <recorded output>       the measurements, logs or recordings it produced

raw/articles/<slug>/      documentation, a standard or an article
  source.md               where it came from, and why it was captured
```

A trial carries `method.md` because a trial nobody can repeat is an anecdote. A capture carries
`source.md`:

```yaml
---
url: <the page>
retrieved: YYYY-MM-DD
title: <as published>
author: <as published, or unknown>
---
Why it was captured, in a sentence.
```

## What does not land here

Notes, summaries, arguments and conclusions. Those go in `wiki/`, where they can be revised and
their standing is tracked.
