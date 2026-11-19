Fandom Live - Safari 마이크 재구성 버전

이 버전은 SpeechRecognition을 사용하지 않습니다.
브라우저의 getUserMedia + MediaRecorder로 6초 단위 오디오를 녹음하고,
서버가 OpenAI 음성 전사 API(gpt-transcribe)에 전달합니다.

실행 준비(서버/호스팅 환경 필요)
1. Python 3.10+ 설치
2. 이 폴더에서: pip install -r requirements.txt
3. OPENAI_API_KEY 환경변수 설정
   macOS/Linux: export OPENAI_API_KEY="본인_API_키"
   Windows PowerShell: $env:OPENAI_API_KEY="본인_API_키"
4. python server.py 실행
5. 브라우저에서 https://로 배포된 주소 접속

주의
- API 키를 index.html에 넣으면 안 됩니다. 반드시 서버 환경변수로 보관하세요.
- 로컬 테스트는 http://localhost:8000 에서 가능하지만, 아이폰에서 원격 접속할 때는 HTTPS가 필요합니다.
- 음성 오디오 조각이 서버로 전송되어 텍스트로 변환됩니다. 비용이 발생할 수 있습니다.
- 이 패키지는 음성 입력을 교체한 프로토타입입니다. 댓글 생성은 브라우저 내 규칙 기반이며, AI가 즉흥적으로 생성하는 기능은 별도 연결이 필요합니다.
