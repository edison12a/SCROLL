from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        descr = f.read()
    return descr


setup(
    name='scroll',
    version='2020.6.14',
    # package_dir={'': 'scroll'},
    packages=find_packages(),
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        scroll=scroll:scroll
    ''',
    # metadata to display on PyPI
    author="Edison Abahurire",
    author_email="abahedison@gmail.com",
    description="This is SCROLL",
    long_description=readme(),
    long_description_content_type="text/markdown",
    download_url="https://pypi.org/project/scroll/",
    keywords="scroll documentation unit tests",
    url="https://github.com/SimiCode/SCROLL/",   # project home page, if any
    project_urls={
        "Bug Tracker": "https://github.com/SimiCode/SCROLL/issues",
        "Documentation": "https://github.com/SimiCode/SCROLL/README.md",
        "Source Code": "https://github.com/SimiCode/SCROLL",
    },
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries :: Python Modules",
        'Programming Language :: Python :: Implementation :: CPython',
        "License :: OSI Approved :: MIT License",
    ]
)
