import click
from api.client import Client

c = Client()

@click.group()
def main():
    """Simple CLI for querying data"""

@main.command()
@click.argument('pk')
def get(pk):
    """Get score from pk"""
    score = c.get_score(pk)
    click.echo(score)

@main.command()
@click.argument('directory')
def update(directory):
    """Update database with jsonl in directory"""
    status = c.update_data(directory)
    click.echo(status)

if __name__ == "__main__":
    main()
