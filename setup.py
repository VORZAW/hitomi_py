from distutils.core import setup
import pathlib

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name = 'hitomi_py',
    packages = ['hitomi_py'],
    version = '1.0',
    license='MIT',
    description = 'hitomi api',
    long_description=README,
    long_description_content_type="text/markdown",
    author = 'VORZAM',
    author_email = 'dayomosiu2@gmail.com',
    url = 'https://github.com/VORZAW/hitomi_py',
    download_url = 'https://github.com/VORZAW/hitomi_py/archive/refs/heads/main.zip',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3"
    ]
)