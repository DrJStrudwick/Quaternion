# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog],
and this project adheres to [Semantic Versioning].

## [Unreleased]

### Added

- added license
- added code of conduct
- added initial folder structure
- added initial vscode settings
- added initial pre-commit hooks config and run
- added poetry init
- added configured testing suite
- added juypter for development
- added initial Quaternion Class
  - added `__init__` method
  - added `_typecheck` method
  - added `__eq__` method
  - added `__str__` method
  - added `__repr__` method
  - added `__add__` and `__radd__` method
  - added `__sub__` and `__rsub__` method
  - added `__mul__` and `__rmul__` method
  - added `conjugate` method
  - added `inverse` method
  - added `norm` attribute
  - added `__truediv__` and `__rtruediv__` method
  - added `trace` attribute
  - added `pure` attribute
  - added `unit` attribute
- streamlined import
- Added `tox` for multiple python version testing, including back to `3.10`
- Added `pdoc3` to generate documentation
- Added config yaml for Read the Docs
- Added `CONTRIBUTING.md`

### Changed

- Updated `README.md`

## [0.0.1] - 2024-06-20

- initial release

<!-- Links -->
[keep a changelog]: https://keepachangelog.com/en/1.0.0/
[semantic versioning]: https://semver.org/spec/v2.0.0.html

<!-- Versions -->
[unreleased]: https://github.com/Author/Repository/compare/v0.0.2...HEAD
[0.0.1]: https://github.com/Author/Repository/releases/tag/v0.0.1
