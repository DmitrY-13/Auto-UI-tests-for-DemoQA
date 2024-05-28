from pydantic import BaseModel, Field

from data.fake import fake


class PersonData(BaseModel):
    name: str = Field(default_factory=fake.name)
    email: str = Field(default_factory=fake.email)
    current_address: str = Field(default_factory=fake.address)
    permanent_address: str = Field(default_factory=fake.address)
