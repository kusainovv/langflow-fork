FROM langflowai/langflow-backend as backend_build
WORKDIR /app

RUN apt-get update && apt-get install git -y

COPY --from=backend_build /app/dist/*.whl /app/
RUN pip install langflow-*.whl
RUN rm *.whl

EXPOSE 80

CMD [ "uvicorn", "--host", "0.0.0.0", "--port", "7860", "--factory", "langflow.main:create_app" ]