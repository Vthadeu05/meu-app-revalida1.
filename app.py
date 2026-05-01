import streamlit as st

# Configuração da página
st.set_page_config(page_title="Revalida Quiz", page_icon="🩺")

# Simulação de um banco de dados de questões
questions = [
    {
        "area": "Pediatria",
        "pergunta": "Qual a conduta imediata para um recém-nascido a termo, com bom tônus e chorando?",
        "opcoes": ["Clampeamento imediato do cordão", "Prover calor e posição", "Aspirar vias aéreas", "Clampeamento tardio do cordão e contato pele a pele"],
        "correta": "Clampeamento tardio do cordão e contato pele a pele"
    },
    {
        "area": "Cirurgia Geral",
        "pergunta": "Qual o sinal clássico de apendicite aguda na fossa ilíaca direita?",
        "opcoes": ["Sinal de Murphy", "Sinal de Blumberg", "Sinal de Jobert", "Sinal de Cullen"],
        "correta": "Sinal de Blumberg"
    }
]

st.title("🩺 Revalida Study App")
st.subheader("Prepare-se para a revalidação médica")

# Barra lateral para progresso
st.sidebar.header("O teu progresso")
area_selecionada = st.sidebar.selectbox("Escolha a Área", ["Todas", "Pediatria", "Cirurgia Geral", "Clínica Médica"])

# Lógica simples de Quiz
score = 0
for i, q in enumerate(questions):
    if area_selecionada == "Todas" or area_selecionada == q["area"]:
        st.write(f"**Questão {i+1}:** {q['pergunta']}")
        resposta = st.radio(f"Selecione a opção para a Q{i+1}:", q["opcoes"], key=i)
        
        if st.button(f"Confirmar Resposta {i+1}"):
            if resposta == q["correta"]:
                st.success("Correto! ✅")
                score += 1
            else:
                st.error(f"Incorreto. A resposta certa era: {q['correta']}")
        st.divider()

st.sidebar.write(f"Pontuação atual: {score}")
