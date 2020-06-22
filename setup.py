#!/usr/bin/env python

from distutils.core import setup

setup(name='entity-calendar',
      version='1.0',
      description='entity calendar: Simple Django App to provide an, for example quarterly, overview',
      author='Thomas Güttler',
      author_email='guettli@thomas-guettler.de',
      url='https://github.com/guettli/entity-calendar/',
      packages=['entity_calendar'],
      install_requires=[
            'Django>=3.0.3',
      ],
      )
