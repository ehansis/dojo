import click


@click.command()
@click.argument('greeting')
@click.argument('name')
@click.option('--reps', default=3, help='number of repetitions')
def hello_args(greeting, name, reps):
    click.echo((greeting + ' ' + name + '! ') * reps)


@click.command()
@click.option('--greeting', prompt='The greeting')
@click.option('--name', prompt='The name')
@click.option('--reps', default=3, help='number of repetitions')
def hello_prompt(greeting, name, reps):
    click.echo((greeting + ' ' + name + '! ') * reps)


@click.group()
def doit():
    pass


@doit.command()
@click.argument('what')
def it(what):
    """Do something"""
    click.echo("Did " + what)


@doit.command()
def itnot():
    """Dont' do it"""
    click.echo("Did it not")


if __name__ == "__main__":
    # hello_prompt()
    # hello_args()
    doit()
    hello_args()
