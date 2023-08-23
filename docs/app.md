# Aloja tu aplicación de Streamlit de forma gratuita


![](https://blog.streamlit.io/content/images/2022/08/image--4-.svg)

> **Nota**: Los artículos originales (en inglés) se encuentra disponible en:
> - [Host your Streamlit app for free](https://blog.streamlit.io/host-your-streamlit-app-for-free/#:~:text=Connect%20your%20account%20to%20GitHub,-There%20are%20two&text=On%20the%20authorization%20page%2C%20click%20on%20%E2%80%9CAuthorize%20streamlit.%22&text=This%20will%20let%20Community%20Cloud,%2C%20click%20%E2%80%9CAuthorize%20streamlit.%22&text=Now%20you're%20ready%20to%20deploy%20Streamlit%20apps!).
> - [streamlit-community-cloud/get-started/quickstart](https://docs.streamlit.io/streamlit-community-cloud/get-started/quickstart).

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



## Inicio rápido

Aquí tienes un conjunto conciso de pasos para crear tu cuenta en Streamlit Community Cloud y desplegar una aplicación de ejemplo. Para otras opciones y explicaciones completas, comienza con [Crea tu cuenta](/streamlit-community-cloud/get-started/create-your-account).

Durante este proceso, iniciarás sesión en tus cuentas de Google y GitHub. Si aún no tienes estas cuentas, puedes crearlas antes de comenzar. Si no deseas usar una cuenta de Google, puedes [crear tu cuenta con cualquier correo electrónico](/streamlit-community-cloud/get-started/create-your-account#primary-identity-option-2-email).

### Registrarse


1.  Ve a [share.streamlit.io/signup](https://share.streamlit.io/signup).
2.  Haz clic en "**Continue with Google**".

    ![Registrarse en Streamlit Community Cloud con Google](https://docs.streamlit.io/images/streamlit-community-cloud/sign-up-Google-XL.png)

3.  Ingresa tus credenciales de Google y sigue las indicaciones de autenticación de Google.
4.  Después de autenticar con Google, haz clic en "**Authorize streamlit**".

    ![Conectar tu cuenta de GitHub a Streamlit Community Cloud](https://docs.streamlit.io/images/streamlit-community-cloud/sign-up-2.png)

5.  Ingresa tus credenciales de GitHub y sigue las indicaciones de autenticación de GitHub.
6.  Haz clic en "**Autorizar streamlit**".

    ![Autorizar a streamlit a conectar con tu cuenta de GitHub](https://docs.streamlit.io/images/streamlit-community-cloud/GitHub-auth1-none.png)

7.  Para finalizar, completa tu información y haz clic en "**Continue**" en la parte inferior de la pantalla.

    ![Configura tu cuenta en Streamlit Community Cloud](https://docs.streamlit.io/images/streamlit-community-cloud/sign-up-3.png)

8.  Serás llevado a tu espacio de trabajo en Streamlit. Si ves un ícono de advertencia (⚠️) junto a "**Settings**" en la esquina superior derecha, esto se resolverá en los siguientes pasos.

    ![Tu nuevo espacio de trabajo en Streamlit Community Cloud](https://docs.streamlit.io/images/streamlit-community-cloud/workspace-empty-warning.png)

### Fork a una app de ejemplo

9.  Haz clic en la flecha hacia abajo (_expand\_more_) para desplegar las opciones debajo de "**New App**".

    ![Opciones para desplegar una nueva app desde tu espacio de trabajo en Streamlit Community Cloud](https://docs.streamlit.io/images/streamlit-community-cloud/deploy-example-1.png)

10.  Haz clic en "**Create from sample app template**".

    ![Despliega una nueva app desde una plantilla de app de ejemplo](https://docs.streamlit.io/images/streamlit-community-cloud/deploy-example-2.png)

11.  Se te pedirá que "Streamlit solicita permisos adicionales". Haz clic en "**Authorize streamlit"**".

    ![Autoriza a streamlit a acceder a repositorios privados](https://docs.streamlit.io/images/streamlit-community-cloud/GitHub-auth2-none.png)

12.  Haz clic en "**Fork sample app**".

    ![Duplica la app de ejemplo de Streamlit](https://docs.streamlit.io/images/streamlit-community-cloud/deploy-example-fork.png)

### Despliega una app de ejemplo


13.  Después de que el repositorio se copie a tu cuenta de GitHub, la información del repositorio duplicado se llenará automáticamente en una pantalla de despliegue. Haz clic en "**¡Deploy!**"

     ![Despliega tu app de ejemplo de Streamlit](https://docs.streamlit.io/images/streamlit-community-cloud/deploy-example-deploy.png)

14.  Espera a que la app se compile. Esto puede llevar unos minutos.

     ![Observa cómo se compila y despliega tu app](https://docs.streamlit.io/images/streamlit-community-cloud/deploy-demo-provisioning.png)

### ¡Has terminado!


¡Felicidades! Acabas de desplegar una app en Streamlit Community Cloud. 🎉 Puede que la app tarde unos minutos en compilar completamente, pero una vez que esté lista, se cargará automáticamente.

![Observa tu app de Streamlit desplegada](https://docs.streamlit.io/images/streamlit-community-cloud/deploy-example-done.png)
