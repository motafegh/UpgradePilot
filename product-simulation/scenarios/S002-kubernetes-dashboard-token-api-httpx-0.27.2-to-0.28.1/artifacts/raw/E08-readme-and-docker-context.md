# Bounded repository context capture

Frozen head: `391508134b083b8f54461c0b576e8f7985c6ecb4`

Relevant README statements:

- The application can run with `fastapi dev app/main.py`.
- The Docker image is built from the repository Dockerfile.
- TODO: `pytest and ruff should not get installed in container`.

Relevant Dockerfile behavior:

```dockerfile
FROM python:3.13-slim-bullseye
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY . /code
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
```

Direct observation: the shared requirements file, including HTTPX and test tooling, is installed into the production image.
