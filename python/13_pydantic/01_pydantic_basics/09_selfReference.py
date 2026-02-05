from typing import List,Optional
from pydantic import BaseModel

class Comment(BaseModel):
    id:int
    content: str
    replies: Optional[List['Comment']]= None

Comment.model_rebuild()

comment = Comment(
    id=1,
    content= "Hello there!",
    replies=[
        Comment(id=2,content="hi"),
        Comment(id=3,content="hi there", replies=[
            Comment(id=9,content='hi janu')
        ]),
        Comment(id=4,content="hey"),
        Comment(id=5,content="hola amigo")
    ]
)


print(comment)