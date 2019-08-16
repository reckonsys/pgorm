from json import load
from dataclasses import dataclass

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


@dataclass
class Version:
    year: int
    build: int
    release: str
    release_number: int
    post_number: int

    @property
    def version_string(self) -> str:
        v = f'{self.year}.{self.build}'
        if self.release:
            v = f'{v}{self.release}'
            if self.release_number:
                v = f'{v}{self.release_number}'
        if self.post_number != 0:
            v = f'{v}.post{self.post_number}'
        return v

    def __lt__(self, other) -> bool:
        attrs = ['year', 'build', 'release', 'release_number', 'post_number']
        for attr in attrs:
            self_val = getattr(self, attr)
            other_val = getattr(other, attr)
            if self_val < other_val:
                return True
            if self_val > other_val:
                return False
        return False

    def __le__(self, other) -> bool:
        return self < other or self == other

    def __gt__(self, other) -> bool:
        return not self <= other

    def __ge__(self, other) -> bool:
        return self > other or self == other


@task
def bump(c, release='p'):
    if release not in ['a', 'b', 'c', 'f', 'p']:
        raise ValueError('invalid `release` code')
    version_json = load(open('version.json'))
    v1 = Version(**version_json['version'])
    v2 = Version(**version_json['version'])
    v2.build = 232
    print(v1.version_string, v2.version_string)
