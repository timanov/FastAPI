pip3 install fastapi
pip3 install unicorn[standard]
pip3 install sqlalchemy
pip3 install databases
pip3 install "databases[postgresql]"
pip3 install psycopg2-binary   

 uvicorn main:app --reload
 python3 -m uvicorn main:app --reload

 BD: Postgres

http://localhost:8000/docs - документация open API (Swagger), стандарт документации к API, является стандартом отрасли

Если мы создаем какую-то апишку, то ожидается, что мы предоставим к ней документацию в подобном виде, передадим его фронтендеру и он будет создавать по этим запросом интерфейс, будет видеть, какие запросы.


BD: Postgres


Директории в root директории:
core - настройка приложения
db -
endpoints - handler'ы нашего приложения
models - способ описания данных, описание данных для отображения сущностей, получение данных от сущностей и хранение в базе данных.
repository - паттерн, срок абстрации, инкапсулирующий в себе все, что относится к способу хранения данных. 

