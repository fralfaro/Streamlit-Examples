# Aloja tu aplicación de Streamlit de forma gratuita


![](https://blog.streamlit.io/content/images/2022/08/image--4-.svg)

> **Nota**: El artículo original en inglés se encuentra disponible en [Host your Streamlit app for free](https://blog.streamlit.io/host-your-streamlit-app-for-free/#:~:text=Connect%20your%20account%20to%20GitHub,-There%20are%20two&text=On%20the%20authorization%20page%2C%20click%20on%20%E2%80%9CAuthorize%20streamlit.%22&text=This%20will%20let%20Community%20Cloud,%2C%20click%20%E2%80%9CAuthorize%20streamlit.%22&text=Now%20you're%20ready%20to%20deploy%20Streamlit%20apps!).

Si tienes una aplicación de Streamlit pero no deseas pagar una tarifa mensual para
alojarla en una plataforma de nube comercial, una opción es migrarla a 
[Streamlit Community Cloud](https://streamlit.io/cloud). ¡Es GRATIS!

En esta publicación, te mostraré cómo construir una aplicación de demostración y desplegarla en Community Cloud paso a paso:

*   Paso 1. Crea una aplicación simple de Streamlit
*   Paso 2. Configura una cuenta en Community Cloud
*   Paso 3. Conecta tu cuenta a GitHub
*   Paso 4. Crea un repositorio GitHub para tu aplicación
*   Paso 5. Despliega tu aplicación en unos pocos clics

¿No puedes esperar para verlo en acción? Aquí tienes
la [aplicación de demostración](https://coding-hello.streamlit.app/?ref=blog.streamlit.io)
y el [código del repositorio](https://github.com/coding-professor/st-hello-world/tree/main?ref=blog.streamlit.io).


### Por qué desplegar tus aplicaciones en internet

Desplegar tus aplicaciones en internet permite que los usuarios accedan a ellas desde un navegador web, sin tener que configurar un entorno de programación ni instalar dependencias.

Tienes dos opciones:

1. Configurar manualmente un servidor privado virtual para desplegar tu aplicación.
2. Alojar la aplicación en un repositorio de GitHub y desplegarlo en una plataforma de nube.

![](https://blog.streamlit.io/content/images/2022/08/E55BB258-DA30-4262-BDAA-7B2C6A0E5E15.jpeg)

La primera opción te brinda control total. Puedes configurar todo localmente. Sin embargo, puede llevar tiempo, tanto para la configuración como para el mantenimiento (como mantener actualizado el sistema operativo, etc.).

La segunda opción es la más sencilla. Simplemente sube tu aplicación a GitHub. Si está configurada correctamente con una plataforma en la nube, se actualizará automáticamente cuando hagas cambios en el código.

### Por qué usar Community Cloud

Aquí tienes por qué podrías querer usar Community Cloud para alojar tus aplicaciones:

|                Ventajas                |                                       Descripción                                      |
|:--------------------------------------:|:--------------------------------------------------------------------------------------:|
| Gratis                                 | ¡Puedes desplegar aplicaciones de Streamlit de forma gratuita!                         |
| Despliegue en un clic                  | Tu aplicación completamente alojada está lista para compartirse en menos de un minuto. |
| Mantén tu código en tu repositorio     | Sin cambios en tu proceso de desarrollo. Tu código permanece en GitHub.                |
| Actualizaciones en vivo                | Tus aplicaciones se actualizan al instante cuando realizas cambios en el código.       |
| Conexión segura a datos                | Conéctate a todas tus fuentes de datos utilizando protocolos seguros.                  |
| Restringe el acceso a aplicaciones     | Autentica a los espectadores con listas de permisos por aplicación.                    |
| Administra fácilmente tus aplicaciones | Visualiza, colabora y administra todas tus aplicaciones en un solo lugar.              |



### Paso 1. Crea una aplicación simple de Streamlit

Primero, creemos una aplicación sencilla que imprima `¡Hola mundo!`. Solo se necesitan dos líneas de código (para profundizar, lee [este artículo](https://blog.streamlit.io/how-to-master-streamlit-for-data-science/)).

Crea un archivo `streamlit_app.py`:

```python
import streamlit as st

st.write('¡Hola mundo!')
```

### Paso 2. Configura una cuenta en Community Cloud

Ve a [Community Cloud](https://streamlit.io/cloud?ref=blog.streamlit.io) y haz clic en "Registrarse" para crear una cuenta gratuita con tu cuenta existente de Google, GitHub o correo electrónico:

![Registrarse en Community Cloud](https://blog.streamlit.io/content/images/2022/08/324BEA1A-997C-49E7-A279-040300162E27.jpeg#browser)

Luego, ingresa tus credenciales de GitHub y haz clic en "Autorizar streamlit" para permitir que Streamlit acceda a tu cuenta de GitHub:

![Autorizar streamlit en GitHub](https://blog.streamlit.io/content/images/2022/08/40F6254E-3523-4ADE-B9B6-D4436FE8B68A.jpeg#browser)

Finalmente, ingresa tu información y haz clic en "Continuar":

![Ingresar información en Community Cloud](https://blog.streamlit.io/content/images/2022/08/2B353264-DDBA-4251-94E4-7CF77A256B9B.jpeg#browser)

¡Felicitaciones! Te has registrado en tu espacio de trabajo en Community Cloud.

### Paso 3. Conecta tu cuenta a GitHub

Hay dos opciones para conectar tu cuenta de Community Cloud a GitHub:

**Opción 1**

Haz clic en "Nueva aplicación":

![Nueva aplicación en Community Cloud](https://blog.streamlit.io/content/images/2022/08/6FD187E5-2A74-4205-97B9-E19890E6C741.jpeg#browser)

En la página de autorización, haz clic en "Autorizar streamlit".

**Opción 2**

Haz clic en "Configuración", luego en "Cuentas vinculadas" y después en "Permitir acceso":

![Vincular cuenta en Community Cloud](https://blog.streamlit.io/content/images/2022/08/F2A5148A-2F6F-48D2-B935-A38542A87468.jpeg#browser)

Esto permitirá que Community Cloud despliegue tus aplicaciones de Streamlit desde tus repositorios de GitHub. En la página de autorización, haz clic en "Autorizar streamlit".

**Cuenta vinculada a GitHub**

Una vez que inicies sesión, Community Cloud obtendrá acceso a tu cuenta de GitHub:

![Cuenta vinculada a GitHub en Community Cloud](https://blog.streamlit.io/content/images/2022/08/16FA6767-9630-4C65-869D-77E2B2FC4199.jpeg#browser)

¡Ahora estás listo para desplegar aplicaciones de Streamlit!

Pero primero, creemos un repositorio en GitHub.

### Paso 4. Crea un repositorio GitHub para tu aplicación

Haz clic en "+" y luego en "Nuevo repositorio":

![Nuevo repositorio en GitHub](https://blog.streamlit.io/content/images/2022/08/A15327B7-F711-448A-BB97-A1CF2580BBC7.jpeg#browser)

Esto te llevará a la página "Crear un nuevo repositorio".

En el campo "Nombre del repositorio", escribe `st-hello-world`, haz clic en "Público", marca "Agregar un archivo README" (tu nuevo repositorio tendrá un archivo `README.md`) y haz clic en "Crear repositorio":

![Crear repositorio en GitHub](https://blog.streamlit.io/content/images/2022/08/1F88C1F7-893E-432D-9E7B-AEFD23D4D0B3.jpeg#browser)

¡Tu repositorio está listo!

Ahora crea el archivo de tu aplicación:

![Crea tu archivo de aplicación en GitHub](https://blog.streamlit.io/content/images/2022/08/7A37797E-C57A-4560-8104-790FA5537DEF.jpeg#browser)

Luego, crea el archivo `streamlit_app.py`:

![Crea el archivo streamlit_app.py en GitHub](https://blog.streamlit.io/content/images/2022/08/1825A4E6-9D5C-43DF-A4E3-DCC3FE2A5F37.jpeg#browser)

Tu repositorio de GitHub estará poblado con los archivos `README.md` y `streamlit_app.py`.

Después, regresa a Community Cloud:

![Vuelve a Community Cloud](https://blog.streamlit.io/content/images/2022/08/72631AEA-B0B9-412E-BA7C-06B3382855FA.jpeg#browser)

### Paso 5. Despliega tu aplicación en unos pocos clics

Finalmente, aquí viene la parte divertida. ¡Puedes desplegar tu aplicación!

Haz clic en "Nueva aplicación" y completa la información de tu aplicación:

![Nueva aplicación en Community Cloud](https://blog.streamlit.io/content/images/2022/08/9E0C7298-B079-4074-9DBB-EE9C04D14C31.jpeg#browser)

Esto creará un nuevo servidor. Verás el mensaje "Tu aplicación está en el horno".

En la esquina inferior derecha, haz clic en "Administrar aplicación" para ver los mensajes de registro (úsalos para depurar y solucionar errores):

![Administrar aplicación en Community Cloud](https://blog.streamlit.io/content/images/2022/08/EE1466B0-0A0C-4BD9-8B1E-02A37A380CF4.jpeg#browser)

El menú lateral muestra todos los mensajes de registro en tiempo real:

![Mensajes de registro en tiempo real en Community Cloud](https://blog.streamlit.io/content/images/2022/08/153F5C49-8CDC-4B1E-AFAE-AECC7AA4F849.jpeg#browser)

Una vez que tu aplicación termine de compilar, verás la salida. En nuestro ejemplo, será un mensaje simple: `¡Hola mundo!`

![Salida de la aplicación en Community Cloud](https://blog.streamlit.io/content/images/2022/08/IMG_0430.png#browser)

### Conclusión

¡Felicidades! Has desplegado exitosamente tu aplicación en Streamlit Community Cloud. Ahora puedes compartir la [URL de la aplicación](https://coding-professor-st-hello-world-streamlit-app-qj9a1u.streamlitapp.com/?ref=blog.streamlit.io) con la comunidad.

Si prefieres un video tutorial, echa un vistazo al siguiente video:

[<img src="https://i.ytimg.com/vi/HKoOBiAaHGg/maxresdefault.jpg" alt="Italian Trulli">](https://www.youtube.com/watch?v=HKoOBiAaHGg&ab_channel=Streamlit)




Lee más sobre:

* [Self-hosting ](https://docs.streamlit.io/knowledge-base/deploy/deploy-streamlit-heroku-aws-google-cloud?ref=blog.streamlit.io) de aplicaciones Streamlit en tus propios servidores (AWS, Azure, etc.).
* Diferentes [casos de uso de Streamlit](https://blog.streamlit.io/tag/community/) de la comunidad.


