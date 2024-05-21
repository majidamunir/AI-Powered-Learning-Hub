build:
	docker build -t myproject .

run:
	docker run -d -p 8000:8000 myproject 

