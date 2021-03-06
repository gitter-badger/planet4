import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

pandas_version = '0.16.2'


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['-v']
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name = "Planet4",
    version = "0.4",
    packages = find_packages(),

    install_requires = ['pandas>='+pandas_version],
    tests_require = ['pytest'],

    cmdclass = {'test': PyTest},

    entry_points={
        "console_scripts": [
            'p4reduction = planet4.reduction:main',
            'plot_p4_imageid = planet4.markings:main',
            'create_season2and3 = planet4.reduction:create_season2_and_3_database',
            'p4catalog_production = planet4.catalog_production:main',
            'hdf2csv = planet4.hdf2csv:main'
            ]
    },

    #metadata
    author = "K.-Michael Aye",
    author_email = "kmichael.aye@gmail.com",
    description = "Software for the reduction and analysis of Planet4 data.",
    license = "BSD 2-clause",
    keywords = "Mars Planet4 Zooniverse",
    url = "http:www.planetfour.org",
)
