from invoke import task

@task
def test(ctx):
    ctx.run('coverage run --branch -m pytest src', pty=True)
    print('\nCoverage Report:')
    ctx.run('coverage report -m', pty=True)
    ctx.run('coverage html', pty=True)

@task
def lint(ctx):
    ctx.run('pylint src')

@task
def start(ctx):
    ctx.run('python3 src/app.py')
