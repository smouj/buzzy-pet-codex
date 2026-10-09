# Prompt de instalación

Copia este bloque en una conversación con un agente que tenga la integración Pets:

```text
Instala y activa Buzzy desde https://github.com/smouj/buzzy-pet-codex.

Lee primero README.md, docs/INSTALL.md, docs/FORMAT.md y
THIRD_PARTY_NOTICES.md. Es una mascota existente en formato v1,
con nueve estados. No regeneres el arte, no modifiques los archivos
y no afirmes que tiene miradas hacia el cursor.

Comprueba que tienes las herramientas Pets para validar, preparar la
subida, crear, seleccionar y listar mascotas. Si faltan, explica qué
integración falta y detente antes de intentar activarla. No modifiques
archivos internos de la aplicación ni inventes opciones de configuración.

Lista mis mascotas existentes. Reutiliza una instalación de Buzzy si
puedes verificar su identidad y que corresponde a este archivo, usando
un ID estable conocido y su hash cuando sea posible. No basta con que
coincida el nombre. Tras un timeout, verifica el resultado antes de
crear otra mascota.

Descarga el PNG de esta release en un directorio local de trabajo:
https://github.com/smouj/buzzy-pet-codex/releases/download/v1.0.1/buzzy-mascota.png
Comprueba su SHA-256:
425476ee25c31a83597ffc9ba3485ddaa0859a8124067e0787ee34c674ed4143

Valida la ruta local absoluta con validate_pet_spritesheet. Exige
valid=true, sprite_version=1, dimensiones 1536x1872 y fotogramas
[6,8,8,4,5,8,6,6,6]. Muestra el GIF de todos los estados antes de subirlo.

Llama a prepare_pet_upload con ese PNG exacto. El host lo transfiere
automáticamente. Usa upload.upload_session_id en create_pet, nombre
Buzzy y descripción "Adaptación fan animada del asesor de Theme Park
World, con fondo transparente." Reintenta fallos transitorios con la
misma sesión, nombre y descripción; prepara otra sesión solo si hace falta.

Guarda el pet.id estable en un registro local, sin credenciales, sesiones
de subida ni enlaces firmados. Actívalo con select_pet, comprueba que
active_pet_id coincide y pagina list_pets hasta verlo como mascota
personalizada activa. Confirma la instalación solo tras verificarlo;
si falla, explica el bloqueo concreto y qué pasos se han completado.
```
