# Game design

Inspiration from Ultima and maybe Dragon Warrior. Graphically more Ultima.

Field battles or cutscene battles?

Maps. The city maps are going to be hand-made, but what about the wider Skyrim map? I might generate it.

# Program design

ECS, OOP, or composition?

I think people are still recommending Entity-Component-System. Do I want that? Python has weak typing, so I could send anything to any function, and it works as long as it's got the right shape. That lets me use OOP. If I keep that part mostly as free functions, I don't have diamond inheritance problems.

Alternately, I can have entities that are effectively collections of components. Or just OOP.

I'm going to start with ECS, see how it goes.

# Map Generation

## Overworld

There are several features on the map that I need to specify:
- roads
- dungeons
- cities
- water
- biome
  * I can infer wintry-ness from the Y coordinate

There are a fixed number of cities. Plenty of dungeons. I can make some tiles for each city and specify them by hind. I can draw the biomes, waterways, and roads as one giant image. What about dungeons? Well, most of them are going to be generic caves or generic bandit camps. I can allocate two colors to that.

Some dungeons will be hand-rolled. That's a third color.

Okay, so the colors I've got are:
- water
- rock
- forest
- road
- generic cave
- generic bandit hideout
- generic Dwemer
- generic barrow
- custom dungeon
- city
- impassible

There's the swampy area, though. Meh, I'll start here and worry more later.
