---
name: Add Axis
about: Submit a custom axis to Google Fonts Axis Registry.
title: 'Add [Axis (TAG) Name]'
labels: '--new-axis'
assignees: ''

---

## Font Project introducing the axis

(Provide the name and GitHub repo of the font introducing the axis)

## Validate the incoming custom axis against the Axis Registry

Please inspect the current [Axis Registry](https://github.com/googlefonts/axisregistry/tree/main/Lib/axisregistry/data) and determine if there is already a custom axis that could be used for the variation purpose on the font. We should ensure it's not a duplicated concept.

## Short description of what the axis does

Describe the effect of the axis in the font. Over what does it operates (stems, terminals, serifs, etc) how changes happen. 

## Image

Attach here a pic or a gif showing the axis behavior.

## Why is the axis needed

Please provide an expected case of use from the user’s point of view, reasoning on why or how the users might use or would benefit from the axis. 

This explanation would help to discern the validity of the axis itself and its definitions such as the ranges. This information could be used to create additional educational content.

## Axis metadata fields

Complete the following metadata field for the axis. You can read about the [Axis Metadata Fields](https://github.com/googlefonts/axisregistry#axis-metadata-fields) in the Readme section of this repository.

- For the time being every custom axis is registered with only one fallback, which should be named "Default" and the value should match the axis `default_value`.
- The description gives users more context about what the axis does or how it can be used. It should be written in a general way allowing it to make sense for other cases and should include a clarificacion of the range. This text is used on the Type Tester tab of the font specimen page, under the info button (i) next to the axis name.

```
#[Four letter axis TAG] based on (url of the font's repository introducing the axis)
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



