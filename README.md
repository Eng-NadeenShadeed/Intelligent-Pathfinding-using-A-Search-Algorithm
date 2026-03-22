# A* Pathfinding Implementation

## Description

This mini project demonstrates the implementation of the A* search algorithm on a grid-based environment.
The agent starts from a defined position (S) and aims to reach the goal (G) while avoiding obstacles (#).

## Concepts Used

- A* Search Algorithm
- Heuristic Function (Manhattan Distance)
- Graph Search
- Pathfinding

## How It Works

Each node in the grid is evaluated using:
- g(n): cost from the start node
- h(n): estimated cost to the goal (Manhattan distance)
- f(n) = g(n) + h(n)

The algorithm always selects the node with the lowest f(n) value to explore next.

## Example Grid

S * * .
# # * #
. . * G

## Output Example

Path found by A*: [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3)]
