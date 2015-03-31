from setuptools import setup

exec(open('yelp/__version__.py').read())

setup(
    name='UCSDYelpDataChallenge',
    version=__version__,
    description='UCSD Yelp Data Challenge',
    author='UCSD',
    author_email='sah002@ucsd.edu',
    url='https://github.com/jjangsangy/YelpDataChallenge',
    packages=['yelp'],
)

