CMSPlugin Template Placeholder
============

A django-cms plugin with a better placeholder tag.

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    pip install cmsplugin-template-placeholder

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://github.com/bitmazk/cmsplugin-template-placeholder.git#egg=cmsplugin_template_placeholder

TODO: Describe further installation steps (edit / remove the examples below):

Add ``cmsplugin_template_placeholder`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'cmsplugin_template_placeholder',
    )

Add the ``cmsplugin_template_placeholder`` URLs to your ``urls.py``

.. code-block:: python

    urlpatterns = patterns('',
        ...
        url(r'^//', include('cmsplugin_template_placeholder.urls')),
    )

Before your tags/filters are available in your templates, load them by using

.. code-block:: html

	{% load cmsplugin_template_placeholder_tags %}


Don't forget to migrate your database

.. code-block:: bash

    ./manage.py migrate cmsplugin_template_placeholder


Usage
-----

TODO: Describe usage or point to docs. Also describe available settings and
templatetags.


Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    mkvirtualenv -p python2.7 cmsplugin-template-placeholder
    make develop

    git co -b feature_branch master
    # Implement your feature and tests
    git add . && git commit
    git push -u origin feature_branch
    # Send us a pull request for your feature branch
