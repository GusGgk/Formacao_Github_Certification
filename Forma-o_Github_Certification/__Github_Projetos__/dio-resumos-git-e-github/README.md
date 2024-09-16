
# DIO | RESUMOS - Git e GitHub

Repositório para armazenar resumos de aprendizado do Git e GitHub, dentro do Python AI Backend Developer, curso de 67 horas
da [Digital Innovation One](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwji5PjIoIyHAxWOrpUCHYbtB6IQFnoECAYQAQ&url=https%3A%2F%2Fwww.dio.me%2F&usg=AOvVaw3P75GLlstjORQVFDCyOyYk&opi=89978449)

## 📖 Documentação
- [Documentação Git](https://git-scm.com)
- [Documentação GitHub](https://docs.github.com)

## 💻 Resumos das Aulas

| Aulas | Resumos |
|-------|---------|
Criando e Clonando Repostórios | [Resumo](https://web.dio.me/course/versionamento-de-codigo-com-git-e-github/learning/a377a00b-461c-4ab0-8258-3addd2fef14c?back=/track/coding-future-vivo-python-ai-backend-developer&tab=undefined&moduleId=undefined) |
Salvando Alterações no Repositório Local | [Resumo](https://web.dio.me/course/versionamento-de-codigo-com-git-e-github/learning/599dd3dd-d189-474f-a55c-22f37b4472da?back=/track/coding-future-vivo-python-ai-backend-developer&tab=undefined&moduleId=undefined) |
Desfazendo Alterações no Repositório Local |[Resumo](https://web.dio.me/course/versionamento-de-codigo-com-git-e-github/learning/3f9f2336-6fd5-44cb-ba39-d1a4f6448023?back=/track/coding-future-vivo-python-ai-backend-developer&tab=undefined&moduleId=undefined) |
Enviando e Baixando Alterações com o Repositório Remoto | [Resumo](https://web.dio.me/course/versionamento-de-codigo-com-git-e-github/learning/dd17c56e-2327-493c-942a-358a49a26549?back=/track/coding-future-vivo-python-ai-backend-developer&tab=undefined&moduleId=undefined) |
Trabalhando com Branches - Criando, Mesclando, Deletando e Tratando Conflitos | [Resumo](https://web.dio.me/course/versionamento-de-codigo-com-git-e-github/learning/2c7fd2b1-e7c4-4947-9b07-ffcbfb4bd689?back=/track/coding-future-vivo-python-ai-backend-developer&tab=undefined&moduleId=undefined) |
Trabalhando com Branches - Comandos Úteis no Dia a Dia |[Resumo](https://web.dio.me/course/versionamento-de-codigo-com-git-e-github/learning/80018fab-daac-4917-8527-a6be2e0c3cf0?back=/track/coding-future-vivo-python-ai-backend-developer&tab=undefined&moduleId=undefined) |

## 👨‍💻 ANOTAÇÕES DA AULA - Criando e Clonando Repostórios
```
existem 2 formas de obter um repositório Git na sua maquina
1- Transformando um diretório local que não está sob controle de versão, num repositório Git;
2- Clonando um repositório Git Existente
dentro do git

mkdir repo-local
cd repo-local/
git init
cd .git
ls (lsita)
cat config
git clone ( repositório ) (trocar nome em seguida se quiser)
cd repo-clonado
git remote ~v
cd ..
git remote add origin ( URL ) 
git clone url novo nome
```
## 👨‍💻 ANOTAÇÕES DA AULA - Salvando Alterações no Repositório Local
```
mkdir nome-escolhido
cd nome-escolhido
git init
git status
touch (arquivo).md

git commit -m"mensagem"
git log

echo nome/ > .gitignore

touch nome/.gitkeep
git add . (add todos de uma vez)
clear (limpa tudo)
```
## 👨‍💻 ANOTAÇÕES DA AULA - Desfazendo Alterações no Repositório Local
```
git init
para remover 
rm -rf .git
git status

caso apagar um arquivo sem querer
use o comando 
git restore (nome do arquivo)

git commit --amend -m"mensagem"
para trocar a mensagem do commit

ou tbm pode usar apenas
git commit --amend (aperte i dps na outra aba e escreva)

git reset --soft (commit)


git add .
git commit -m"soft"
git log

clear

git log
git reset --mixed (commit)

git add .
git commit -m"mixed"

git reset --hard (commit)
apaga tudo 
```
## 👨‍💻 ANOTAÇÕES DA AULA - Enviando e Baixando Alterações com o Repositório Remoto
```
git remote add origin https://github.com/GusGgk/dio-resumos-git-e-github.git
git branch -M main
git push -u origin main
git pull para puxar o remoto para o local
```
## 👨‍💻 ANOTAÇÕES DA AULA - Trabalhando com Branches - Criando, Mesclando, Deletando e Tratando Conflitos
```
De maneira simplista, uma Branch (em tradução, "Ramo"), é uma ramificação do seu projeto.
- É um ponteiro móvel para um commit no histórico do repositório;
- Quando você cria uma nova Branch a partir de outra existente, a nova se inicia apontando para o mesmo commit da Branch que estava quando foi criada.

para criar um arquivo apenas
comando

echo "#nomedoarquivoMAIN" > nomedoarquivoMAIN.txt
git add .
git commit -m"mensagem"
git log

git checkout -b teste

criar uma branch dentro da teste agora

echo "#nomedoarquivoTESTE" > nomedoarquivoTESTE.txt
git add .
git commit -m"mensagem"
git log

para tirar do teste basta usar o msm código so que com main
git checkout main
(o de teste não ira aparecer o arquivo pois funciona de maneira independente)

Para ver tudo use o código
git branch -v

Para mesclar o main com o teste
git merge (nome da branch para mesclar--nesse caso ---teste)
git merge teste


git branch (serve para ver a lista de branch)

(para excluir a branch teste já que foram mescladas é)
git branch -d (branch para excluir)
git branch -d teste
```
## 👨‍💻 ANOTAÇÕES DA AULA - Trabalhando com Branches - Comandos Úteis no Dia a Dia
```
git pull -> git fetch + git merge

git fetch origin main
para trazer o arquivo feito depois do GITHUB PARA O GIT
git diff main origin/main (rebola pros cria)
git merge origin/main

caso queira clonar so uma branch em um repositório cheio de branch faça esse código

Git clone (url do repositório) --branch (a que você quer) --sigle-branch

git stash
git stash apply
```
## ❓QUESTIONÁRIO DO CURSO
```
Qual o comando utilizado para criar uma cópia de um repositório Git existente?
git clone

Qual comando utilizado para configurar o email no Git?
git config --global user.email seuemail@gmail.com

Qual o comando utilizado para inicializar um repositório Git?
git init

Qual comando do Git podemos utilizar para alternar entre branches?
git checkout

Qual a diferença entre Git e GitHub?
git sistema de controle de versão distribuído e GitHub hospedagem de código para controle utilizando o git

Qual comando utilizado no Git para enviar alterações do repositório local para o remoto?
git push

Qual comando do Git podemos utilizar para clonar apenas uma branch?
git clone nome --branch nome --single-branch

Sobre Versionamento de Código, é INCORRETO afirmar:
gera uma versão final do código somente no final do desenvolvimento de cada projeto
```

## 🔍 Referências
- [Digital Innovation One](https://www.dio.me)
- [Repositório da Eliana Andrade](https://github.com/elidianaandrade/dio-curso-git-github)


