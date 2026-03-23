Imagen del profiler, si no carga por aca igual voy a subir la imagen dentro de la carpeta
![imagen del profiling](/profiling.png)

El perfil de tiempo muestra que load_playlist tardó 0.004s en total para cargar 100 canciones, donde insert_at_end se tarda 0.003s al ser llamada 100 veces.
En cuanto a memoria, el proceso base ocupa 63.1 MiB y cargar toda la playlist solo agregó 0.1 MiB, lo que demuestra que la estructura de nodos es muy liviana.
Ayuda que las canciones estan almacenadas en un archivo json, que es muy liviano. El resto de operaciones no dejaron huella medible.

El shuffle tiene una complejidad de O(n) únicamente al momento de activarse, ya que recorre todos los nodos de la lista para construir el orden aleatorio. Una vez activado, navegar con next y previous es O(1) porque simplemente se mueve un índice sobre la queue ya generada.

Para poner probar este codigo dentro de otra maquina haz lo siguiente:
1. Clona el repositorio
2. Corre el programa — esto cargará las 100 canciones desde songs.json y ejecutará la demo del playlist player con shuffle.