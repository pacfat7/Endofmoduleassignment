import pickle
import json
from dict2xml import dict2xml
import xmltodict
import yaml

class DataHelper:
    @staticmethod
    def dict_to_binary_bytes(data):
        serialized_data = pickle.dumps(data)
        return serialized_data
    
    @staticmethod
    def dict_to_json_bytes(data):
        serialized_str = json.dumps(data)
        serialized_data = serialized_str.encode('utf-8')
        return serialized_data
    
    @staticmethod
    def dict_to_xml_bytes(data):
        serialized_str = dict2xml(data, wrap='dictionary', newlines=False)
        serialized_data = serialized_str.encode('utf-8')
        return serialized_data
    
    @staticmethod
    def binary_bytes_to_dict(serialized_data):
        data = pickle.loads(serialized_data)
        return data
    
    @staticmethod
    def json_bytes_to_dict(serialized_data):
        data = json.loads(serialized_data)
        return data
    
    @staticmethod
    def xml_bytes_to_dict(serialized_data):
        serialized_str = serialized_data.decode('utf-8')
        data = xmltodict.parse(serialized_str)
        return data
    
    @staticmethod
    def binary_bytes_to_str(serialized_data):
        data = DataHelper.binary_bytes_to_dict(serialized_data)
        str = yaml.dump(data)
        return str
    
    @staticmethod
    def json_bytes_to_str(serialized_data):
        data = DataHelper.json_bytes_to_dict(serialized_data)
        str = json.dumps(data)
        return str
    
    @staticmethod
    def xml_bytes_to_str(serialized_data):
        data = DataHelper.xml_bytes_to_dict(serialized_data)
        str = dict2xml(data, newlines=False)
        return str
