from piccolo.table import Table
from piccolo.columns.column_types import Varchar, BigInt, Text


class Message(Table):
    user_id = BigInt()
    user_first_name = Varchar(length=50) 
    user_last_name = Varchar(length=50)
    text = Text()
