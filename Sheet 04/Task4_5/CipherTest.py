#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pprint
import matplotlib.pyplot as plt
from sslyze.plugins_finder import PluginsFinder
from sslyze.plugins_process_pool import PluginsProcessPool
from sslyze.server_connectivity import ServerConnectivityInfo, ServerConnectivityError, ServersConnectivityTester

if __name__ == '__main__':

    path = 'top100.txt'
    file = open(path, 'r')

    cipherCount = dict()

    for line in file:
        for word in line.split():

            # Setup the servers to scan and ensure they are reachable
            hostname = word
            print'\nconnecting to {}'.format(hostname)
            try:
                server_info = ServerConnectivityInfo(hostname=hostname)
                server_info.test_connectivity_to_server()
            except ServerConnectivityError as e:
                # Could not establish an SSL connection to the server
                raise RuntimeError('Error when connecting to {}: {}'.format(hostname, e.error_msg))

            sslyze_plugins = PluginsFinder()

            plugins_process_pool = PluginsProcessPool(sslyze_plugins)

            from sslyze.plugins.openssl_cipher_suites_plugin import OpenSslCipherSuitesPlugin

            print '\nchecking ciphers for {}'.format(hostname)
            plugin = OpenSslCipherSuitesPlugin()
            plugin_result = plugin.process_task(server_info, 'tlsv1')
            # adding ciphers which were accepted by the host
            for cipher in plugin_result.accepted_cipher_list:
                if cipherCount.has_key(cipher.name):
                    cipherCount[cipher.name] = cipherCount.get(cipher.name) + 1
                else:
                    cipherCount[cipher.name] = 1
                print '    {} was added to cipherCount'.format(cipher.name)

    print '\nAll ciphers accepted by the hosts from top100.txt:\n'
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(cipherCount)