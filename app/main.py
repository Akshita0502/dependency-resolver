from fastapi  import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.logic import resolve_dependencies_logic #core logic 
from app.models import DependencyInput #import input chema validate incoming request

app = FastAPI(title="Dependency Resolver API")

# CORS
app.add_middleware( # cross origin requests - allows frontend to call backend
    CORSMiddleware,
    allow_origins=["*"], # allow all origin
    allow_credentials=True, # allow cookies 
    allow_methods=["*"], # allow all methods http 
    allow_headers=["*"], # all headers
) 
@app.get("/")
def home():
    return{"message": "dependency resolver api is running."}

@app.post("/resolve") # endpoint resolve
def resolve_dependencies(data: DependencyInput): #data validated 
    result = resolve_dependencies_logic(data.edges) #extract edges and pass to your dfs logic

    if "cycle" in result: # if exists 
        return {
            "status" : "error",
            "cycle": result["cycle"]
        } # return 
    return{
        "status": "success",
        "order":result["order"]  # success case
    }
