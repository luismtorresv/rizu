---
title: "Usability Tests Results"
icon: "material/ab-testing"
---

## Participants

| ID  | Major | Semester |
| --- | ----- | -------- |
| P1  | CS    | 5        |
| P2  | CS    | 5        |
| P3  | CS    | 5        |
| P4  | CS    | 5        |
| P5  | CS    | 5        |
| P6  | CS    | 5        |
| P7  | ?     | ?        |

!!! note

    All participants were given an initial context of the platform's purpose
    and function prior to conducting the tests.

<!----------------------------------------------------------------------------->

## Tests

### Test 1: Account Creation and Login

| ID  | Time (min) | Success (%) | # Input errors                                        | Satisfaction (1–5) | Notes                                                                                                                                                                                                                                                                                    |
| :-- | :--------- | :---------- | :---------------------------------------------------- | :----------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1  | 1:06,65    | 100%        | 0                                                     | 5                  | El login lo vio muy bonito e intuitivo, con un diseño moderno. No entendió muy bien el propósito de seleccionar el rol al registrarse.                                                                                                                                                   |
| P2  | 00:49,74   | 100%        | 0                                                     | 3                  | No comprende el concepto de los roles, ya que siente que cuando alguien se va a crear una cuenta siempre querrá ser project manager y no le ve el sentido al rol de User. Además que no le gustó no pueder ver la contraseña que escribió. Sugirió poner un botón de mostrar contraseña. |
| P3  | 01:41,89   | 100%        | 1, no leyó bien las indicaciones de crear contraseña  | 5                  | Le parece que está super bien, muy bonita, parece una página de “verdad”.                                                                                                                                                                                                                |
| P4  | 01:32,07   | 100%        | 1, en el campo de username no puso un usuario válido. | 4                  | Le pareció bueno que no deje copiar y pegar los campos de las contraseñas, pero le parece mal que al equivocarse (en el campo de username) se le borre la contraseña que había puesto de manera correcta, sugiere que se borre únicamente el campo donde sí se equivocó                  |
| P5  | 00:56,30   | 100%        | 0                                                     | 4.5                | Sugiere que se muestre la contraseña, de resto muy lindo e intuitivo.                                                                                                                                                                                                                    |
| P6  | 01:35,00   | 100%        | 0                                                     | 4                  | Sugiere que se pueda ver la contraseña que se está escribiendo.                                                                                                                                                                                                                          |
| P7  | 00:58,43   | 100%        | 0                                                     | 5                  | Sugiere que se explique en un texto corto lo que significa el rol en el formulario de registro.                                                                                                                                                                                          |

#### Summary

| Metric              | Value   |
| :------------------ | :------ |
| Mean time (min)     | 1:14,30 |
| Success rate (%)    | 100%    |
| Mean # input errors | 0,2     |
| Mean satisfaction   | 4,35    |

### Test 2: Project Selection and Navigation

| ID  | Time (min) | Success (%) | Navigation errors                                                                                 | Clarity (1–5)                                                                                                | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| :-- | :--------- | :---------- | :------------------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1  | 01:18,50   | 80%         | 1, Presionó incorrectamente el botón de “View project detail” en lugar de ir al menú desplegable. | 4                                                                                                            | Al principio no entendía cómo entrar a manejar el proyecto, no vio con facilidad el menú desplegable de los proyectos y no logró encontrarlo. Pero con mínimas indicaciones “Leer los pasos de la dashboard” logró completarlo.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| P2  | 01:43,17   | 100%        | 2, Confusión en la Dashboard inicial y dificultad para encontrar proyectos unidos.                | 2                                                                                                            | Sugiere que después de que un usuario realiza una acción por primera vez (como unirse a un proyecto), las instrucciones iniciales “texto en la dashboard” deberían desaparecer y ser reemplazadas por la lista de proyectos (similar a la experiencia de un commit en GitHub), como un listado de los proyectos ya que el menú desplegable le parece poco intuitivo y muy escondido. El esperaría ver los proyectos ya directamente en la dashboard al unirse. Aunque el campo de búsqueda se podría mantener, los proyectos registrados deberían aparecer en la dashboard de forma predeterminada para evitar tener que buscarlos constantemente. |
| P3  | 01:59,65   | 100%        | 0                                                                                                 | 5                                                                                                            | En lugar de decir “Select a project..” en el menú desplegable de proyectos sería mejor poner “Select your project…”, Opiná que lo ideal es que los botones de join a project y create a project estén siempre en el header ya que es más intuitivo.                                                                                                                                                                                                                                                                                                                                                                                                |
| P4  | 02:38,66   | 100%        | 3                                                                                                 | Le dio dos calificaciones: 4 (si hubiera leído lo que estaba en la dashboard) 3 (no leyó, y se perdió mucho) | Opina que como la mayoría de las personas no se detienen a leer, que el apartado de la dashboard debería estar de mayor tamaño.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| P5  | 00:46,86   | 100%        | 0                                                                                                 | 4.7                                                                                                          | Le gustaría que cuando se una a un proyecto, aparezca un mensaje que se unió exitosamente y que automáticamente se redirigiera a la dashboard de ese proyecto al que se unió.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| P6  | 00:50,03   | 100%        | 1, Confusión al encontrar el menú desplegable                                                     | 4                                                                                                            | Sugiere mayor claridad para encontrar los proyectos rápidamente (ubicar el menú desplegable).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| P7  | 02:16,22   | 100%        | 1, Dificultad para encontrar proyectos unidos.                                                    | 3.5                                                                                                          | Sugiere reubicar el menú desplegable de la dashboard y que las instrucciones sean más claras.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

#### Summary

| Metric                  | Value    |
| :---------------------- | :------- |
| Mean time to select (s) | 01:39,01 |
| Success rate (%)        | 97,14%   |
| Mean navigation errors  | 1,1      |
| Mean clarity (1–5)      | 3,8      |

### Test 3: VM Deployment

| ID  | Time to launch (min) | Completion (%) | Error count                                                                                                                                                                   | Satisfaction (1–5) | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| :-- | :------------------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1  | 02:47,20             | 100%           | 3, Many errors, try to join a project using the view project bottom, it was difficult to look for the project in the dropdown selector, but easily find the create VM button. | 3                  | Le gustaría que seleccionar los proyectos fuera más intuitivo.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| P2  | 02:19,55             | 100%           | 0.                                                                                                                                                                            | 4                  | Menciona que muchos términos técnicos, como "RAM" y "flavor", pueden no ser comprendidos por usuarios sin conocimientos técnicos. Indica que la interfaz no es clara y que no muestra información suficiente cuando se crea un proyecto. Expresa confusión sobre si el proyecto se ha creado o no. Expresa que la experiencia del usuario debe ser más intuitiva, sugiriendo que se podrían incluir textos que ayuden a los usuarios a entender mejor las opciones disponibles. No le gusto mucho el contraste de color entre la landing page y la dashboard, al ver la dashboard con color en negro penso que se habia equivocado. |
| P3  | 00:56,19             | 100%           | 0                                                                                                                                                                             | 5                  | No entiende que es flavor y le gustaría que en el formulario le mostrará cómo un pequeño texto de los que es, lo mismo para los campos de image. Sugiere como una etiqueta corta con palabras clave. También cambiar “Flavor” por otro nombre más intuitivo.                                                                                                                                                                                                                                                                                                                                                                        |
| P4  | 01:24,00             | 100%           | 0                                                                                                                                                                             | 5                  | No le quedó claro para qué es la network y el router.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| P5  | 00:36,26             | 100%           | 1, Ingresó a “view project detail”.                                                                                                                                           | 4.5                | Sugiere que desde el apartado de listar todas las máquinas virtuales en la dashboard del proyecto también este un botón para desplegar una nueva.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| P6  | 01:10,33             | 100%           | 2                                                                                                                                                                             | 3.5                | Tuvo varios inconvenientes al intentar entrar en un proyecto. Pero resaltó que el botón para desplegar vm era fácil de ubicar. Tampoco entendía la terminología.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| P7  | 00:54,12             | 100%           | 0                                                                                                                                                                             | 5                  | Muy intuitivo y facil, le gustaria mayor claridad sobre qué es un flavor y una image.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

#### Summary

| Metric                  | Value    |
| :---------------------- | :------- |
| Mean time (min)         | 01:26,81 |
| Completion rate (%)     | 100%     |
| Mean error count        | 0,8      |
| Mean satisfaction (1–5) | 4,2      |

### Test 4: Overall Workflow

| ID  | Total time (min) | Task success (%) | Total errors                                                                             | Overall satisfaction | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| :-- | :--------------- | :--------------- | :--------------------------------------------------------------------------------------- | :------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1  | 13:48,30         | 100%             | 1 navigation confusion                                                                   | 5                    | Le gusto mucho la interfaz, pero le gustaría mayor claridad a la hora de seleccionar los proyectos.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| P2  | 04:20,96         | 100%             | 1 tuvo un error al crear un proyecto ya que no sabía que la descripción era obligatoria. | 4                    | Le parece muy “Bacano” la interfaz para ingresar a los proyectos y le gustaría que así también se listaran los proyectos de la dashboard, le gustaría que en la landing page estuviera la opción de entrar al perfil del usuario sin necesidad de tener que entrar en la dashboard cada vez, quiere poner los proyectos privados, ya que ahora cualquiera puede unirse a los proyectos que quiera, como darle permisos a las personas que quieran ingresar a los proyectos. No le gusta que al crear un proyecto no sepa si ya se creó(no hay mensaje de éxito). |
| P3  | 05:10,21         | 100%             | 0                                                                                        | 5                    | Muy intuitivo el workflow.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| P4  | 01:45,48         | 100%             | 0                                                                                        | 4                    | Sugiere que en el form de crear VM hubiera un texto explicando qué es flavor/image, ya que las personas que no sepan de plataformas como aws no lo entenderian.                                                                                                                                                                                                                                                                                                                                                                                                  |
| P5  | 01:09,51         | 100%             | 0                                                                                        | 4.5                  | Sugiere agregar un nuevo botón en el header de “My projects” y ahí ver los proyectos a los que se unió.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| P6  | 06:03,19         | 100%             | 0                                                                                        | 5                    | Sugiere que que en el formulario de creación de VM haya una breve explicación de términos como flavor e image. Sugiere mejorar la interfaz del dropdown menu.                                                                                                                                                                                                                                                                                                                                                                                                    |
| P7  | 07:06,09         | 100%             | 2                                                                                        | 4                    | Muy bien el diseño.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

#### Summary

| Metric                          | Value    |
| :------------------------------ | :------- |
| Mean total time (min)           | 05:37,68 |
| Task success rate (%)           | 100%     |
| Mean total errors               | 0,5      |
| Mean overall satisfaction (1-5) | 4,5      |

<!----------------------------------------------------------------------------->

## Overall Summary

### Positive Aspects

*  Visual design: attractive, modern interface.
*  Login: screen perceived as clear and intuitive; good validations that help
   with quick corrections.
*  Overall flow: intuitive workflow; users complete tasks with minimal
   instructions.
*  Key access: the button to deploy VM is easy to locate and use.
*  Reusable patterns: users like the way to enter projects; they ask to see the
   same pattern when listing projects.

### Negative Aspects

*  Unclear roles (Project Manager vs User). Purpose is unclear.

*  Password not visible; several users request a ‘show/hide’ button.

*  In the registration form, if the ‘username’ fails, the form deletes the
   correct password.

*  The dropdown is ‘hidden’ and does not clearly communicate its importance.

*  Expectation is to see a list of projects directly on the dashboard.

*  The initial help text does not ‘disappear’ after completing an action
   (joining a project).

*  Success message + automatic redirection to the project dashboard after
   joining is missing.

*  ‘Select a project...’ sounds generic; ‘Select your project...’ is preferred.

*  On the dashboard, show a list of projects (cards or simple table) as the
   default view.

*  Keep the search engine + filters at the top; leave the dropdown only as a
   secondary quick access (or remove it if it does not contribute).

*  First time on the dashboard: ‘You have no projects → large buttons: Join /
Create’ + brief steps (3 bullets). -> Once the user joins for the first time,
hide the instruction block and display the list of projects.

*  Unclear technical terminology: ‘Flavour’, ‘Image’, ‘RAM’, “Network”, ‘Router’
   are confusing, lack of context help during forms.

*  Contrast/theme between landing page (light) and dashboard (dark)

*  ‘Deploy VM’ button also in the project's VM list.

*  Anyone can join projects; suggestion for private projects with access
   control.

## Personal Opinion

> “You can observe a lot by watching.”
>
> — Yogi Berra, American professional baseball catcher

Running these sessions reminded us that usability tests are less about
validating finished ideas and more about discovering blind spots early. Hearing
participants stumble over roles, menus, and terminology gave us insights that no
review had surfaced. Each test means an opportunity for clearer flows and a
product that matches user expectations.
