from fastapi import FastAPI
from TodoApp import models
from TodoApp.database import engine
from TodoApp.routers import auth, todos, admin, users

app = FastAPI()

# ✅ Safe DB initialization
try:
    if engine:
        models.Base.metadata.create_all(bind=engine)
except Exception as e:
    print("DB connection failed:", e)

# ✅ Root endpoint (important for testing)
@app.get("/")
def root():
    return {"message": "API is running"}

# ✅ Routers
app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)