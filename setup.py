from setuptools import setup, find_packages

__VERSION__ = '0.0.1'

setup(
    name='pgorm',
    version=__VERSION__,
    description="A n00by PostgreSQL ORM in pure python 3.7+ which probably abuses asyncio, dataclasses & type hints",  # noqa
    long_description="Coming to nearby PostgreSQL DBs soon...",
    url='https://github.com/reckonsys/pgorm',
    author='dhilipsiva',
    author_email='dhilipsiva@pm.me',
    maintainer='Reckonsys',
    maintainer_email='info@reckonsys.com',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Framework :: AsyncIO',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: SQL',
        'Topic :: Database',
        'Topic :: Database :: Database Engines/Servers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Typing :: Typed',
    ],
    keywords='database asyncio dataclasses reckonsys postgres postgresql orm pgorm sqlalchemy django-orm peewee orator',  # noqa
    packages=find_packages(),
    install_requires=[
        'asyncpg', 'inflection'
    ],
)
