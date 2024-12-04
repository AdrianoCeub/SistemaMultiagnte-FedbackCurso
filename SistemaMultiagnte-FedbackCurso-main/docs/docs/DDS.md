## Diagrama de Sequência - Feedback de Curso

Diagrama de Sequência

Fluxo de Envio de Feedback
- Ator: Aluno.
- Objetos: Frontend → Backend → Banco de Dados → API de IA.
- Descrição: O aluno envia um feedback, que é armazenado no banco de dados e processado pela API de IA.

Etapas:
- Aluno: Preenche o feedback na interface.
- Frontend: Envia dados ao backend.
- Backend: Armazena no banco e envia requisição à API.
- API de IA: Processa o feedback e retorna os resultados ao backend.
- Backend: Atualiza banco com os resultados e notifica o frontend.

![Diagrama de Sequência](DiagramaSequencia%20.jpg)


