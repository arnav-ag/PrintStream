from setuptools import setup, find_packages

setup(
    name='printstream',
    version='0.1.0',
    author='Arnav',
    author_email='arnavaggarwalwork@gmail.com',
    description='A library for enhanced print debugging.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/arnav-ag/printstream',
    packages=find_packages(),
    install_requires=[
        'termcolor',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
