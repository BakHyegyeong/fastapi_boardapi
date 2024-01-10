from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles

from domain.question import question_router
from domain.answer import answer_router
from domain.user import user_router
from domain.sympton import sympton_router
from domain.diary import diary_router
from domain.physicalpain import physicalpain_router
from domain.imdiary import imdiary_router

app = FastAPI()

origins = [
    "http://localhost:5173",    # 또는 "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(question_router.router)
app.include_router(answer_router.router)
app.include_router(user_router.router)
app.include_router(sympton_router.router)
app.include_router(diary_router.router)
app.include_router(physicalpain_router.router)
app.include_router(imdiary_router.router)

app.mount("/assets", StaticFiles(directory="frontend/dist/assets"))

# @app.get("/")
# def index():
#     return FileResponse("frontend/dist/index.html")

# app.mount("/images",StaticFiles(directory="/home/ubuntu/projects/boardapi/domain/imdiary/images"))

app.mount("/Math_TemplateData",StaticFiles(directory="unity_webGL/MathGame/Math_TemplateData"))
app.mount("/Math_Build",StaticFiles(directory="unity_webGL/MathGame/Math_Build"))

app.mount("/Array_TemplateData",StaticFiles(directory="unity_webGL/ArrayGame/Array_TemplateData"))
app.mount("/Array_Build",StaticFiles(directory="unity_webGL/ArrayGame/Array_Build"))

app.mount("/Card_TemplateData",StaticFiles(directory="unity_webGL/CardGame/Card_TemplateData"))
app.mount("/Card_Build",StaticFiles(directory="unity_webGL/CardGame/Card_Build"))


@app.get("/unity_math")
def index():
	return FileResponse("unity_webGL/MathGame/index.html")

@app.get("/unity_array")
def index():
	return FileResponse("unity_webGL/ArrayGame/index.html")

@app.get("/unity_card")
def index():
	return FileResponse("unity_webGL/CardGame/index.html")
