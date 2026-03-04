import subprocess

import typer
from rich import print
from rich.progress import track

APP_NAME = "Universal Updater Utility"
APP_VERSION = "0.1"
APP_AUTHOR = "Francois B (Makoto)"
APP_WEBSITE = "https://makotonoblog.be"

app = typer.Typer()


@app.command()
def about():
    """Return the About information"""
    print(f"[blue]::[/blue] {APP_NAME} {APP_VERSION}")
    print(f" [yellow]-->[/yellow] author : {APP_AUTHOR}")
    print(f" [yellow]-->[/yellow] website : {APP_WEBSITE}")


@app.command()
def version():
    """Return the app version"""
    print(f"{APP_VERSION}")


def processcmd(text, cmd):
    """Process a given bash command

    Arguments:
        text -- Task description
        cmd -- Bash command to perform
    """
    print(f" [yellow]-->[/yellow] {text} ({cmd})")
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            executable="/bin/bash",
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError as cpe:
        result = cpe.output
    finally:
        print(result.stdout)


@app.command()
def pipxugrade():
    """Upgrade all pipx packages"""
    processcmd("Upgrading pipx packages", "pipx upgrade-all")


@app.command()
def yarnugrade():
    """Upgrade all Yarn packages installed globally"""
    processcmd("Upgrading yarn packages", "yarn-upgrade-all -g")


@app.command()
def flatpakugrade():
    """Upgrade all Flatpak packages"""
    processcmd("Upgrading flatpak packages", "flatpak update -y")


@app.command()
def rustupupdate():
    """Upgrade rustup and thus Rust components"""
    processcmd("Upgrading rustup", "rustup update")


@app.command()
def cargoupgrade():
    """Upgrade all Cargo packages"""
    processcmd("Upgrading cargo packages", "cargo install-update -a")


@app.command()
def cinnamonspices():
    """Upgrade all Cinnamon Desktop spices"""
    processcmd("Upgrading cinnamon spices", "cinnamon-spice-updater --update-all")


@app.command()
def tldrupdate():
    """Update the local cache of tldr pages"""
    processcmd("Upgrading tldr pages", "tldr -u")


@app.command()
def brewupdate():
    """Fetch the newest version of Homebrew and all formulae from GitHub using git and perform any necessary migrations"""
    processcmd("Upgrading brew", "brew update")


@app.command()
def brewupgrade():
    """Upgrade outdated casks and outdated, unpinned formulae using the same options they were originally installed with, plus any appended brew formula options"""
    processcmd("Upgrading brew packages", "brew upgrade")


@app.command()
def atuinupdate():
    """Upgrade atuin binary"""
    processcmd("Upgrading atuin", "atuin-update")


@app.command()
def codeupgrade():
    """Upgrade all VSCode extensions"""
    processcmd("Upgrading VSCode extensions", "code --update-extensions")


@app.command()
def codiumupgrade():
    """Upgrade all VSCodium extensions"""
    processcmd("Upgrading VSCodium extensions", "codium --update-extensions")


@app.command()
def upgrade():
    """Upgrade everything at once"""
    print("[blue]::[/blue] Updating system...")
    fcts = (
        pipxugrade,
        yarnugrade,
        flatpakugrade,
        rustupupdate,
        cargoupgrade,
        cinnamonspices,
        tldrupdate,
        brewupdate,
        brewupgrade,
        atuinupdate,
        codeupgrade,
        codiumupgrade,
    )
    for fct in fcts:
        fct()


@app.command()
def archnews():
    """Display Arch Linux news about packages"""
    processcmd("News from Arch Linux", "yay -Pwwq")


@app.command()
def cleanorphan():
    """Uninstall pacman orphan packages"""
    print(
        " [yellow]-->[/yellow] Clean pacman orphan packages (sudo pacman -Rs $(pacman -Qqtd))"
    )
    try:
        result = subprocess.run(
            "pacman -Qqtd && sudo pacman -Rs $(pacman -Qqtd)",
            shell=True,
            executable="/bin/bash",
            stderr=subprocess.STDOUT,
        )
    except subprocess.CalledProcessError as cpe:
        result = cpe.output
    finally:
        print(result)


@app.command()
def flatpakuninstall():
    """Uninstall unused package(s) runtimes(s)"""
    processcmd("Uninstalling unused flatpak packages", "flatpak uninstall --unused -y")


@app.command()
def brewclean():
    """Remove stale lock files and outdated downloads for all formulae and casks, and remove old versions of installed formulae"""
    processcmd("Cleaning up brew", "brew cleanup")


@app.command()
def brewautoremove():
    """Uninstall formulae that were only installed as a dependency of another formula and are now no longer needed"""
    processcmd("Auto-removing brew", "brew autoremove")


@app.command()
def clean():
    """Perform all cleaning tasks at once"""
    print("[blue]::[/blue] Cleaning system...")
    fcts = (flatpakuninstall, brewclean, brewautoremove)
    for fct in fcts:
        fct()


def main():
    app()


if __name__ == "__main__":
    main()
