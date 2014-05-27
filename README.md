## vEvents -- VMware vSphere Events from the command-line

`vEvents` is an application that allows you to view and monitor VMware vSphere Events from the command-line.

## Requirements

* Python 2.7.x
* [docopt](https://github.com/docopt/docopt)
* [pyVmomi](https://github.com/vmware/pyvmomi)
* [vconnector](https://github.com/dnaeon/py-vconnector)

## Contributions

`vEvents` is hosted on Github. Please contribute by reporting issues, suggesting features or by sending patches using pull requests.

## Installation

In order to install `vEvents` simply execute the command below:

	# python setup.py install

## Examples

Here is an example usage of `vEvents`.

First we configure our VMware vSphere host with `vConnector`, so that `vEvents` can connect to our VMware vSphere host.

![vConnector Adding New vSphere Host](https://raw.github.com/dnaeon/py-vevents/master/img/vconnector-cli.jpg)

For more information about `vConnector` and how to use it, please refer to the [vConnector Github repository documentation](https://github.com/dnaeon/py-vconnector).

Having our VMware vSphere host registered in the `vConnector` database we can now fire up `vEvents` and monitoring our VMware vSphere Events.

![vEvents Monitoring VMware vSphere Events](https://raw.github.com/dnaeon/py-vevents/master/img/vevents-cli.jpg)

## Bugs

Probably. If you experience a bug issue, please report it to the [vEvents issue tracker on Github](https://github.com/dnaeon/py-vevents/issues).
