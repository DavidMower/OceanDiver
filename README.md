# OceanDiver
2D Platform Game - Ocean Diver


Game Design

Summary
The main character is a scuba diver who wishes to search the oceans to discover and catalogue different species of aquatic life from around the world. There’re also hidden treasures to find and ocean clean-up tasks to complete.

Gameplay
The goal of the game is to explore different underwater environments. The player must avoid dangerous obstacles such as unexploded mines, objects falling from above and potentially dangerous aquatic life if the player wishes to complete their catalogue and discover the hidden treasures.

Mind-set
Player needs to remain focused and alert to any potential dangers around them, while diving through the level exploring the environment.

Story
This game is about a scuba diver who wants to dive in different environments to see what underwater life each has to offer. The diver has been sent from a marine conservation group to document as much aquatic life as possible.
Towards the end of the game, the diver would have explored all the environments and have a catalogue containing full range of aquatic life. The catalogue contains details about each species or object which can be read as an educational element to the game.
The player can complete additional tasks such as collecting plastic garbage to clean-up the ocean and search for hidden treasure.

Demo
The demo of the game will show the diver exploring part of the Coastal Dive level and some of the fish the game will have to offer.


Technical

Platform
Scuba Diver will be a cross-platform game supporting Microsoft Windows, Macintosh computers and Linux systems. The client’s computer would need Python installed to launch this game.

Screens
Main menu
1.	Start New Game
2.	Load Game
3.	Save Game
4.	How to Play
5.	Options
6.	High Scores
7.	Quit
Level select menu
1.	Coastal Dive
2.	Coral Reef Dive
3.	Wreck Dive
4.	Cave Dive
5.	Mangrove Dive
6.	Antarctica Dive
Controls in-menus
1.	Keyboard to navigate the menu
2.	Gaming Pad as an alternative to navigate the menu
3.	Mouse as another alternative to navigate the menu
Controls in-game
1.	Keyboard to control the Scuba Divers movement.
2.	Gaming Pad as an alternative to control the Scuba Divers movement.
Mechanics
The diver has a movement speed, ranging from stopped (not moving) to swimming at full speed. The diver’s proximity to objects and aquatic life around them determines how the diver interacts. Aquatic life can be catalogued by the interact key being pressed which the diver is close enough to interact. The diver cannot swim though the aquatic life or objects within the different dive sites themselves. Colliding with these objects will cause the diver to stop moving.
The diver has health and oxygen bars, that if either reaches zero, the diver will have to start the level again. Health of the player can be lowered by certain aquatic life or objects. The diver shows damage if health is below 100%.
The diver has gold coins, treasure chests, ancient artefacts values which increase with every discovery. There’re also several plastic objects removed from the ocean.


Level Design

Themes
Coastal Dive
•	Based on Egypt’s Red Sea environment
•	Choppy water near the coast
•	Enter / exit dive from the beach
•	High amount of aquatic life
Coral Reef Dive
•	Based on Australia’s Great Barrier Reef environment
•	Bright coloured
•	Colourful them from the Corals
•	Enter / exit dive from a boat
•	High amount of aquatic life
Wreck Dive
•	Based around a World War 2 sunken war ship near France
•	Dark colours
•	Unexploded mines and other objects scattered around the sunk war ship
•	Enter / exit dive from a boat
•	Medium amount of aquatic life
Cave Dive
•	Based on a south American underwater cave
•	Dark / Dangerous / Narrow feeling
•	Objects falling around the diver occasionally
•	Enter / exit dive from a boat
•	Small amount of aquatic life
Mangrove Dive
•	Based on a Mangrove forest environment
•	Murky water
•	Lots of plants / mangroves
•	Enter / exit dive from the lakes edge (wooden pier)
•	Medium amount of aquatic life
Antarctica Dive
•	Enter / exit dive from a boat
•	Small amount of aquatic life

Basic object levels
Every level contains:
•	Aquatic Life
•	Collectable items
•	Hazards
•	Entry / exit point are the same position


Game Flow
The user launches the game. The first screen will be the main menu. In the main menu there is a set of options including Start New Game, options and quit for example. Once a game has been started, it can be paused at any time and the main menu will be displayed. The level selector will be displayed first, showing a map where different levels can be selected (in any order of completion).
Each level will have unique designs along with different underwater life selected specifically for that area. These will include freshwater for River or Lake dives and marine life so ocean dives such as reef or coastal dives. Some levels will include more dangers, such as wrecks and larger aquatic life such as sharks. The player will have a diver’s log when you can log each piece of wildlife or object discovered and keep track by viewing this log at any time.
Each level will have varying amounts of plastic garbage which can be cleared. Hidden Easter eggs will be artefacts hidden within the sand to be discovered. This won’t be visible to the player, and the sand will have to be searched manually if they wish to discover the Easter eggs.
Once you start a new level, you will see the diver either next to the dive boast or at the coast where they entered the ocean. The diver can the decent to begin their dive. You control the diver, trying to avoid different harmful objects or creatures to discover the fish they wish to document. The game will indicate when danger appears by presenting a warning sign whenever a hazard or potentially dangerous creature is near the diver. If the player gets hit or attacked then the diver’s health will drop and if the players health is depleted, the player must restart the level. The player can explore all the ocean but is trying to leave the edge of the map, an indicator will pop up to tell the diver they are going too far from the boat/coast.
The player will have an oxygen level which depletes over time. The oxygen level can be restored by returning to the dive boat or beach periodically to replenish. If the oxygen level reaches zero, then the diver will die, and the level will restart.


Graphics

Style Attributes
Characters and environments are made up of simple 2D shapes. Each level will have a different feel in terms of the number of colours and lighting.

Reference material:
Simple 2D shapes which can be repeated often without requiring lots of processing power.


Darker colour scheme to signify the level increased amount of dangers.


Asset List

2D Sprites

Dynamic Sprites
Characters
•	Scuba Diver
Aquatic Life
•	Egypt – Blue Spotted Stingray, Giant Moray Eel, Snowflake Moray Eel, Lionfish, Red Sea Clownfish, Coral Grouper, Lyretail Anthias, Picasso Trigger Fish, Masked Puffer, Sabre Squirrelfish, Crown Butterfly Fish, Masked Butterfly Fish, Emperor Angelfish, Bluefin Trevally, Blackspotted Sweetlips, Fiveline Cardinalfish, Octopus, Hermit crab, Green Turtle, Dugong, Scalloped Hammerhead shark, Oceanic Whitetip shark, Tiger shark.
•	Australia – Tusk fish, Manta Rays, Tiger Sharks, Whale Sharks, Damselfish, Butterfly fish, Triggerfish, Cowfish, pufferfish, angelfish, sea horses, scorpion fish, surgeon fish, green turtle, loggerhead turtle, leatherback turtle, sea snakes, humpbacked whale, dugongs, whale shark, sea anemones, jellyfish, coral trout, crocodile, bottlenose dolphins
•	Wreck Dives – Grey seals, harbour seals, basking sharks, wrasses, Pollock, cod, sea-urchin, starfish, leaf fish, cutell fish, frog fish
•	Cave Dives – Crabs, Lobsters, Crustaceans
•	Mangrove Dives – Sea anemones, Brittle starts, sea urchins, fiddler crabs, mud lobster, alligators, crocodiles, lemon shark babies
•	Antarctica Dive – jellyfish, sea butterflies, dogfish, squat lobsters, crabs, fur seals, leopard seals, penguins, walruses
Hazards
•	Sea Mines
Static Sprites
Environment
•	Corals
•	Rocks
•	Plants / Mangroves
•	Crystals
Objects
•	Sunken shipwreck
•	Dive boat
Collectibles
•	Gold coins
•	Treasure Chest
•	Ancient Artefact
•	Pearls
•	Plastic garbage


Sound / Music

Style Attributes
•	Coastal Dive
•	Coral Reef Dive
•	Wreck Dive
•	Cave Dive
•	Mangrove Dive
•	Antarctica Dive
Music
•	Main menu will have background music of ocean waves crashing.
•	Each level will have its own background music, with the rhythm/volume based on the amount of danger that level presents.
Sound Effects
Scuba Diver Sounds
•	Bubbles from breathing
•	Taking damage / pain
•	Death (health reached zero)
•	Warning for low amount of oxygen remaining
Collectable Sounds
•	Collectable picked up
Hazard Sounds
•	Object falling
•	Destructible object changing its state
•	Mine explosion
Level Sounds
•	Boat engine
•	Waves crashing


Enhancement Requests / Known Bugs
1.	Enchancement - Animation at the start/end of each level to show the diver either launching from the boat or the beach.
2.	Enchancement - Archways that the diver swims underneath in the Cave Dive level.