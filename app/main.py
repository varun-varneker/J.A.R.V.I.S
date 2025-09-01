from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI()

# Enable CORS (important if you're calling from frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to specific domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check route
@app.get("/")
async def root():
    return {"message": "J.A.R.V.I.S API is running!"}


# SPEECH-TO-TEXT ENDPOINT
@app.post("/stt")
async def speech_to_text(audio: UploadFile = File(...)):
    """
    Receives audio file (blob) from frontend and returns transcribed text.
    """
    contents = await audio.read()
    # TODO: Integrate your Speech-to-Text engine here (e.g., Whisper, Google, AssemblyAI)
    # Example placeholder transcription:
    transcription = "This is a sample transcription"
    return {"text": transcription}


# CHAT ENDPOINT
@app.post("/chat")
async def chat(request: Request):
    """
    Receives a JSON payload with 'message' key and returns chatbot response.
    """
    try:
        body = await request.json()
        user_message = body.get("message", "")

        # TODO: Integrate your chatbot logic here (e.g., OpenAI API, Rasa, custom model)
        # Example placeholder response:
        bot_response = f"You said: {user_message}"

        return {"response": bot_response}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)
