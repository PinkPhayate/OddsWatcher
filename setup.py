
from setuptools import setup, find_packages
 

setup(
        name             = 'odds_watcher',
        version          = '0.1.0',
        description      = 'this module extracts odds(rate) of hourse race held today ',
        license          = 'MIT',
        author           = 'phayate',
        long_description = readme,
        author_email     = 'pinqphayat@gmail.com',
        url              = 'https://github.com/PinkPhayate/OddsWatcher',
        keywords         = 'hourse race odds',
        packages         = find_packages("odds_watcher"),
        install_requires = [bs4, request]
        )
