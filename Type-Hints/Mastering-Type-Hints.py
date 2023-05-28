# This file is the program
from typing import List, Tuple, Dict, Any, Union
age: int = 30
def greet(name: str) -> str:
    return "Hello, " + name

from typing import Optional

def find_user(user_id: int) -> Optional[str]:
    # Implementation here
    # Return a username or None if not found

from typing import List, Tuple, Dict

def process_data(data: List[int]) -> Tuple[str, Dict[str, int]]:
    # Implementation here

class User:
    # Class implementation

def get_users() -> List[User]:
    # Implementation here

from typing import Callable

def apply(func: Callable[[int, int], int], x: int, y: int) -> int:
    return func(x, y)

from typing import List

UserList = List[str]

def get_usernames() -> UserList:
    # Implementation here

from typing import NewType

UserId = NewType("UserId", int)

def get_user(user_id: UserId) -> str:
    # Implementation here
