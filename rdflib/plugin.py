_kinds = {}

def register(name, kind, module_path, class_name):
    _module_info = _kinds.get(kind, None)
    if _module_info is None:
        _module_info = _kinds[kind] = {}
    _module_info[name] = (module_path, class_name)

def get(name, kind):
    _module_info = _kinds.get(kind)
    module_path, class_name = _module_info[name]
    module = __import__(module_path, globals(), locals(), True)
    return getattr(module, class_name)
    

register('xml', 'serializer',
         'rdflib.syntax.serializers.XMLSerializer', 'XMLSerializer')

register('pretty-xml', 'serializer',
         'rdflib.syntax.serializers.PrettyXMLSerializer', 'PrettyXMLSerializer')

register('nt', 'serializer',
         'rdflib.syntax.serializers.NTSerializer', 'NTSerializer')

register('xml', 'parser',
         'rdflib.syntax.parsers.RDFXMLParser', 'RDFXMLParser')

register('nt', 'parser',
         'rdflib.syntax.parsers.NTParser', 'NTParser')

register('default', 'backend',
         'rdflib.backends.IOMemory', 'IOMemory')

register('IOMemory', 'backend',
         'rdflib.backends.IOMemory', 'IOMemory')

register('Memory', 'backend',
         'rdflib.backends.Memory', 'Memory')

register('Sleepycat', 'backend',
         'rdflib.backends.SleepyCat', 'SleepyCat')

register('ZODB', 'backend',
         'rdflib.backends.ZODB', 'ZODB')