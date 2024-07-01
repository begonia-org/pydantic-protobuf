
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   example.py
@Time    :   
@Desc    :   
'''



from sqlmodel import SQLModel, Field

import datetime

from sqlmodel import JSON, Column

from sqlmodel import Integer

from enum import Enum

from typing import List, Dict, Any, Optional



class ExampleType(Enum):
    UNKNOWN = 0
    TYPE1 = 1
    TYPE2 = 2
    TYPE3 = 3




class Example(SQLModel,table=True):
    __tablename__="users"
    name: Optional[str] = Field(description="Name of the example",example="'ohn Doe",default="John Doe",alias="full_name",primary_key=True,max_length=128)
    age: Optional[int] = Field(description="Age of the example",example=30,default=30,alias="years")
    emails: Optional[List[str]] = Field(description="Emails of the example")
    entry: Optional[Dict[str,Any]] = Field(description="Properties of the example",sa_column=Column(JSON))
    created_at: datetime.datetime = Field(description="Creation date of the example",default=datetime.datetime.now(),schema_extra={'required': True})
    type: Optional[ExampleType] = Field(description="Type of the example",default=ExampleType.TYPE1)
    score: Optional[float] = Field(description="Score of the example",default=0.0,le=100.0,sa_type=Integer)

