pip3 install fastapi
pip3 install unicorn[standard]
pip3 install sqlalchemy
pip3 install databases
pip3 install "databases[postgresql]"
pip3 install psycopg2-binary   
pip3 install pydantic[email]
pip3 install passlib
pip3 install bcrypt
pip3 install python-jose

docker run --name habr-pg-13.3 -p 5432:5432 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=fast_api -d postgres:13.3

# container stop
docker container stop SOMENAME

# container removal
docker rm -f SOMENAME

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



INSERT INTO users
VALUES (2, 'mishka123@mail.ru', 'Mishka', 'base64', True, '2022-08-06 15:15:20.804', '2022-08-06 15:15:20.804');

SELECT * FROM users;