#!/usr/bin/python3
""" fonction de sérialisation et déséralisation en utilisant XML comme
format alternatif à JSON
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    home = ET.Element("data")
    for key, value in dictionary.items():
        bor = ET.SubElement(home, key)
        bor.text = str(value)

    tree = ET.ElementTree(home)
