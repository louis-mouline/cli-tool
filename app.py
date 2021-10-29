#!/usr/bin/env python

import click


@click.command()
@click.option("--name")
def hello(name):
    click.echo(f"Hello {name}!")


if __name__ == '__main__':
    #pylint: disable-value-for-parameter
    hello()