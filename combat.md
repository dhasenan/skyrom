What combat style do we want?

- Chrono Trigger style: requires a lot more work to set up each encounter; no random encounters
- FF style: gives random encounters; no need to worry about sensible placement; might require background images for each zone
- mixed: enemies appear on the map but you can avoid them
  * patrol routes require some extra work
  * could do a proximity thing?
  * could do world map has random encounters, cities only have triggered encounters

Turn-based combat for simplicity. All combat is 1v1 for now.

How do I handle stealth in combat?
- stealth impacts enemy miss chance
- can skip enemy turns sometimes
  * need to use stealth action?
- can give an extra surprise round

Ranged vs melee? Extra round at the start.

How do I determine the palette of actions available to the player?
- using consumables is always listed
  * if they don't have any consumables, they get an appropriate message
- stealth archer is _the_ Skyrim archetype; need to support that somehow
  * do I ask at the start what archetype you're going for?
  * and then if it's stealth based, you automatically roll stealth v perception
  * or maybe have a sneaky mode?
  * a sneak button?

How about the NPC?
- always have some basic attack
  * Equipment thing gets filled somehow, use the weapon there
- if they have spells, they use spells

What about summons?
- don't support them just now
- eventually support multi-person battles
  * or is it easier to do that from the start?
- should handle followers too

How do you aggro a foe? I'm going to say something like: there are no solid tiles between you two and you're within 4 tiles (Manhattan distance), if they're already an enemy. If they're peaceful, you can walk up to them to begin combat, which doesn't really match with the stealth archer thing...
