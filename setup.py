#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(name='webkiller',
      version='8.0.0',
      description='webkilelr test.',
      url='http://github.com/burkuts/webkiller',
      author='burkuts',
      author_email='gokt048@gmail.com',
      license='MIT',
      python_requires='>=3.7.0',
      packages=find_packages(),
      include_package_data=True,
      entry_points={
          "console_scripts": [
                "webkiller = webkiller.webkiller:main"
          ]
      },
      install_requires=[
          'adb-shell'
          'requests'
          'colorama'
          'ipapi'
          'builtwith'
      ],
      zip_safe=False
)