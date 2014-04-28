import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'waitress',
    'outlib',
    ]   

github_dependencies = [ 
    'git+git://github.com/rhintz42/outlib.git#egg=outlib',
]

setup(name='parsefilelib',
      version='1.0.1',
      description='parsefilelib',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      dependency_links=github_dependencies,
      install_requires=requires,
      tests_require=requires,
      test_suite="parsefilelib",
      entry_points="""\
      [paste.app_factory]
      main = parsefilelib:main
      """,
      )
