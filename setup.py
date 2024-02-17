# python setup.py bdist_wheel
# twine upload

from setuptools import setup, find_packages

setup(
    name="xing-brokervi-crawler",
    version='0.0.1',
    url="https://github.com/BOmBzOO/xing-brokervi-crawler",
    license="MIT",
    author="Bumju Ahn",
    author_email="bombzoo78@gmail.com",
    description="xing broker vi crawler",
    install_requires=[
        'pandas',
        'pywin32'
    ],
    packages=find_packages(),
    python_requires='>=3',
    long_description=open('README.md', encoding='UTF8').read(),
    long_description_content_type="text/markdown",
    package_data={},
    zip_safe=False,
)
