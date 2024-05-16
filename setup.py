from distutils.core import setup

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name='aiogram3_calendar_ru',
  packages=setuptools.find_packages(),
  version='0.2.0',
  license='MIT',
  description='Simple Inline Calendar & Date Selection tool for Aiogram (version 3.4 and upper) Telegram bots',
  long_description=long_description,
  author='Kataev Nikita',
  author_email='nik.kataev00@gmail.com',
  url='https://github.com/nik-kataev-wf-dev/aiogram3_calendar-ru',
  keywords=['Aiogram', 'Aiogram3' 'Telegram', 'Bots', 'Calendar'],
  install_requires=[
          'aiogram~=3.4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
