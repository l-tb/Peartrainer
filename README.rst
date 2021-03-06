[![CI](https://github.com/l-tb/Peartrainer/actions/workflows/ci.yml/badge.svg?branch=refactor)](https://github.com/l-tb/Peartrainer/actions/workflows/ci.yml)

=======================================================
 Peartrainer - A musical ear trainer written in python
=======================================================

Installation
============

Portable
--------

Just clone the repository or download the code and excecute the main.py
file found in src/peartrainer. You will need to install `Poetry <https://github.com/python-poetry/poetry>`__ and run ``poetry install`` to install all dependencies.

Install from Release
--------------------

Download the .tar.gz file from the latest release and install it with pip.

Build from Source
-----------------

Install `Poetry <https://github.com/python-poetry/poetry>`__ and clone this repository.
Then run ``poetry build`` in the project directory and install the created .tar.gz using pip.

Usage
=====

If you use the portable version of peartrainer visit src/peartrainer and run ``poetry run main.py``.
If you installed peartrainer using pip you can just execute it from your terminal by executing ``peartrainer``.
You will need to connect a Synthesizer because Peartrainer can only send
Midi but is unable to produce sound.



Supported APIs
==============

The following APIs are supported:

-  Linux ALSA
-  Unix Jack
-  MacOS Core Midi
-  Windows Multimedia Library

When using the Windows Multimedia Library you will need a tool like
loopMidi to create Virtual Ports

Specifying API
--------------

You can use the following flags to use a specific API:

-  Linux ALSA: ``--alsa``
-  Unix Jack: ``--jack``
-  MacOS Core Midi: ``--core``
-  Windows Multimedia Library: ``--multimedia``

Contributing
============

This project uses `Poetry <https://github.com/python-poetry/poetry>`__
for package management. To contribute you will need to install Poetry as
explained on their Github Repository.

After forking and cloning you need to run ``poetry install``. To
activate the created virtual environment run ``poetry shell``.
