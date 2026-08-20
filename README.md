# Brain Games

[![Actions Status](https://github.com/gempro760-eng/python-project-140/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/gempro760-eng/python-project-140/actions)
[![Quality gate status](https://sonarcloud.io/api/project_badges/measure?project=gempro760-eng_python-project-140&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=gempro760-eng_python-project-140)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=gempro760-eng_python-project-140&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=gempro760-eng_python-project-140)

## Descripción

Brain Games es una colección de juegos de consola para practicar lógica y
matemáticas. Cada partida tiene tres rondas y requiere responder correctamente
las preguntas generadas para ganar.

Juegos disponibles:

- `brain-games`: saludo inicial.
- `brain-even`: identifica si un número es par.
- `brain-calc`: resuelve una operación aritmética.
- `brain-gcd`: calcula el máximo común divisor.
- `brain-progression`: encuentra el número oculto de una progresión.
- `brain-prime`: identifica si un número es primo.

## Requisitos

- Python 3.10 o superior.
- [uv](https://docs.astral.sh/uv/getting-started/installation/) para instalar
	dependencias y ejecutar el proyecto.
- Git para clonar el repositorio.

## Instalación

```bash
git clone https://github.com/gempro760-eng/python-project-140.git
cd python-project-140
uv sync
```

Para construir e instalar la herramienta localmente:

```bash
uv build
uv tool install dist/*.whl --force
```

## Uso

Durante el desarrollo, los juegos pueden ejecutarse con `uv run`:

```bash
uv run brain-games
uv run brain-even
uv run brain-calc
uv run brain-gcd
uv run brain-progression
uv run brain-prime
```

Después de instalar el wheel, también pueden ejecutarse directamente:

```bash
brain-even
brain-calc
brain-gcd
brain-progression
brain-prime
```

Cada juego solicita el nombre del jugador, muestra tres preguntas y termina
con un mensaje de felicitación si todas las respuestas son correctas.

## Desarrollo

Comandos disponibles mediante `Makefile`:

```bash
make install          # Instala las dependencias
make build            # Construye el paquete
make package-install  # Instala el wheel generado
make brain-games      # Ejecuta el juego inicial
make lint             # Ejecuta Ruff
make clean            # Elimina artefactos locales
```

La lógica de los juegos se encuentra en `brain_games/games` y los puntos de
entrada ejecutables en `brain_games/scripts`.

## Demo

Cada juego incluye una ejecución ganadora y una ejecución con respuesta
incorrecta:

| Juego | Victoria | Derrota |
| --- | --- | --- |
| `brain-even` | [Ver grabación](https://asciinema.org/a/8GPxwpQN8NVTdGZd) | [Ver grabación](https://asciinema.org/a/SphT1Nbg97D7nfeF) |
| `brain-calc` | [Ver grabación](https://asciinema.org/a/GzTMLtV63Xr0sGF2) | [Ver grabación](https://asciinema.org/a/qDLj7YuJylJbOWWX) |
| `brain-gcd` | [Ver grabación](https://asciinema.org/a/B2aSqZWCCcCWF5Fy) | [Ver grabación](https://asciinema.org/a/2CtkPjZNbDzxqC1D) |
| `brain-progression` | [Ver grabación](https://asciinema.org/a/RHPXeJuyHV5DLCRO) | [Ver grabación](https://asciinema.org/a/Zn0KaW0Iitfsk1UH) |
| `brain-prime` | [Ver grabación](https://asciinema.org/a/gQuDkxtJeGbZeuPk) | [Ver grabación](https://asciinema.org/a/iDkn6GSo4YwPm6RD) |