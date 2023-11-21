from abc import ABC,abstractmethod

class ISlaves:
    def update_db(self,value,is_add):
        if is_add:
            self.db_values.append(value)
        else:
            self.db_values.remove(value)

class SlaveOne(ISlaves):
    def __init__(self,db_values) -> None:
        self.db_values = db_values
    def update_db(self,value,is_add):
        super().update_db(value,is_add)
        print("Slave one list is",self.db_values)
        
class SlaveTwo(ISlaves):
    def __init__(self,db_values) -> None:
        self.db_values = db_values
    def update_db(self,value,is_add):
        super().update_db(value,is_add)
        print("Slave two list is",self.db_values)

class MasterParent:
    def __init__(self,set_of_slaves,db_values) -> None:
        self.set_of_slaves = set_of_slaves
        self.db_values = db_values
    def add_slave(self,slave):
        self.set_of_slaves.add(slave)
    def remove_slave(self,slave):
        self.set_of_slaves.remove(slave)
    def broadcast(self,value,is_add):
        if is_add:
            for slave in self.set_of_slaves:
                slave.update_db(value,True)
        else:
            for slave in self.set_of_slaves:
                slave.update_db(value,False)

class Master(MasterParent):
    def __init__(self, set_of_slaves, db_values) -> None:
        super().__init__(set_of_slaves, db_values)
    
    def add_value(self,value):
        self.db_values.append(value)
        super().broadcast(value,True)
        print("Master list is",self.db_values)
        
    def remove_value(self,value):
        if value in self.db_values:
            self.db_values.remove(value)
            super().broadcast(value,False)            

        print("Master list is",self.db_values)
        
if __name__ == "__main__":
    master = Master(set(),[])
    master.add_slave(SlaveOne([]))
    master.add_slave(SlaveTwo([]))
    
    for value in range(1,5):
        master.add_value(value)
    
    master.remove_value(4)

    
        
    