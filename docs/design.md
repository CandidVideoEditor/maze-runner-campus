# Maze Runner Campus – Game Design Document

## 1. Overview
Maze Runner Campus is a top-down maze adventure where:
- **Girl** = Player  
- **Boy** = Enemy chaser  
- **HOD** = Life saver / rescue NPC  
Theme: College campus maze with multiple buildings.

## 2. Core Gameplay
- Player moves through maze collecting items.
- Boy chases player using BFS/A*.
- HOD rescues the player when in danger (limited uses).
- Items increase score or provide boosts.
- Player wins by collecting all items or reaching exit.
- Player loses when caught by Boy and no HOD rescues left.

## 3. Characters
### Girl (Player)
- Speed: Medium
- Controls: Arrow keys / WASD
- Abilities: Can pick items, boost pads, win zone.

### Boy (Enemy)
- AI: BFS/A* pathfinding
- Behavior:
  - Constantly chases player.
  - Avoids walls.
  - Gets stunned when HOD intervenes.

### HOD
- Spawns occasionally near player.
- Breaks line of chase and saves player.
- Limited number of rescues (default: 3).

## 4. Items
- Coin: +10 score
- Booster: +speed temporarily
- Freeze: freezes Boy for 3 seconds

## 5. Win/Lose
- Win:
  - Collect all items or reach exit.
- Lose:
  - Boy catches player after HODs are used up.

## 6. UI Screens
- Title screen
- HUD (lives, score, boosts)
- Game over
- You win screen
