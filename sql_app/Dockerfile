FROM python:latest

RUN mkdir -p /app/

COPY . /app/
WORKDIR /app/

RUN pip -V

RUN pip install -r requirements.txt

ENV TZ Europe/Moscow

# WORKDIR /app/my_super_project/sql_app/

RUN alembic init alembic
RUN alembic revision --autogenerate
RUN alembic upgrade head

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]