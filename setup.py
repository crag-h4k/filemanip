import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'phone-home',
    version = '0.0.0',
    author = 'Dane Morgan',
    author_email = 'danemorgan91@gmail.com',
    description = 'a simple phone home to check in with a remote server',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/deadlift1226/phone-home',
    install_requires = ['paramiko',], #3rd party pip packages
    packages = setuptools.find_packages(),
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)


