El script en python realiza web scraping en la pagina de Google trends en la sección de 
tecnología en tiempo real y genera un archivo json llamado data.json que recibe las tendencias
que se encuentren en la primera pagina de 
"https://trends.google.com/trends/trendingsearches/realtime?geo=US&hl=en-US&category=t"
con un maximo de 20.

Para correr el programa se necesitan de los paquetes de:
Selenium
Pandas

Tambien se requiere de internet y se configuro selenium con Google Chrome por eso
se necesita Chrome.


Solo se requiere correr el script en la terminal y para concluirlo Ctrl + C.
Para ver la información actualizarse abrir el archivo generado data.json.


Notas: De vez en cuando bloquea la solicitud pero con otro intento vuelve a funcionar 
por ello recomieno bajar el tiempo de 60 segundos a 10 para probar rapido que funciona,
Los datos del archivo json generado se presentan en orden descendente por lo que la 
información mas reciente se encuentra hasta arriba.
El programa se encuentra en bucle infinito para terminarlo Ctrl + C en la terminal.


 