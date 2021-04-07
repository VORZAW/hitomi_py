from distutils.core import setup
setup(
    name = 'hitomi_py',         # How you named your package folder (MyLib)
    packages = ['hitomi_py'],   # Chose the same as "name"
    version = '1.0',      # Start with a small number and increase it with every change you make
    license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description = 'hitomi api',   # Give a short description about your library
    author = 'VORZAM',                   # Type in your name
    author_email = 'dayomosiu2@gmail.com',      # Type in your E-Mail
    url = 'https://github.com/VORZAW/hitomi_py',   # Provide either the link to your github or to your website
    download_url = 'https://github.com/VORZAW/hitomi_py/archive/v_1-0.tar.gz',    # I explain this later on
    classifiers=[
        'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3"
    ]
)