from invoke import task


@task
def deploy(c, bump_version="patch"):
    # c.run(f'bumpversion {bump_version}')
    u = c.run('git rev-parse --abbrev-ref HEAD')
    __import__('ipdb').set_trace()
