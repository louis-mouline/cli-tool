#!/usr/bin/env python

import glob
import click


@click.command()
@click.option(
    "--path",
    prompt="Path to search for a type of files",
    help="This is the path to search for files: /tmp"
)
@click.option(
    "--ftype",
    prompt="Pass in the type of file",
    help="Pass in the file type, i.e. csv"
)
def search(path, ftype):
    """Search files with specified type in the specified folder."""
    results = glob.glob(f"{path}/*.{ftype}")
    click.echo(click.style("Found matches:", fg="red"))
    for result in results:
        click.echo(click.style(f"{result}", bg="blue", fg ="white"))


if __name__ == '__main__':
    # pylint: disable=no-value-for-parameter
    search()