FROM python:3.12.3-bullseye

COPY . ./app/

WORKDIR /app

RUN python -m venv ./.venv

RUN . ./.venv/bin/activate

RUN pip install -r requirements/backend.txt

CMD ["uvicorn", "spaceship.main:app", "--host=0.0.0.0", "--port=8080"]
