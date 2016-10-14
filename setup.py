#import ez_setup
#ez_setup.use_setuptools()

from setuptools import setup, find_packages
import aioprocessing

setup(
    name="aioprocessing",
    version=aioprocessing.version,
    packages=find_packages(exclude=["tests"]),
    author="Dan O'Reilly",
    author_email="oreilldf@gmail.com",
    description=" A Python 3.3+ library that integrates the multiprocessing module with asyncio.",
    zip_safe=False,
    license="BSD",
    keywords="asyncio multiprocessing coroutine",
    url="https://github.com/dano/aioprocessing",
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ),
)


