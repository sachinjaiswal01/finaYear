from fastapi.middleware.cors import CORSMiddleware # type: ignore
from fastapi import FastAPI    
from pydantic import BaseModel
from googletrans import Translator


# Initialize FastAPI app and Translator
app = FastAPI()
translator = Translator()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Replace with your frontend's origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model for translation request
class TranslationRequest(BaseModel):
    text: str
    src_lang: str
    dest_lang: str

# Translation endpoint
@app.post("/translate/")
async def translate(request: TranslationRequest):
    translated = translator.translate(request.text, src=request.src_lang, dest=request.dest_lang)
    return {"translated": translated.text}

# To run the server: uvicorn backend.main:app --reload
