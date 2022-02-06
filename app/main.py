from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.core import auth, db, init_app
from app.routes import router as root_router
from app.routes.v1 import router as v1_router

app = FastAPI()

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event('startup')
async def startup():
    await db.boot(app)
    await init_app.init_repositories(app)
    await init_app.init_controllers(app)

app.include_router(auth.router)
app.include_router(root_router.router)
app.include_router(v1_router.router, prefix="/v1")

# @app.post("/v1/alarm/test", response_model=bool)
# def create_alarm_config(
#     config: schemas.AlarmConfigBase
# ):
#     complete_config = schemas.AlarmConfig(**config.dict(), id=randint(0,100), timestamp=datetime.datetime.now())
#     print(complete_config)
#     return crud.create_alarm_config(db=app.db, alarm_config=complete_config)

