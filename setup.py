"""
Based entirely on Django's own ``setup.py``.
"""
import os
from distutils.command.install import INSTALL_SCHEMES
from setuptools import setup, find_packages


import tagging



def fullsplit(path, result=None):
    """
    Split a pathname into components (the opposite of os.path.join) in a
    platform-neutral way.
    """
    if result is None:
        result = []
    head, tail = os.path.split(path)
    if head == '':
        return [tail] + result
    if head == path:
        return result
    return fullsplit(head, [tail] + result)

# Tell distutils to put the data_files in platform-specific installation
# locations. See here for an explanation:
# http://groups.google.com/group/comp.lang.python/browse_thread/thread/35ec7b2fed36eaec/2105ee4d9e8042cb
for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

setup(
    name = 'django-tagging',

    install_requires=[
        'unidecode',
    ],
    version = tagging.get_version(),
    description = 'Generic tagging application for Django',
    url = 'http://github.com/pythonben/django-tagging',
    packages = ['tagging', 'tagging.templatetags', 'tagging.tests', 
                 ],
    classifiers = ['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
)
