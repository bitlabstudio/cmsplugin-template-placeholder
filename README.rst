CMSPlugin Template Placeholder
==============================

A django-cms plugin with a better placeholder tag.

Unfortunately the ``{% placeholer %}`` tag of django-cms3 is not an assignment
tag. This plugin adds a ``{% placeholder_as %}`` tag to address this issue.

Additionally, we also thought that it would be cool to allowed the use of any
templatetag in Placeholder fields. This is extremely useful when linking via
the ``{% url %}`` tag, for example.

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    pip install cmsplugin-template-placeholder

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://github.com/bitmazk/cmsplugin-template-placeholder.git#egg=cmsplugin_template_placeholder

Add ``cmsplugin_template_placeholder`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'cmsplugin_template_placeholder',
    )

Before the new tags are available in your templates, load them by using

.. code-block:: html

	{% load cmsplugin_template_placeholder_tags %}


Usage
-----

Import the tag and use it similar to the original ``{% placeholder %}`` tag:

.. code-block:: html

    {% load cmsplugin_template_placeholder %}
    {% placeholder_as "placeholder_name" as output %}
    {{ output }}


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
