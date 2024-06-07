#!/usr/bin/env python3
"""Serializing and Deserializing with XML"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """This will take a Python dictionary
    and a filename as parameters."""
    root = ET.Element('data')

    for key, value in dictionary_items():
        child = ET.Element(key)
        child.text = str(value)
        root.append(child)

    tree = ET.ElementTree(root)

    tree.write(filename, encoding='utf-8', xml_declaration=True)

def deserialize_from_xml(filename):
    """Parse the XML file"""
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    data_dict = {}
    for child in root:
        data_dict[child.tag] = child.text

    return data_dict
    
