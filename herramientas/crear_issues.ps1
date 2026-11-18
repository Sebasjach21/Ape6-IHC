# Publica los Issues del backlog en GitHub.
# Requisitos: GitHub CLI (`winget install GitHub.cli`) y `gh auth login`.
# Uso (desde la raíz del repositorio):  powershell -File herramientas/crear_issues.ps1
$ErrorActionPreference = 'Stop'
$repo = 'Sebasjach21/Ape6-IHC'
gh issue create --repo $repo --title "B-01 · Búsqueda sensible a tildes (P1)" --body-file "Fase4-Cierre/issues/B-01.md"
gh issue create --repo $repo --title "B-02 · Producto con pocas unidades se agota recién al confirmar (P1)" --body-file "Fase4-Cierre/issues/B-02.md"
gh issue create --repo $repo --title "B-03 · El pedido confirmado no se encuentra desde «Mi pedido» (P2)" --body-file "Fase4-Cierre/issues/B-03.md"
gh issue create --repo $repo --title "B-05 · Falta información de pago, tiempo y lugar de retiro (P2)" --body-file "Fase4-Cierre/issues/B-05.md"
gh issue create --repo $repo --title "B-04 · Etiquetas de navegación inconsistentes (P3)" --body-file "Fase4-Cierre/issues/B-04.md"
gh issue create --repo $repo --title "B-06 · Horas de retiro fijas y sin relación con la hora actual (P3)" --body-file "Fase4-Cierre/issues/B-06.md"
gh issue create --repo $repo --title "B-08 · Agregar un producto lleva a «Mi pedido» sin avisar (P3)" --body-file "Fase4-Cierre/issues/B-08.md"
gh issue create --repo $repo --title "B-07 · Textos secundarios menores a 12 px (P4)" --body-file "Fase4-Cierre/issues/B-07.md"
gh issue create --repo $repo --title "B-09 · Límite de 9 unidades sin mensaje (P4)" --body-file "Fase4-Cierre/issues/B-09.md"
gh issue create --repo $repo --title "B-10 · «Sanduche» sin tilde y distinto del nombre en las tareas (P4)" --body-file "Fase4-Cierre/issues/B-10.md"
