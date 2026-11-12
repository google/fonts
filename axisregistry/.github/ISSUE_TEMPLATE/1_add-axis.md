---
name: Add Axis
about: Submit a custom axis to Google Fonts Axis Registry.
title: 'Add (axis name here) [ (AXIS tag here) ] axis'
labels: '--new-axis'
assignees: ''

---

### Requirements

Before creating this new issue to propose a new custom axis, you should read the [Axis Registry Protocol](https://googlefonts.github.io/gf-guide/axis-registry.html) in the Production chapter of the GF-Guide. It provides the required steps for including a new axis (prior to creating this Issue), as well as detailed information on the axis requirements and the type of axes that would inform your decisions on the required Metadata Fields.

By ticking the cases (or putting x between the square brackets in text mode), you confirm the following:

- [ ] I have inspected the current [Axis Registry](https://github.com/googlefonts/axisregistry/tree/main/Lib/axisregistry/data) and there is not a registered custom axis that could be used for the variation purpose on the upcoming font project.
- [ ] The metadata fields of the proposed axis meet the *Axis Requirements* as specified in the Protocol (linked above).

### Font project(s) using the axis

(Replace this line with a line or list of the font name(s) and GitHub repo links that already use the axis)

### Short description of what the axis does

(Replace this line with a description of the effect of the axis in the font: What does it operate on (stems, terminals, serifs, etc) and how do changes happen along it?)

### Image

(Replace this line with a GIF showing the axis behavior from default to min to max to default in a loop)

### Why is the axis needed

(Replace this line with 1 or more expected cases, from the user’s point of view, with reasoning on why or how the users can benefit from the axis. This explanation helps the Google Fonts team to discern the validity of the axis itself, and its definitions, such as the ranges. This information could be used to create additional educational content.)

### Axis metadata fields

(Remove this line and fill out the mock of the data structure of the axis)

```
#(replaced this with the four letter AXIS tag) based on (replace this with a URL of the font project repository)
tag: ""
display_name: ""
min_value: 
default_value: 
max_value: 
precision: 
fallback {
  name: "Default"
  value: 0.00
}
fallback_only: false
description: ""
````



