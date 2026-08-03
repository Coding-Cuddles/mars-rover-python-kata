# Mars rover kata in Python

[![CI](https://github.com/Coding-Cuddles/mars-rover-python-kata/actions/workflows/main.yml/badge.svg)](https://github.com/Coding-Cuddles/mars-rover-python-kata/actions/workflows/main.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Overview

This kata complements [Clean Code: Advanced TDD, Ep. 20](https://cleancoders.com/episode/clean-code-episode-20).

This repository contains several exercises designed to improve your skills in
test-driven development.

## Instructions

As a NASA engineer, you are part of the team that explores Mars by sending
remotely controlled vehicles to the planet's surface. You need to develop a
control software that translates the commands sent from Earth to instructions
that the rover understands.

NASA engineers treat the surface of Mars as a square grid, with side length
being a power of two, e.g., 4x4, 8x8, 16x16, etc.

On the grid, the rover's location is defined by coordinates (x, y) and an
orientation represented by one of the four compass directions (N, S, W, or E).
Coordinates (0, 0) represent the bottom left corner of the grid.

Given an initial rover's location, NASA sends commands encoded as a sequence
(string) of characters with the following meaning:

* 'L' and 'R' turn the rover 90 degrees left or right, respectively;
* 'F' and 'B' move the rover forward or backward one grid point.

### Exercise 1

For *Opportunity*, the grid had the torus (or "donut") topology, where (think
games like Snake or Pacman) the rover vanishes on the top and reappears on the
bottom (and visa versa for left and right).

> [!NOTE]
> In a 4x4 grid, the following table shows the resulting position for a
> movement on the grid (edge cases shown in **bold**):
>
> | Position | x + 1  | x - 1      | y + 1  | y - 1      |
> |----------|--------|------------|--------|------------|
> | (0, 0)   | (1, 0) | **(3, 0)** | (0, 1) | **(0, 3)** |
> | (1, 0)   | (2, 0) | (0, 0)     | (1, 1) | **(1, 3)** |
> | (1, 1)   | (2, 1) | (0, 1)     | (1, 2) | (1, 0)     |

Your task is to implement Opportunity's control software.

### Exercise 2

For *Curiosity*, NASA decided to improve the accuracy of their grid system by
using a Polar coordinate system. This interpretation of the grid system lends
itself to the concept of latitude and longitude: the sphere is sliced into an
even number of latitudes (central lines) and longitudes (evenly spaced lines
from North to South pole). In this model, coordinates (x, y) become abstract
representations of longitudes and latitudes.

While this model is closer to planets, it produces some significant edge cases
that complicate the control system. For example, the behavior is undefined at
the poles if we want the poles to be represented through the coordinates.

The chief engineer decided to constrain the solution to the following: the
poles are not "on the grid," so the rover moves "over" them but never rests
on them.

> [!NOTE]
> In a 4x4 grid, the following table shows the resulting position for a
> movement on the grid (edge cases shown in **bold**):
>
> | Position | x + 1  | x - 1      | y + 1  | y - 1      |
> |----------|--------|------------|--------|------------|
> | (0, 0)   | (1, 0) | **(3, 0)** | (0, 1) | **(2, 0)** |
> | (1, 0)   | (2, 0) | (0, 0)     | (1, 1) | **(3, 0)** |
> | (1, 1)   | (2, 1) | (0, 1)     | (1, 2) | (1, 0)     |

Your task is to extend the rover control software that you created for
*Opportunity* to support this new "polar" grid topology. The control software
should still support the older "torus" topology, and your implementation should
provide a way to select the desired topology.

### Exercise 3

Now, each grid point might contain an obstacle, so we need to implement
obstacle detection. If a given sequence of commands encounters an obstacle, the
rover moves up to the last possible point, aborts the sequence, and reports the
obstacle by throwing an exception.

Your task is to extend the rover control software to support obstacle
detection.

Setup is complete when the existing test suite passes.

## Prerequisites

Required:

- [Git](https://git-scm.com/downloads)
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

Optional:

- [GNU Make](https://www.gnu.org/software/make/), for shorter commands. Every required task also
  has a direct `uv` command.

You do not need to install Python or pytest separately. `uv` installs a compatible Python version
and the locked project dependencies when needed.

## Set up the kata

1. Clone the repository:

   ```console
   git clone https://github.com/Coding-Cuddles/mars-rover-python-kata.git
   ```

2. Enter the repository directory:

   ```console
   cd mars-rover-python-kata
   ```

3. Run the existing tests. Use Make when it is installed:

   ```console
   make test
   ```

   Otherwise, run pytest through `uv` directly:

   ```console
   uv run pytest
   ```

   The first run may install Python and the project dependencies. Setup is complete when pytest
   reports `1 passed`.

   If the command fails with `uv: command not found`, install
   [uv](https://docs.astral.sh/uv/getting-started/installation/) and repeat this step.

## Work on the kata

Implement the exercises in `mars_rover.py`. The initial behavior is covered by
`test_mars_rover.py`.

Run the tests after each change. Use Make when it is installed:

```console
make test
```

Otherwise, run pytest through `uv` directly:

```console
uv run pytest
```

Continue when the test run passes.

## Make command reference

Make is optional. Run `make` or `make help` to list these commands in the terminal.

| Command             | Result                                  |
| ------------------- | --------------------------------------- |
| `make all`          | Run the test suite                      |
| `make help`         | Show the command reference              |
| `make test`         | Run the test suite                      |
| `make format`       | Format tracked Python files             |
| `make format-check` | Check formatting without changing files |
| `make clean`        | Remove generated caches                 |

## Credits and references

* <https://kata-log.rocks/mars-rover-kata>
