from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.routers import router


# Middlewares 

from starlette.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
]


# Jobs

from src.jobs.job_ping.job import init_cron_ping
from src.jobs.job_get_data.job  import init_job_get_data

@asynccontextmanager
async def lifespan(app: FastAPI):
    JOB_PING_INSTANCE = init_cron_ping()
    JOB_GET_DATA_INSTANCE = init_job_get_data()

    print('Starting jobs...')
    JOB_PING_INSTANCE.start()
    JOB_GET_DATA_INSTANCE.start()

    yield

    print('Stopping jobs...')
    JOB_PING_INSTANCE.shutdown()
    JOB_GET_DATA_INSTANCE.shutdown()



# App

app = FastAPI(
    title="Template API generada desarrollo Ecadem",
    description="Este template se genera como base del desarrollo de apis en el equipo de ecadem",
    version = "1.0",
    openapi_url="/openapi.json", 
    docs_url="/docs",
    middleware=middleware,
    lifespan=lifespan
)

app.include_router(router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, port=8000, host='0.0.0.0')
