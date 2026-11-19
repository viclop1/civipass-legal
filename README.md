# civipass-legal

Las páginas públicas de Civipass, servidas con GitHub Pages en
https://viclop1.github.io/civipass-legal/. La app las abre desde Ajustes
(`lib/core/config/links.dart` en el repo `civipass`) y las fichas de las
tiendas enlazan a ellas.

| Página | Para qué |
| --- | --- |
| `fr/confidentialite.html` | Política de privacidad, texto de referencia |
| `en/privacy.html` | La misma política en inglés |
| `fr/assistance.html`, `en/support.html` | Ayuda y contacto (Apple exige una URL de soporte que se pueda abrir) |
| `index.html` | Portada con los cuatro enlaces |

## Publicar una versión de la política

Las dos políticas llevan una línea de borrador y la fecha sin poner hasta que
la abogada da el visto bueno. Entonces:

    python3 publicar.py AAAA-MM-DD
    git commit -am "Política de privacidad vN publicada" && git push

El script se niega si queda una línea de borrador o un `[marcador]`. Un
cambio en los datos que trata la app cambia la política antes de que salga
esa versión de la app.
