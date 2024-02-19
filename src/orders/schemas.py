from datetime import datetime

from pydantic import BaseModel
from typing import List, Dict


class OrderCreate(BaseModel):
    data_orders: List[Dict]
    id_user: int
    timestamp: datetime
