from invoke import task


@task
def deploy(c, bump_version="patch"):
    c.run(f'bumpversion {bump_version}')
