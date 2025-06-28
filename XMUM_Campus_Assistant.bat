@echo off
echo Starting Campus Assistant...
echo.

echo [1/4] Installing backend dependencies...
cd py_code
pip install flask flask-cors joblib spacy thinc pandas scikit-learn vaderSentiment tqdm ollama > nul 2>&1

echo [2/4] Starting backend service...
start "Campus Assistant-Backend" cmd /k "python app.py"

cd ..

echo [3/4] Installing frontend dependencies...
cd frontend
call npm install > nul 2>&1

echo [4/4] Starting frontend service...
start "Campus Assistant-Frontend" cmd /k "npm run dev"

echo.
echo Application started!
echo Frontend address: http://localhost:5173
echo Backend address: http://localhost:5000

echo.
echo Opening frontend in default browser...
start http://localhost:5173

echo.
echo Press any key to close this window...
pause > nul
