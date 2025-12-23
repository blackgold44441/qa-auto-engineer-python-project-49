### Hexlet tests and linter status:
[![Actions Status](https://github.com/blackgold44441/qa-auto-engineer-python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/blackgold44441/qa-auto-engineer-python-project-49/actions)
### SonarQube
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=blackgold44441_qa-auto-engineer-python-project-49&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=blackgold44441_qa-auto-engineer-python-project-49)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=blackgold44441_qa-auto-engineer-python-project-49&metric=bugs)](https://sonarcloud.io/summary/new_code?id=blackgold44441_qa-auto-engineer-python-project-49)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=blackgold44441_qa-auto-engineer-python-project-49&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=blackgold44441_qa-auto-engineer-python-project-49)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=blackgold44441_qa-auto-engineer-python-project-49&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=blackgold44441_qa-auto-engineer-python-project-49)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=blackgold44441_qa-auto-engineer-python-project-49&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=blackgold44441_qa-auto-engineer-python-project-49)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=blackgold44441_qa-auto-engineer-python-project-49&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=blackgold44441_qa-auto-engineer-python-project-49)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=blackgold44441_qa-auto-engineer-python-project-49&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=blackgold44441_qa-auto-engineer-python-project-49)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=blackgold44441_qa-auto-engineer-python-project-49&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=blackgold44441_qa-auto-engineer-python-project-49)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=blackgold44441_qa-auto-engineer-python-project-49&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=blackgold44441_qa-auto-engineer-python-project-49)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=blackgold44441_qa-auto-engineer-python-project-49&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=blackgold44441_qa-auto-engineer-python-project-49)

**Brain Games** is a console-based set of logic games.  
This is a Hexlet educational project focused on Python basics, CLI applications, modular architecture, and automated code quality checks.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/blackgold44441/qa-auto-engineer-python-project-49.git
cd qa-auto-engineer-python-project-49
```

Build and install the package:
```bash
make package-install 
```
After installation, the game commands (brain-*) will be available globally.


Games
Even Number Check (brain-even)

[![asciicast](https://asciinema.org/a/761462.svg)](https://asciinema.org/a/761462)

Calculator (brain-calc)

[![asciicast](https://asciinema.org/a/JgT2NB6CMInb21P9lAYa6E1Ly.svg)](https://asciinema.org/a/JgT2NB6CMInb21P9lAYa6E1Ly)

Greatest Common Divisor (brain-gcd)

[![asciicast](https://asciinema.org/a/EQdCIqubyxvEChkgbwSTUj8Ln.svg)](https://asciinema.org/a/EQdCIqubyxvEChkgbwSTUj8Ln)

Arithmetic Progression (brain-progression)

[![asciicast](https://asciinema.org/a/9bPWnFkEGyoK2IJL7cFue1KDM.svg)](https://asciinema.org/a/9bPWnFkEGyoK2IJL7cFue1KDM)

Prime Number Check (brain-prime)

[![asciicast](https://asciinema.org/a/q1ItEQu7ALsYoq520FAwAanP2.svg)](https://asciinema.org/a/q1ItEQu7ALsYoq520FAwAanP2)

## Project Architecture

- Shared game logic is implemented in the `engine` module
- Each game is implemented in a separate module inside the `games` package
- CLI entry points are placed in the `scripts` directory
- All games reuse a common game engine to avoid code duplication