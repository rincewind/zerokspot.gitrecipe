from setuptools import setup, find_packages

setup(
        name='zerokspot.recipe.git',
        author='Horst Gutmann',
        author_email='zerok@zerokspot.com',
        description='Simple zc.buildout recipe for sources in a git repository',
        version='0.1.0',
        url='http://github.com/zerok/zerokspot.gitrecipe/',
        install_requires=['setuptools', 'zc.buildout'],
        namespace_packages=['zerokspot'],
        packages=find_packages(exclude=['ez_setup']),
        entry_points={'zc.buildout': ['default = zerokspot.recipe.git:Recipe']},
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: Plugins',
            'Framework :: Buildout',
            'Intended Audience :: Developers',
            'Programming Language :: Python',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: System :: Installation/Setup',
            'License :: OSI Approved :: BSD License',
            ]
        )
