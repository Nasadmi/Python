# Python
Este archivo "calc.py" es un archivo que nos servira para hacer operaciones simples desde un terminal GNU-Linux, en cualquier distribucion.
Su metodo de instalacion es el siguiente.
1)Clonamos el repositorio con git o Descargar el archivo.py
2)Abrimos una terminal y colocamos "su" en el caso que no tengas password colorca "sudo passwd root"
3)Abrimos una terminal y movemos el archivo.py a la carpeta /usr/bin con ayuda del comando mv y usando como cuenta root.Algo asi "# mv archivo.py /usr/bin"
4)Metemos en otra terminal el siguiente comando "sudo nano .bashrc"
5)Al final del archivo despes de fi colocamos lo siguiente 
"
fi
#Mis comandos 
alias calcy="python3 /usr/bin/archivo.py"
"
6) Guardamos con Ctrl + O y cerramos nano con Ctrl + X
7) Abrimos una terminal y colocamos lo siguiente "source .bashrc"
8) Y ponemos en la terminal calcy
Y listo
