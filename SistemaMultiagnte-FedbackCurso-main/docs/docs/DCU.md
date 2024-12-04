# Diagrama de Caso de Uso - Feedback de Curso

Casos de Uso (Detalhamento)

1.Cadastro/Login (Aluno)
Descrição: Permitir que alunos se cadastrem e façam login para acessar a plataforma.

Atores Envolvidos: Aluno.

Fluxo Principal:
O aluno acessa a página de login/cadastro.
Insere suas credenciais (e-mail, senha).
O sistema verifica a autenticidade das informações.
Acesso autorizado.

Fluxo Alternativo: Em caso de erro, o sistema retorna mensagens específicas (e.g., "Senha incorreta").

2.Enviar Feedback (Aluno)
Descrição: Registrar a opinião sobre um curso.

Atores Envolvidos: Aluno, API de IA.

Fluxo Principal:
O aluno acessa a página do curso.
Preenche o formulário de feedback.
O feedback é enviado para o backend, armazenado no banco de dados e enviado à API de análise de sentimentos.

Fluxo Alternativo: Caso a conexão com a API falhe, o sistema armazena o feedback para envio posterior.

3.Visualizar Relatório de Sentimentos (Administrador)
Descrição: Permitir que administradores acessem relatórios de feedback com análise de sentimentos.

Atores Envolvidos: Administrador.

Fluxo Principal:
O administrador faz login no sistema.
Acessa o painel de relatórios.
Visualiza gráficos e análises geradas pela API de sentimentos.

4.Análise de Sentimentos (API de IA)
Descrição: Realizar análise automática dos textos de feedback para gerar insights.

Atores Envolvidos: API de IA, Feedbacks (dados).

Fluxo Principal:
O feedback enviado pelo aluno é processado pela API.
A API retorna informações de polaridade (positivo, negativo, neutro) e palavras-chave associadas.

|Etapa|Ator|Descrição|Fluxo Principal|
|---|---|---|---|
|Cadastro|Aluno|Permite que o aluno crie uma conta e faça login na plataforma|1.Aluno acessa a tela de login 2.Insere dados de acesso. 3.Validação e login são confirmados.|
|Enviar Feedback|Aluno|O aluno envia uma avaliação para o curso específico|1.Aluno seleciona o curso. 2.Insere feedback. 3.Envia o feedback que é registrado no sistema.|
|Visualizar Relatório de Sentimentos|Administrador|O administrador acessa o relatório de feedbacks com análise de sentimentos.|1.Administrador acessa a interface de relatórios. 2.Visualiza gráficos e insights dos feedbacks.|
|Análise de Sentimento|API de IA|Realiza a análise de sentimento do feedback recebido.|1.Feedback é enviado para a API. 2.API processa o sentimento. 3.Resultados são exibidos para o admin.|

Imagem Do Diagrama de Caso de Uso:
![Diagrama Caso de Uso](CasoDeUso.png)















