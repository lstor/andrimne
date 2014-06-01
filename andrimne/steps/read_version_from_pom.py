import andrimne.config as config
import logging
import xml.etree.ElementTree as ElementTree

### WARNING
#
# This step uses the Python module xml.etree.ElementTree, which is vulnerable to maliciously constructed data.
# If you do not have full control over your XML file, *do not* use this step!


def run():
    logging.info('reading version from pom')

    namespace = config.read_or_default('maven_pom_namespace', '')
    version_tag_name = config.read_or_default('version_tag_name', 'version')
    pom_file = config.read_or_default('main_pom', 'pom.xml')

    try:
        find_and_store_version(version_tag_name, namespace, pom_file)
    except (IOError, ElementTree.ParseError) as e:
        logging.error('could not read version: {}'.format(e))


def find_and_store_version(version_tag_name, namespace, pom_file):
    version_tag = '{{{0}}}{1}'.format(namespace, version_tag_name)

    root = ElementTree.parse(pom_file).getroot()
    if root.tag == version_tag:
        return root.text

    version = root.findtext(version_tag)
    assert version is not None
    config.store['version'] = version
