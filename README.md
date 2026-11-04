# QGIS Plugin Modernization Standard

This repository contains the **Standard Modernization Guide for QGIS Plugins**:
a practical migration path from `pip`/`requirements.txt` to `uv`, plus a
copy-ready plugin template.

The standard targets **QGIS 3.28–4.x (Qt5/Qt6)** and a modern Python toolchain.

## Content

- [📄 Modernization Guide (GUIDE.md)](GUIDE.md): migration, `pyproject.toml`,
  `uv.lock`, Makefile, tests, CI, packaging and troubleshooting.
- [`template/`](template/): `pyproject.toml`, `Makefile`, `.flake8`,
  `.pre-commit-config.yaml`, `.gitignore` and a lockfile.

## What this standard assumes

- **`uv` manages development**: environment, lockfile and tool execution.
- **QGIS is external**: QGIS, Qt and GDAL are provided by the QGIS installation;
  they are not installed through `uv`.
- **No PyQt runtime dependency**: plugins import from `qgis.PyQt`, never from
  `PyQt5`/`PyQt6` directly.
- **One packaging tool**: `qgis-manage` (0.16.1+) for compile, deploy, package,
  artifact validation and portal security; `qgis-plugin-ci` is an alternative,
  not an extra requirement.
- **Shapefile for BlenderGIS**: vector interchange uses `.shp` with `.prj`;
  GeoPackage and DXF are for QGIS/CAD, not BlenderGIS.
- **Reproducibility**: `uv sync --frozen` in CI and `uv lock --check`.

## How to use

1. Read [GUIDE.md](GUIDE.md).
2. Copy `template/pyproject.toml`, `Makefile`, `.flake8`,
   `.pre-commit-config.yaml` and `.gitignore` into the plugin repository.
3. Adjust the package name, Python policy, QGIS metadata and license.
4. Run:

   ```bash
   uv lock
   uv sync
   uv run pre-commit install
   uv run qgis-manage validate --strict --repo
   ```

5. Add `metadata.txt`, the plugin entry point and tests; build the ZIP with
   `make package` and upload it to the QGIS plugin repository.

## Standard objectives

1. **Speed**: install the development environment with `uv`.
2. **Quality**: Ruff, Flake8 (portal scope), mypy, tests and the QGIS analyzer.
3. **Reproducibility**: `pyproject.toml` + `uv.lock`, no ad-hoc environments.
4. **Portal readiness**: artifact validation and security scanning before upload.
5. **Interoperability**: georeferenced 3D outputs for GIS and BlenderGIS.

## License

The documentation is distributed under **CC-BY-4.0**. The template is provided
under **GPL-2.0-or-later** so it can be adapted to QGIS plugin requirements.
