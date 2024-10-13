# Asteroids Game

A simple recreation of the classic **Asteroids** game built using **Python** and **Pygame**. Players control a spaceship that can rotate, move, and shoot bullets to destroy asteroids. Large asteroids split into smaller asteroids when hit, and the game challenges players to survive as long as possible.

## Features

- **Player Movement**: Use the keyboard to rotate the ship and move in any direction.
- **Shooting Mechanic**: Press the spacebar to shoot bullets.
- **Asteroid Splitting**: Large and medium asteroids split into smaller asteroids when hit by bullets.
- **Collision Detection**: The player can collide with asteroids, resulting in a game over.
- **Cool Shooting Down**: Players can only shoot every 0.3 seconds to avoid overpowered firing.

## Controls

- **W**: Move forward
- **S**: Move backward
- **A**: Rotate left
- **D**: Rotate right
- **Spacebar**: Shoot bullets

## Installation

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd asteroids-game
    ```
2. **Create and activate a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```
3. **Install the required dependencies:**:
    ```bash
    pip install -r requirements.txt
    ```
4. **Run the game**:
    ```bash
    python src/main.py
    ```

## File Structure
```
.
├── src/
│   ├── asteroid.py        # Asteroid class (handles asteroid behavior and splitting)
│   ├── asteroidfield.py   # AsteroidField class (spawns asteroids)
│   ├── circleshape.py     # CircleShape base class (handles collision detection)
│   ├── constants.py       # Contains game constants (screen size, asteroid sizes, player speed, etc.)
│   ├── main.py            # Main game loop and logic
│   ├── player.py          # Player class (handles movement, shooting, and collision)
│   ├── shot.py            # Shot class (handles bullets)
├── venv/                  # Virtual environment directory
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

## Game Mechanics

### Player
- The player can rotate left or right and move in any direction.
- Shooting is limited by a cooldown period of 0.3 seconds.

### Asteroids
- Asteroids come in three sizes: large, medium, and small.
- Large asteroids split into two medium asteroids when hit by a bullet.
- Medium asteroids split into two small asteroids when hit.
- Small asteroids are destroyed completely upon being hit.

### Bullets
- Bullets are small, fast-moving circles that destroy asteroids upon collision.
- Bullets originate from the tip of the player's spaceship.

## Extending the project

You've done all the required steps, but if you'd like to make the project your own, here are some ideas:

- Add a scoring system
- Implement multiple lives and respawning
- Add an explosion effect for the asteroids
- Add acceleration to the player movement
- Make the objects wrap around the screen instead of disappearing
- Add a background image
- Create different weapon types
- Make the asteroids lumpy instead of perfectly round
- Make the ship have a triangular hit box instead of a circular one
- Add a shield power-up
- Add a speed power-up
- Add bombs that can be dropped

