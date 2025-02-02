```
name: Bug Report
about: Report a bug that you've found
title: "[BUG] "
labels: ["bug", "triage"]
body:
  - type: markdown
    attributes:
      value: Thanks for taking the time to fill out this bug report!
  - type: textarea
    id: description
    attributes:
      label: Bug Description
      description: What happened?
    validations:
      required: true
  - type: textarea
    id: expected
    attributes:
      label: Expected Behavior
      description: What should have happened?
    validations:
      required: true
  - type: textarea
    id: reproduction
    attributes:
      label: Steps to Reproduce
      description: How can we reproduce this issue?
    validations:
      required: true
      
```      
      
