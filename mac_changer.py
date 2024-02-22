#!/usr/bin/env python

import subprocess
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    return parser.parse_args()

def mac_change(interface, new_mac):
    print("[+] Changing MAC Address for", interface, "to", new_mac)
    subprocess.call(["ip", "link", "set", interface, "down"])
    subprocess.call(["ip", "link", "set", interface, "address", new_mac])
    subprocess.call(["ip", "link", "set", interface, "up"])



(options, arguments) = get_arguments()
mac_change(options.interface, options.new_mac)
