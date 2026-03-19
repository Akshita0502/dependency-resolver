from pydantic import BaseModel  # validate input and parse json to python object
from typing import List  # list of edges
class DependencyInput(BaseModel): # schema data model defines what input the api expects 
    edges: List[List[str]]