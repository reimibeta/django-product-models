#!/usr/bin/env python


import os

# allow setup.py to be run from any path
# os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# if __name__ == "__main__":
import setuptools

setuptools.setup(
    name='product_models',
    version='1.0.1',
    packages=setuptools.find_packages(),
    # install_requires=[
    #     'image-utils @ git+https://github.com/reimibeta/django-image-utils.git',
    #     'datetime-utils @ git+https://github.com/reimibeta/django-datetime-utils.git',
    #     'html-render-utils @ git+https://github.com/reimibeta/django-html-render-utils.git',
    #     'djangorestframework==3.12.4',
    #     'djangorestframework-simplejwt==4.7.0',
    #     'drf-flex-fields==0.9.0',
    #     'django-admin-list-filter-dropdown==1.0.3',
    #     'rest-framework-utils @ git+https://github.com/reimibeta/django-rest-framework-utils.git',
    #     'pillow==8.2.0',
    #     'django-cleanup==5.2.0'
    # ]
    # scripts=['makemigrations.py','migrate.py']
)
