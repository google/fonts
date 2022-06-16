So far, we’ve explored the transition of typography in augmented and virtual reality and its impact on design. Now let’s review how text will be used in this new medium.

In AR/VR, the whole world is our design space. Therefore, a good understanding of the different ways in which we can set text can have a huge impact on the reading experience. This understanding starts with the reader’s head and its placement in space, which provides our frame of reference. Do we intend to keep the text accessible to the user all the time, or do we want it to be visible only when it is required, depending on head movement? Is the text context-specific, with no relation to the space around the reader, like an important notification or warning? Or is it something that directly relates to the user's surroundings, like text highlighting the keys someone was searching for? Let’s explore each of these concepts in detail.

## Anchoring of Information

The placement of text in 3D space in reference to the reader’s head is crucial for determining how the text will be read, and for defining its behavior. Knowing this will help choose the parameters to look for while selecting and setting type.

### Anchored to head

In this case, the information moves with the person’s head so it’s always in front of them. It’s more intrusive and, in AR, this might create dangerous scenarios by limiting the visibility of the real world. This is recommended only for crucial information and for short texts.

[CAPTION] The virtual objects follow head movement and stay in view all the time.

It’s not advisable to anchor long-running text (i.e., paragraphs) to the head. In most headsets, the ends of long lines will be harder to read due to distortion close to the edges of the lens, so users might face legibility issues. Our heads tend to move a few degrees at most times, even if we are not aware of this. When reading text anchored to the head, these slight head movements result in jitter, which is not a good reading experience. In VR, to reduce jitter, UI elements may ease back into view when someone’s head moves past the UI.

### Anchored to space

In this case, virtual elements are anchored to real-world coordinates in 3D space around the subject. Therefore, the information stays at a particular position, and they see it only when they’re looking in that direction. Information anchored in space seems more immersive and realistic, and is similar to how we observe text in our physical surroundings.

[CAPTION] The virtual object stays in a specific position and doesn’t follow head movement.

## Placement Zones

We can also decide on text placement based on its perceived distance from the user. Consider these three regions based on the distance and priority of information that can be displayed in each:

[CAPTION] The distances are approximations based on different studies and guidelines for AR displays.

### Heads-up display (HUD) region

This region is reserved for user interface (UI) elements that are anchored to the head and stay in their view no matter where someone’s looking (as shown by the first image). It can be used for showing essential information, such as time, or notifications, similar to the status bar in smartphones. However, this space should be used sparingly for absolutely necessary elements. It’s recommended not to place objects too close to the subject as it results in the accommodation-vergence conflict, which causes visual fatigue.

[CAPTION] The red area shows the HUD region that requires eye movement to see the information. The information placed outside the red region requires head movement.

The placement in this region closer to the eyes enables a quick view of  essential info by shifting focus from the real world to the information in the HUD region. Moving through our depth of field, shifting focus with our eye muscles rather than moving our heads is something we perform naturally in our physical surroundings.

### User interface/interaction (UI) region

This is the ideal region for texts to be placed for the most comfortable viewing experience. Here, virtual objects like browser windows can be anchored to either the head or space around the subject, based on their utility (ensuring of course that the text doesn't hinder their view, for example when driving with AR applications). This is the most interactive of all three regions, where people can expect to manipulate and play around with virtual objects.

### Environment (world) region

The final region houses all the elements anchored to space on objects, such as the surface of a building that are usually out of the subject’s control, or with limited potential for interaction, such as the surface of a building. Virtual signage or location markers that give people information about real-world objects are typical uses of text here. The augmented information in this region can extend to infinity, so it’s up to the designers to decide how far to extend the experience and the amount of information on display. Then, the density of this information can help determine the right typefaces and optimal typesetting parameters. For example, if the subject is wearing AR glasses, they can see information from a few meters away to several blocks in front of them. The potential information density in such cases increases with distance, so this presents an interesting challenge for content creators.

We also need to remember that the person’s movement can potentially bring the text from the environment region into the interaction region. This will increase the complexity in the design, since multiple interaction scenarios need to be envisaged.

In the next article, we’ll learn how to use these parameters to spatially classify text and use it in different scenarios.

Useful Links:
- Variables that affect the experience in augmented reality
