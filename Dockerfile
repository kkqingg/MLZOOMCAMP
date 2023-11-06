FROM python:3.8.12-slim

RUN pip install pipenv
RUN pip install numpy
RUN pip install scipy

WORKDIR /app                    

COPY ["Pipfile","Pipfile.lock","./"] 

RUN pipenv install --system --deploy

COPY ["load.py","model_C = logisticmodel.bin","./"]

RUN pip install waitress

EXPOSE 9696

ENTRYPOINT ["waitress-serve",  "--host", "0.0.0.0", "--port", "9696", "load:app"]
