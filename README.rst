ANDRIMNE: Customizable build/deployment tool
============================================

**WARNING**: andrimne is currently *heavily* work-in-progress! Use at your own risk!

It currently does not do a whole lot of useful things.


SYNOPSIS
--------

Andrimne is meant to be a plug-in-enabled tool-running-platform for automating build- and deployment-related tasks.

HOW TO USE
----------

Configure andrimne for your use in ``config/andrimne.yaml``. The main area of interest here is the ``step_modules`` part.

::

  step_modules:
    - svn_checkout
    - maven_build
    - redeploy

Each *step* is a python module (i.e. a file), that has at least a ``run(config)`` function. These steps are run in the
order they appear in the list.

HELPER FUNCTIONS
----------------

The key helper function is ``run_shell_command(command, encoding='utf-8')``. It is a convenience function for running a
shell command. To use it, import: ``from andrimne.common import run_shell_command``.
