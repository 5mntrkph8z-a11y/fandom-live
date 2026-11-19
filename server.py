import os
from pathlib import Path
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from openai import OpenAI

BASE = Path(__file__).parent
app = FastAPI()
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@app.get("/")
async def home():
    return FileResponse(BASE / "index.html")

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    if not os.environ.get("OPENAI_API_KEY"):
        raise HTTPException(status_code=503, detail="서버에 OPENAI_API_KEY가 설정되지 않았어.")
    data = await file.read()
    if not data:
        return {"text": ""}
    suffix = ".mp4" if "mp4" in (file.content_type or "") or (file.filename or "").endswith(".mp4") else ".webm"
    try:
        # SDK는 파일명과 MIME 정보를 이용해 오디오 형식을 판별해.
        result = client.audio.transcriptions.create(
            model="gpt-transcribe",
            file=(f"audio{suffix}", data, file.content_type or "application/octet-stream"),
            prompt="한국어 대화의 자연스러운 받아쓰기. 영어, 일본어, 중국어가 섞일 수 있음."
        )
        return {"text": result.text}
    except Exception as exc:
        raise HTTPException(status_code=502, detail=f"음성 변환 실패: {str(exc)[:240]}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", "8000")))
