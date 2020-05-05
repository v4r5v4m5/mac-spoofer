#! /usr/bin/env python
# [SHAMSI9] - MAC HACKER - TEAM INDIANSERVERS
# QUERIES: | shamsi9@protonmail.com | https://github.com/shamsi9 |

import subprocess
import optparse
import re

def script_intro():
    print("                                    █")
    print("                                  ▄█")
    print("            █                   ▓█▌")
    print("             █▓▄▄▄▓▓▓██████▓▓▄▄▓█")
    print("              ████▀           ▓███▓ ")
    print("            ▓█▓██▌            ██▌▀███▄")
    print("           █▌   ██            █▌   ▀███")
    print("         ▓█▀     ██          █▌    ▐ ▓██▄")
    print("        ▓█▀       █▌        █▌     ▐  ▓██▄")
    print("        ██        ▀█       ██         ▐███")
    print("       ▐██         █▌     ▓█           ███")
    print("        ██▌        ██     █▌          ▐███")
    print("        ▐██▌        █▓   ██           ▓██▌")
    print("          ███       ██  ██▀          ▓██")
    print("           ▀██▓      ██▐██         ▄███")
    print("             ████▄   ████        ▄███▀")
    print("                ▀██▓▄████▌   ▄▓████▀▀")
    print("                 ▓▀███████████▓▀▀   ")
    print("                     ███▀")
    print("                      ██")
    print("                                      ")
    print("          M A C  A D D R E S S  S P O O F E R")
    print("                       B Y  ")
    print("           V Jayavamsi (＠ S H Λ M S I ９)")
    print("                        &")
    print("    ░  T Ξ Λ M ＠I N D I Λ N S Ξ R V Ξ R S ░")
    print("                                                    ")
    print("         https://www.github.com/shamsi9")
    print("                                                          ")

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help=" Target interface to change")
    parser.add_option("-m", "--mac", dest="new_mac", help=" New MAC address")
    return  parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify proper interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify proper MAC , use --help for more info.")
        return options

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] MAC address not found for " + options.interface + " interface")
        print("[-] Perform -h | --help for usage and options")

script_intro()
(options, arguments) = get_arguments()
current_mac = get_current_mac(options.interface)
print("[+] Getting your MAC address")
print("[+] Current MAC address > " + str(current_mac))
change_mac(options.interface, options.new_mac)
current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC address was successfully spoofed to " + current_mac)
    print("[+] Current MAC address > " + str(current_mac))
    print("[+] Script executed successfully")
else:
    print("[-] MAC address did not changed")
    print("[-] Script terminated, use --help for more info.")

