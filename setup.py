"""
Flask-Spotify-Auth
------------------
Greg VanOrt

This library is used for connecting a flask application to the Spotify OAuth2 interface.
"""

from setuptools import setup

setup(
    name='flask-spotify-auth',
    version='0.1',
    url='https://github.com/vanortg/flask-spotify-auth',
    license='MIT',
    author='Gregory VanOrt',
    author_email='grvanort@gmail.com',
    description='Flask library for Spotify user authentication',
    long_description=__doc__,
    py_modules=['flask_spotify_auth'],
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'Flask',
    ],
    classifiers=[
        'Environment :: Server Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python3',
    ]
)
