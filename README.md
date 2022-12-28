SublimeLinter-rome
================================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-rome.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-rome)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [rome](https://rome.tools). It will be used with files that have the “JavaScript” and "TypeScript" syntaxes. As Rome adds support for other languages, support will be added here. Use the "selector" setting to control for which languages this plugin is used.

## Installation
SublimeLinter must be installed in order to use this plugin. 

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before installing this plugin, you must ensure that `rome` is installed on your system, or in your project.

To install `rome`, do the following:

- Install [Node.js](http://nodejs.org) (and [npm](https://github.com/joyent/node/wiki/Installing-Node.js-via-package-manager) on Linux).

- Install `rome` globally by typing the following in a terminal:
```
npm install -g rome
```
    
- Or install `rome` locally in your project folder (**you must have a `package.json` file there**):
```
npm install -D rome
```

## Settings
- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
- Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
