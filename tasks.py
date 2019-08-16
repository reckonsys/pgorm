from invoke import task


@task
def init(c):
    c.run('pipenv install -d neovim ipdb pycalver')


@task
def deploy(c, bump_version="patch"):
    # c.run(f'bumpversion {bump_version}')
    # result = c.run('git rev-parse --abbrev-ref HEAD')
    # current_branch = result.stdout.strip()
    __import__('ipdb').set_trace()
