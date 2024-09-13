from lxml import etree 
import json


class Element:
    '''
    Wrapper on the etree.Element class.  Extends functionality to output element
    as a dictionary.
    '''

    def __init__(self, element):
        '''
        :param: element a normal etree.Element instance
        '''
        self.element = element

    def toDict(self):
        '''
        Returns the element as a dictionary.  This includes all child elements.
        '''
        rval = {
            self.element.tag: {
                'attributes': dict(self.element.items()),
            },
        }
        for child in self.element:
            rval[self.element.tag].update(Element(child).toDict())
        return rval


class XmlDocument:
    '''
    Wraps lxml to provide:
        - cleaner access to some common lxml.etree functions
        - converter from XML to dict
        - converter from XML to json
    '''
    def __init__(self, xml = '<empty/>', filename=None):
        '''
        There are two ways to initialize the XmlDocument contents:
            - String
            - File

        You don't have to initialize the XmlDocument during instantiation
        though.  You can do it later with the 'set' method.  If you choose to
        initialize later XmlDocument will be initialized with "<empty/>".

        :param: xml Set this argument if you want to parse from a string.
        :param: filename Set this argument if you want to parse from a file.
        '''
        self.set(xml, filename) 

    def set(self, xml=None, filename=None):
        '''
        Use this to set or reset the contents of the XmlDocument.

        :param: xml Set this argument if you want to parse from a string.
        :param: filename Set this argument if you want to parse from a file.
        '''
        if filename is not None:
            self.tree = etree.parse(filename)
            self.root = self.tree.getroot()
        else:
            self.root = etree.fromstring(xml)
            self.tree = etree.ElementTree(self.root)


    def dump(self):
        etree.dump(self.root)

    def getXml(self):
        '''
        return document as a string
        '''
        return etree.tostring(self.root)

    def xpath(self, xpath):
        '''
        Return elements that match the given xpath.

        :param: xpath
        '''
        return self.tree.xpath(xpath);

    def nodes(self):
        '''
        Return all elements
        '''
        return self.root.iter('*')

    def toDict(self):
        '''
        Convert to a python dictionary
        '''
        return Element(self.root).toDict()

    def toJson(self, indent=None):
        '''
        Convert to JSON
        '''
        return json.dumps(self.toDict(), indent=indent)
    
    @staticmethod
    def remove_namespace(xml: etree.XMLSchema):
        for elem in xml.getiterator():
            # Remove the namespace by splitting on } and keeping the part after
            if '}' in elem.tag:
                elem.tag = elem.tag.split('}', 1)[1]
        return xml

    @classmethod
    def toDictStatic(cls, xml):
        '''
        Convert to Dict static
        '''        
        root = etree.fromstring(xml)


        return Element(root).toDict()

