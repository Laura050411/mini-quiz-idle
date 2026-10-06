# ===========================================
# DESAFIO DEV: MINI-QUIZ DE TECNOLOGIA ⚜
# ===========================================

#================================================================
#INSTITUIÇÃO: Colégio Estadual Jardim Oriente (CEJO) / SENAI
#CURSO: Técnico em Desenvolvimento de Sistemas
#ESTUDANTE: Laura Gonçalves Rodrigues
#TURMA: 1º A (Matutino) / 1º B (Vespertino)
#DATA: 06/10/2026
#UC: Lógica de Programação I / Programação de Apps I
#DESCRIÇÃO: Prática de Laços de Repetição (While e For)
#================================================================

print("=== BEM-VINDO AO QUIZ TECH CEJO/SENAI ===")
nome = input("Digite seu nome: ")
print(f"\nOlá, {nome}! Responda às perguntas com A, B ou C:\n")

pontuacao = 0

# --- PERGUNTA 1 ---
print("1) Qual linguagem estamos aprendendo nesta aula?")
print("A) HTML")
print("B) Python")
print("C) C++")
resposta1 = input("Sua resposta: ").strip().upper()

if resposta1 == "B":
    print("✅ Resposta correta! +1 ponto.\n")
    pontuacao = pontuacao + 1
else:
    print("❎ Resposta incorreta. A certa era B (Python).\n")

# --- PERGUNTA 2 ---
print("2) O que significa a sigla SGBD em banco de dados?")
print("A) Sistema de Gerenciamento de Banco de Dados")
print("B) Sistema Geral de Busca Digital")
print("C) Software de Gravação de Baixo Desempenho")
resposta2 = input("Sua resposta: ").strip().upper()

if resposta2 == "A":
    print("✅ Resposta correta! +1 ponto.\n")
    pontuacao = pontuacao + 1
else:
    print("❎ Resposta incorreta. A certa era A (Sistema de Gerenciamento de Banco de Dados).\n")

# --- PERGUNTA 3 ---
print("3) Qual função em Python é usada para exibir textos no terminal?")
print("A) input()")
print("B) print()")
print("C) display()")
resposta3 = input("Sua resposta: ").strip().upper()

if resposta3 == "B":
    print("✅ Resposta correta! +1 ponto.\n")
    pontuacao = pontuacao + 1
else:
    print("❎ Resposta incorreta. A certa era B (print).\n")

# --- PERGUNTA 4 ---
print("4) Qual é a extensão padrão dos arquivos de script Python?")
print("A) .py")
print("B) .pt")
print("C) .html")
resposta4 = input("Sua resposta: ").strip().upper()

if resposta4 == "A":
    print("✅ Resposta correta! +1 ponto.\n")
    pontuacao = pontuacao + 1
else:
    print("❎ Resposta incorreta. A certa era A (.py).\n")
    
# --- PERGUNTA 5 ---
print("5) Qual comando usamos em Python para receber uma entrada digitada pelo usuário?")
print("A) read()")
print("B) get()")
print("C) input()")
resposta5 = input("Sua resposta: ").strip().upper()

if resposta5 == "C":
    print("✅ Resposta correta! +1 ponto.\n")
    pontuacao = pontuacao + 1
else:
    print("❎ Resposta incorreta. A certa era C (input).\n")

# --- RESULTADO FINAL ---
print("======================================================")
print(f"Fim do Quiz, {nome}!")
print(f"Sua pontuação final foi: {pontuacao} de 4 pontos.")

if pontuacao == 5:
    print("🏆 Excelente! Você acertou tudo!")
elif pontuacao >= 2:
    print("👍 Bom trabalho! Dá para melhorar revisando o conteúdo.")
else:
    print("📚 Precisa estudar mais um pouquinho!")
print("======================================================")
