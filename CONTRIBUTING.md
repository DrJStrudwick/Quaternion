<!--
 Copyright (c) 2024 James Strudwick

 This software is released under the MIT License.
 https://opensource.org/licenses/MIT
-->
# Contributing

For those wishing to contribute please read the following guide on how to contribute to this package.

Sections

- [Ways to contribute](#ways-to-contribute)
- [Developer workflow](#development-workflow)
- [Developer environment](#developer-environment)
  - [Pre-requisites](#pre-requisites)
  - [Base environment](#base-environment)
  - [Coding standards](#coding-standards)
  - [Documentation](#documentation)
  - [Testing](#testing)
  - [IDE](#ide)

## Ways to contribute

Contributions may take the form of any of the following, all of which are welcome:

- Submitting feature requests.
- Submitting bug reports.
- Creating code to resolve any issues.
- Creating more documentation. This can be either code documentation or examples.

## Development workflow

We look to operate with a standard development workflow, that is for any new development we would like to go through the following steps:

 1. Please create a corresponding issue related to the Bug report/Feature request.
 2. Create a branch off main, related to your issues & do your work within that branch, including tests & documentation.
 3. Run tests and ensure everything passes with test coverage achieving over 80%.
 4. Submit a pull request.
 5. Upon review, if successful the pull request will be approved and the deployment pipeline triggered.

## Developer environment

### Pre-requisites

The following are pre-requisites that are needed on your local machine to be able to contribute to this package:

- `Python`. We opt for using `pyenv` to manage our Python distributions details of which can be found here (<https://github.com/pyenv/pyenv>) but contributors do not have to use `pyenv` if they have some other method. This package was developed starting from `Python 3.12.5`, we shall aim to ensure that the package will continue to work with future releases as soon as they become available. We have back-tested this package and established it works with `3.10` and `3.11`.
- `Poetry`. We use `poetry` to manage the virtual environment used for developing this package (`v1.8.3`). Whilst there are other virtual environment managers this is our recommend one as some of our pre-commit hook are configured to use `poetry`. Details can be found here (<https://python-poetry.org/>)

### Base environment

With the pre-requisites installed, the virtual environment can be initialized by running the following in your cli:

```shell
poetry config virtualenvs.in-project true
poetry install
```

*Note:* The first command will make poetry create the virtual environment files in the project directory, this will help keep your system tidy, but ultimately it is optional.

### Coding standards

We use pre-commit hooks to help ensure that the code base remains of the same consistency & standard as it develops, these can be found in `.pre-commit-config.yaml` and can be installed by running:

```shell
pre-commit install
```

Checks will be run on pull requests to check that submitted development meets our standards and by installing these it will save you from having to go back and make corrections. At it's core we use `Ruff` (<https://docs.astral.sh/ruff/>) as our main linter & formatter.

### Documentation

Within our development environment we have included `pdoc3` (<https://pdoc3.github.io/pdoc/>) to generate documentation for our package *AND*, if you have installed the pre-commit hooks, will automatically be generated whenever you make commits. So as long as you write DocStrings with the code you submit, which will also be checked by the pre-commit hooks, you don't have to worry any further about documentation.

If you wish to check what the documentation will look like before submitting in your cli you can run:

```shell
pdoc --html quaternion --force -o docs
```

and then open `docs/quaternion/index.html` in your browser to check the outputs.

Currently our documentation is hosted by `Read the Docs` (<https://readthedocs.org/dashboard/>), which is configured by `.readthedocs.yaml`. Our packages documentation can be found at (quaternion-djs.readthedocs.io) and only shows what is currently based in the `main` branch

### Testing

We use `pytest` (<https://docs.pytest.org/en/stable/>) to test our code base, which can be found in `quaternion/tests` and we use `pytest-cov` (<https://pytest-cov.readthedocs.io/en/latest/readme.html>) to measure the coverage of our tests, which is configured in `.coveragerc`. Please ensure that any code contributed has tests that cover it.

Tests can be launched by running the following in your cli:

```shell
pytest
```

and then for testing across multiple version of python we use `tox` (<https://tox.wiki/en/stable/>) you can run the following in your cli:

```shell
tox
```

*Reminder:* If you use `pyenv` to manage your python distributions and wish to run `tox` over the python versions specified in `pyproject.toml` then you'll need to install the ones listed in `.python-version`. You wont need to run `pyenv local ...` as the `.python-version` file will take care of that for you.

### IDE

You can use whichever IDE you wish but we developed this with initially within `Visual Studio Code`, our setting for this workspace is included within `.vscode/settings.json`
