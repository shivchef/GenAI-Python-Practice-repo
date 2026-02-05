from typing import Optional
from pydantic import BaseModel, Field


class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Employee name",
        examples="Shivendra"

    )

    department: Optional[str] ="General"
    salary: float = Field(
        ...,
        ge=10000,
        description="Annual salary in Rupees"   
    )

class User(BaseModel):
    email: str = Field(
        ...,
        regex=r""


    )
    phone: str = Field(
        ...,
        regex = r''

    )
    age: int = Field(
        ...,
        ge=0,
        le=100,
        description="Age in years"
    )
    discount: float = Field(
        ...,
        ge=0,
        le=100,
        description="Discount percentage"
    )
