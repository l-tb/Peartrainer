=======================================================
 Peartrainer - A musical ear trainer written in python
=======================================================

Usage
=====

Just clone the repository or download the code and excecute the main.py file found in src/peartrainer.
Note: You may need to make the file excecutable.

You will need to connect a Synthesizer because Peartrainer can only send Midi but is unable to produce sound.

Supported APIs
==============

The following APIs are supported:

 - Linux ALSA
 - Unix Jack
 - MacOS Core Midi
 - Windows Multimedia Library

When using the Windows Multimedia Library you will need a tool like loopMidi to create Virtual Ports

Specifying API
--------------

You can use the following flags to use a specific API:

 - Linux ALSA: `--alsa`
 - Unix Jack: `--jack`
 - MacOS Core Midi: `--core`
 - Windows Multimedia Library: `--multimedia`

Development
===========

This package is still under development and does not function at the moment.
