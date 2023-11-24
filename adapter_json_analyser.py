'''
What is implemented :
There is a analytics tool which only analyse JSON data.
But our system has XML and we don't our client to get to know that we have xml, and our analytics 
tool only analyses json.
So, adapter design pattern will be useful in this case, where adapter class takes xml object and it 
inherits the tool and in analyse common method, we can convert form xml to json and then call analyse 
of the tool class.
'''

class XmlData:
    def __init__(self,xml_data):
        self.xml_data = xml_data
    
    def get_xml_data(self):
        return self.xml_data

class Tool:
    def analyse(self,json_data):
        print("Analaysed json data =>",json_data)

class Adapter(Tool):
    def __init__(self,xml_data_object):
        self.xml_data_object = xml_data_object
        
    def analyse(self):
        # converting xml to json here
        json_data = f"Converted {self.xml_data_object.get_xml_data()} to json data"
        super().analyse(json_data)
        
class Client:
    def __init__(self,tool):
        self.tool = tool
    def analyse_my_data(self):
        self.tool.analyse()

if __name__ == "__main__":
    xml_data = XmlData("I am XML data")
    adapter = Adapter(xml_data)
    client = Client(adapter)
    client.analyse_my_data()    