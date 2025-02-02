```
name: Feature Request
about: Suggest a new feature or improvement
title: "[FEATURE] "
labels: ["enhancement"]
body:
  - type: textarea
    id: problem
    attributes:
      label: Problem Description
      description: What problem does this feature solve?
    validations:
      required: true
  - type: textarea
    id: solution
    attributes:
      label: Proposed Solution
      description: Describe your proposed solution
    validations:
      required: true
  - type: textarea
    id: alternatives
    attributes:
      label: Alternatives Considered
      description: What alternatives have you considered?
```