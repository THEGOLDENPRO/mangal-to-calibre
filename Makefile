build:
	cp main.py manga
	chmod +x ./manga

install:
	cp ./manga ~/.local/bin

uninstall:
	rm ~/.local/bin/manga

clean:
	rm ./manga