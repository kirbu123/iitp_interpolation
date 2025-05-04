# noxfile.py
import nox_poetry

# Default locations to check/format
locations = "src", "tests", "noxfile.py"


# @nox_poetry.session(python=["3.12"])
# def lint(session) -> None:
#     """Lint using flake8."""
#     args = session.posargs or locations
#     session.install("flake8")
#     session.run("flake8", *args)


# @nox_poetry.session(python="3.8")
# def black(session) -> None:
#     """Run black code formatter."""
#     args = session.posargs or locations
#     session.install("black")
#     session.run("black", *args)


@nox_poetry.session(python=["3.11", "3.12"])
def format(session) -> None:
    """Run ruff code formatter."""
    session.run("poetry", "install", external=True)
    session.run("ruff", "check", "--fix", ".")


@nox_poetry.session(python=["3.11", "3.12"])
def tests(session) -> None:
    """Run the test suite."""
    session.run("poetry", "install", external=True)
    session.run("pytest", "--cov")
