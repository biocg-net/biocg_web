FROM ghcr.io/astral-sh/uv:alpine

WORKDIR /biocg_web
COPY pyproject.toml .
COPY README.md .
COPY src ./src
RUN ls -la .

# ENTRYPOINT ["tail", "-f", "/dev/null"]
CMD ["uv", "run", "-p", "3.13", "fastapi", "run", "-e", "biocg_web.app:app", "--proxy-headers", "--port", "8080"]
