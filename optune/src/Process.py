from pydantic import BaseModel

class Process(BaseModel):
    id : int  
    arival_time : float 
    brust_time : float 
    