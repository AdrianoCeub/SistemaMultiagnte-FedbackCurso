# Requisitos - Feedcak de Curso

Requisitos Funcionais (RF)
Módulo de Interface do Usuário (Web)

RF01 – O sistema deve permitir que o aluno envie feedbacks sobre cursos finalizados.  
RF02 – O sistema deve apresentar uma interface para o administrador visualizar relatórios de feedback.

Módulo de Autenticação

RF03 – O sistema deve permitir que o administrador cadastre novos usuários administradores.

Módulo de Feedback (CRUD)

RF04 – O sistema deve permitir que o aluno crie um novo feedback.  
RF05 – O sistema deve armazenar os feedbacks com informações como data, curso e aluno.  
RF06 – O sistema deve validar que o aluno só pode enviar feedback para cursos em que esteja inscrito.

Módulo de Análise de Sentimentos (API de IA)

RF07 – O sistema deve integrar uma API de análise de sentimentos para processar automaticamente os feedbacks.  
RF08 – O sistema deve enviar feedbacks em texto para a API e receber uma classificação de sentimento (positivo, neutro, negativo).  
RF09 – O sistema deve gerar relatórios de análise de sentimento para os administradores visualizarem.  
RF10 – O sistema deve identificar padrões de sentimentos e gerar gráficos com base nos feedbacks recebidos.

Requisitos Não Funcionais (RNF)

RNF01 – O sistema deve ser acessível via navegadores web modernos (Google Chrome, Firefox, Safari).  
RNF02 – O sistema deve seguir as boas práticas de responsividade, permitindo o acesso em dispositivos móveis e desktops.  
RNF03 – O sistema deve garantir que os dados dos usuários sejam armazenados de forma segura, com criptografia de senhas.  
RNF04 – O sistema deve garantir a disponibilidade mínima de 99% durante o horário de funcionamento da instituição.  
RNF05 – O sistema deve processar a análise de sentimentos em até 5 segundos após o envio do feedback.  
RNF06 – O sistema deve ser escalável para suportar até 10.000 usuários simultâneos.  
RNF07 – O sistema deve utilizar padrões de segurança como autenticação JWT para sessões de login.  
RNF08 – O sistema deve permitir exportação de relatórios em formato PDF ou CSV.  
RNF09 – O sistema deve garantir que a API de análise de sentimentos seja acessada por uma conexão segura (HTTPS).