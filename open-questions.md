# Questions to investigate

- What's the resource format? Image format, resource package format, etc.
  * zip file
  * each resource has a number
  * numbers are within its type
  * everything is a pile of numbers
  * tilemap? a grid of ASCII numbers (dunno how it's interpreted)
  * image? a grid of hex digits, 256 by 256
- Can I load other types of resources? How does that work?
  * no
  * make a build step that turns them into Python variables, base64 encoded, and plunks them in an import location
- Is there a way to add layers, triggers, objects, collision, etc to a tilemap?
  * no
  * use tiled
- Can I use a different image format?
  * no
  * convert somehow
- Is there a UI library?
  * no
