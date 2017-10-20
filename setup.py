try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'module to watch trade sites online for items with specific keywords',
        'author': 'Rob Thomas',
        'URL': 'nil',
        'download_url': 'nil',
        'author_email': 'nil',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['webwatcher'],
        'scripts': [],
        'name': 'WebWatcher'
        }

setup(**config)