from pydantic import BaseModel, ConfigDict


class Base(BaseModel):
    """Base class for all schemas."""

    model_config = ConfigDict(extra="ignore", from_attributes=True)