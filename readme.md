![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-green)
![Pytest](https://img.shields.io/badge/Tested-pytest-orange)

# Dependency Resolver API

A FastAPI-based dependency resolution engine that determines correct 
installation order across complex dependency graphs using DFS-based 
topological sorting and cycle detection.

## How It Works

The project is structured into three distinct layers:

**Models (Input Validation)** — Pydantic schemas validate all incoming 
requests, ensuring dependency pairs follow the correct format before 
reaching the core logic.

**Logic (Core Algorithm)** — Implements a graph using an adjacency list 
and DFS with a 3-state visited system (unvisited → visiting → done) to 
perform topological sorting. Detects circular dependencies and returns 
the exact cycle path for debugging.

**API Layer (Controller)** — FastAPI endpoints receive requests, delegate 
to the logic layer, and return either a resolved execution order or a 
structured cycle error. CORS enabled for frontend integration.

This separation ensures the codebase is modular, testable, and scalable.

## Running Tests

```bash
pip install pytest
pytest test_resolver.py -v
```

Covers: valid resolution, cycle detection, empty graphs, single nodes,
multi-node cycles, and independent dependency chains.

## 🌐 Live Demo
👉 https://gentle-paletas-e7a10f.netlify.app/

## Roadmap
- [ ] Visualize dependency graph (nodes and edges)
- [ ] Highlight cycle path visually
- [ ] Pre-filled example inputs for quick testing
- [ ] Support for larger real-world dependency datasets
- [ ] Performance optimization for large-scale graphs
