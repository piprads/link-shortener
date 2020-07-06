import click
from .url_shorten_handler import url_shorten_handler

@click.group()
def main():
    """
    Simple CLI for url shortener
    """
    pass

@main.command()
@click.argument('shorten')
def shorten(url):
    """Shortens to a 4 char link that can be open and navigated through a web browser"""
    
    short_url = url_shorten_handler.shorten_url(url)
    click.echo("Link has been shortened! You can open it here:")
    click.echo(short_url)


@main.command()
@click.argument('stats')
def stats(short_url):
    """Fetches the stats of an already shortened link"""
    stats = get_stats(short_url)
    click.echo(stats)


if __name__ == "__main__":
    main()