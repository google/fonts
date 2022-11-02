---
name: Add Axis
about: Submit a custom Axis Google Fonts
title: 'Add [Axis (TAG) Name]'
labels: '--new-axis'
assignees: ''

---

## Font Project introducing the axis

(Provide the name and github repo of the font introducing the axis)

## Validate the incoming custom axis against the Axis Registry

Please inspect the current [Axis Registry](https://github.com/googlefonts/axisregistry/tree/main/Lib/axisregistry/data) and verify if there is already a custom axis that could be used for the variation purpose on the font. We should look to ensure it's not a duplicated concept.

## Super short description of what the axis does

## Image

Attach here a pic or a gif showing the axis behavior.

## Why is the axis needed

Please provide an expected case of use from the user’s point of view, reasoning on why or how the users might use or would benefit from the axis. This explanation will also help to create additional educational content.

## Axis Metadata fields

Complete the following metadata field for the axis. You could read about the [Axis Metadata Fields](https://github.com/googlefonts/axisregistry#axis-metadata-fields) in the Readme section of this repository.

```
#[TAG] based on (url of the font's repository introducing the axis)
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



