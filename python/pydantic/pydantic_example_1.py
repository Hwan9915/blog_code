from datetime import datetime
from pydantic import BaseModel, PositiveInt


class User(BaseModel):
    id: int  # id는 int값을 가져야 함
    signup_ts: datetime | None  # signup_ts는 datetime 또는 None을 가져야 함
    tastes: dict[str, PositiveInt]  # key는 str, value는 PositiveInt를 가져야 함

external_data = {
    'id': 123,
    'signup_ts': '2019-06-01 12:22',  
    'tastes': {
        'wine': 9,
        'cabbage': '1',
    },
}

user = User(**external_data)

print(user)