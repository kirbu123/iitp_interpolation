# noxfile.py
import nox_poetry


@nox_poetry.session(python=["3.11"])
def lint(session):
    session.run("poetry", "install", external=True)
    session.run("ruff", "check", "--fix", ".")

@nox_poetry.session(python=["3.11"])
def tests(session):
    session.run("poetry", "install", external=True)
    session.run("pytest", "--cov")