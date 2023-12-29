from setuptools import setup, find_packages

setup(
    name='rs3-merch',
    version='1.0.0',
    author='Ben Olds',
    author_email='ben@benolds.co.nz',
    description='An easy way to manage your RS3 Merching.',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=[
        'customtkinter',
    ],
)
