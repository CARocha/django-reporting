from setuptools import setup, find_packages
import os

package = 'reporting'
setup(
    name = 'django-reporting',
    version = '1.1',
    description = 'Django Reporting System allows you to create dynamic reports for your models.',
    long_description = open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    requires = ['django (>=1.3)'],
    license = 'MIT license',

    packages = find_packages(),
    include_package_data = True,
    package_data = {'reporting': ['templates/reporting/*.html',
                                  'templates/admin/*.html',
                                  ],
                    },

    classifiers=[
        'Development Status :: 1 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Framework :: Django',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)