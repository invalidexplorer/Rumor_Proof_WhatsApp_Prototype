
class Block: 
    def __init__(self,sender, reciever):
        self.sender = sender
        self.reciever = reciever
        self.next = None
    
    def __str__(self):
        return f'Sender: {self.sender} Reciever: {self.reciever}'
    

class Message_link:
    def __init__(self,messageID):
        self.head = None
        self.messageID = messageID
    def __str__(self):
        return f'Message: {self.messageID}'
    

class Message_Chain():
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __str__(self):
        return f'Message chain: {self.message_chain}'
    
    def __init__(self, msg, sender, reciever):
        x = Message_link(msg)
        x.head = Block(sender, reciever)
        self.message_chain =[x]
    
    def msg_flag(self, msg, reciever):
        #dummy function for prototyping 
        return None
    
    def add_message_link(self, msg, sender, reciever):
        for i in range(len(self.message_chain)):
            if self.message_chain[i].messageID == msg:
                itr = self.message_chain[i].head
                count = 0
                while itr.next!= None:
                    itr = itr.next
                    count = count + 1
                itr.next = Block(sender,reciever)
                
                if count>400:
                    msg_flag(msg, reciever)        
            else:
                x = Message_link(msg)
                x.head = Block(sender, reciever)
                self.message_chain.append(x)
                    
    
    
if __name__ == '__main__':
            
    dd = Message_Chain('x hai', 914, 332)

    dd.add_message_link('x hai', 432, 331)

    dd.add_message_link('x hai', 33, 331)

    dd.add_message_link('x nahi hai', 4312, 331)

    dd.add_message_link('x hai', 432, 3331)

    dd.add_message_link('x nahi hai', 3722, 9393)

    itr = dd.message_chain[1].head 
    while  itr != None:
        print(itr)
        itr = itr.next
    
        

    
    
        
    
    