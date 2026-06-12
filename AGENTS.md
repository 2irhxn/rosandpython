# AGENTS.md

## Repository Purpose

Personal learning repository for Python, ROS, and hexapod robotics. Contains notes, exercises, and a target hexapod robot project.

## Directory Structure

- `code/` — Python exercise scripts and Jupyter notebooks
- `notes/` — Markdown learning notes (theory)
- `hexapod/` — **Target project**: hexapod robot (currently empty)
- `ros-ws/` — ROS workspace (currently empty)
- `notebooks/` — Jupyter experiments (currently empty)
- `resources/` — Quick reference materials

## Environment

- **Python**: 3.10 (stable)
- **ROS**: Noetic (Ubuntu 20.04)
- **Key packages**: numpy, scipy, matplotlib, jupyter, tqdm

## Markdown Format Convention

Files in `notes/` and `docs/` must start with:

```yaml
---
tags:
  - tag1
  - tag2
---
> Brief description quote.
```

Then content with `# Title` as first heading.

## No Build/Test System

This repo has no `pyproject.toml`, no CI, no lint config. Scripts are standalone.

## Quick Start

```bash
pip install -r requirements.txt
jupyter notebook notebooks/
```

## Working in This Repo

- `hexapod/` is empty — new code goes here for the hexapod project
- `ros-ws/` is empty — ROS workspace for catkin packages
- Exercise scripts in `code/` are standalone, no imports between them
- Use `requirements.txt` for dependencies, not ad-hoc installs
