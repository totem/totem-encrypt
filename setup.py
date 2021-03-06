from setuptools import setup

with open('./requirements.txt') as reqs_txt:
    requirements = [line for line in reqs_txt]

setup(
    name="totem-encrypt",
    version="0.1.0",
    description="Encryption library used for totem",
    author='Sukrit Khera',
    packages=['encryption', 'encryption.store'],
    install_requires=requirements,
    zip_safe=True,
    test_suite='tests',
    classifiers=[
        'Development Status :: In development',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
        'License :: The MIT License (MIT)',
    ],
)
