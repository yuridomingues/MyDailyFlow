# Bibliotecas de opções
cafe_da_manha = [
    "2 fatias de pão integral",
    "2 ovos mexidos com tomate",
    "1 colher de sopa de requeijão ou 1 fatia de queijo magro",
    "1 maçã",
    "1 porção de tomate",
    "Suplemento: Creatina (conforme instruções)"
]

lanche_manha = [
    "1 banana com um pouco de mel",
    "1 ovo cozido",
    "1 colher de sopa de queijo cottage ou iogurte grego"
]

almoco = [
    "150-200g de carne magra (frango, peixe ou carne vermelha magra)",
    "1 porção de arroz integral ou batata-doce",
    "Uma grande porção de vegetais variados",
    "1 colher de sopa de azeite de oliva",
    "Feijão",
    "Extra: Um pedaço de fruta cítrica, como laranja ou kiwi, para ajudar na absorção de ferro da carne."
]

jantar = [
    "150-200g de carne magra",
    "1 porção de batata-doce, arroz integral ou massa de grão integral",
    "Uma grande porção de vegetais (salada ou legumes cozidos)",
    "Feijão (se desejado)",
    "Opcional: 1 colher de chá de sementes de chia ou linhaça"
]

lanche_antes_faculdade = [
    "1 porção de iogurte grego com mel (proteína e carboidratos rápidos para energia)",
    "Uma pequena porção de nozes ou sementes (para gorduras saudáveis e saciedade)",
    "1 fruta prática, como uma maçã ou banana"
]

ceia = [
    "1 copo de leite desnatado ou iogurte grego",
    "Uma pequena porção de frutas (morango, maçã)",
    "1 porção de queijo cottage ou uma pequena quantidade de nozes"
]

treino_a = [
"Remada curvada unilateral (garrafa de amaciante) 3x15",
"Remada curvada simultâneo 4x15",
"Apoio de frente aberto (flexão)",
"Apoio de frente fechado (flexão)",
"Tríceps francês (unilateral, com garrafinha d'água)",
"Bíceps simultâneo (garrafinha)",
"Desenvolvimento fechado (garrafinha)",
"Prancha isométrica",
"Abdominal reto solo"
]

treino_b = [
    "Aquecimento (5-10 minutos):",
    "Polichinelos: 2 minutos",
    "Agachamento livre (sem peso): 1 minuto",
    "Alongamento dinâmico de pernas: 2 minutos (exemplo: balançar as pernas para frente e para os lados).",
    "",
    "Exercícios:",
    "Agachamento livre (com peso opcional): 4x15",
    "Foco: Quadríceps, glúteos e posterior de coxa.",
    "Dica: Mantenha as costas retas e os pés alinhados com os ombros.",
    "",
    "Afundo (passada): 3x12 (cada perna)",
    "Foco: Glúteos, quadríceps e posterior de coxa.",
    "Dica: Dê um passo à frente e desça até o joelho de trás quase tocar o chão.",
    "",
    "Elevação de quadril (ponte glútea): 4x15",
    "Foco: Glúteos e posterior de coxa.",
    "Dica: Eleve o quadril até formar uma linha reta dos ombros aos joelhos.",
    "",
    "Agachamento sumô (pernas abertas): 3x15",
    "Foco: Parte interna das coxas e glúteos.",
    "Dica: Mantenha os pés mais afastados e apontados para fora.",
    "",
    "Subida no banco (ou cadeira): 3x12 (cada perna)",
    "Foco: Quadríceps e glúteos.",
    "Dica: Use um banco ou cadeira firme. Suba com uma perna de cada vez.",
    "",
    "Abdução de quadril lateral (deitado de lado): 3x15 (cada lado)",
    "Foco: Glúteo médio (lateral do quadril).",
    "Dica: Levante a perna devagar, mantendo o controle.",
    "",
    "Prancha com elevação de perna: 3x12 (cada perna)",
    "Foco: Core e glúteos.",
    "Dica: Na posição de prancha, eleve uma perna de cada vez, mantendo o corpo alinhado.",
    "",
    "Abdominal bicicleta: 3x20 (10 de cada lado)",
    "Foco: Oblíquos e reto abdominal.",
    "Dica: Mantenha o movimento controlado e o pescoço relaxado.",
    "",
    "Prancha lateral: 3x30 segundos (cada lado)",
    "Foco: Oblíquos e core.",
    "Dica: Mantenha o corpo alinhado e evite deixar o quadril cair.",
    "",
    "Alongamento final (5-10 minutos):",
    "Alongamento de posterior de coxa: 30 segundos (cada perna).",
    "Alongamento de quadríceps: 30 segundos (cada perna).",
    "Alongamento de glúteos: 30 segundos (cada lado).",
    "Alongamento de panturrilha: 30 segundos (cada perna).",
    "",
    "Dicas para o Treino B:",
    "Progressão: Se os exercícios estiverem fáceis, aumente o número de repetições ou adicione peso (use mochilas com livros ou garrafas cheias de água/areia).",
    "Forma correta: Preste atenção à postura para evitar lesões, especialmente nos agachamentos e afundos.",
    "Descanso: Descanse 30-60 segundos entre as séries.",
    "Frequência: Faça o Treino B 2-3 vezes por semana, alternando com o Treino A."
]

routine = {
    "Segunda-feira": [
        ("6:45 - 6:45", "Acordar + tomar levotiroxina com água em jejum"),
        ("7:00 - 7:20", "{cafe_da_manha}"),
        ("8:00 - 14:00", "Trabalho"),
        ("09:00 - 09:20", "{lanche_manha}"),
        ("14:00 - 14:45", "Deslocamento para casa"),
        ("14:45 - 15:00", "{almoco})"),
        ("15:00 - 17:00", "Tempo com namorada"),
        ("17:00 - 18:00", "{treino_a}"),
        ("18:00 - 18:10", "{jantar}"),
        ("18:10 - 19:00", "Deslocamento para faculdade"),
        ("19:00 - 22:00", "Faculdade"),
        ("22:00 - 22:45", "Deslocamento para casa"),
        ("22:45 - 23:00", "{ceia}"),
        ("23:00 - 23:15", "Relaxar (ler, ouvir música, conversar)"),
        ("23:15", "Dormir")
    ],
    "Terça-feira": [
        ("6:45 - 6:45", "Acordar + tomar levotiroxina com água em jejum"),
        ("7:00 - 7:20", "Café da manhã"),
        ("7:20 - 8:00", "Deslocamento para o trabalho"),
        ("8:00 - 14:00", "Trabalho"),
        ("14:00 - 14:45", "Deslocamento para casa"),
        ("14:45 - 15:00", "Almoço"),
        ("15:00 - 17:00", "Tempo com namorada"),
        ("17:00 - 18:00", "Treino B (Inferiores e Core)"),
        ("18:00 - 18:10", "Lanche pós-treino"),
        ("19:00 - 22:00", "Faculdade"),
        ("22:00 - 22:45", "Deslocamento para casa"),
        ("22:45 - 23:00", "Comida leve"),
        ("23:00 - 23:15", "Relaxar (ler, ouvir música, conversar)"),
        ("23:15", "Dormir")
    ],
    "Quarta-feira": [
        ("6:45 - 6:45", "Acordar + tomar levotiroxina com água em jejum"),
        ("7:00 - 7:20", "Café da manhã"),
        ("7:20 - 8:00", "Deslocamento para o trabalho"),
        ("8:00 - 14:00", "Trabalho"),
        ("14:00 - 14:45", "Deslocamento para casa"),
        ("14:45 - 15:00", "Almoço"),
        ("15:00 - 17:00", "Tempo com namorada"),
        ("17:00 - 18:00", "Treino A (Superior)"),
        ("18:00 - 18:10", "Lanche pós-treino"),
        ("18:10 - 19:00", "Deslocamento para faculdade"),
        ("19:00 - 22:00", "Faculdade"),
        ("22:00 - 22:45", "Deslocamento para casa"),
        ("22:45 - 23:00", "Comida leve"),
        ("23:00 - 23:15", "Relaxar (ler, ouvir música, conversar)"),
        ("23:15", "Dormir")
    ],
    "Quinta-feira": [
        ("6:45 - 6:45", "Acordar + tomar levotiroxina com água em jejum"),
        ("7:00 - 7:20", "Café da manhã"),
        ("7:20 - 8:00", "Deslocamento para o trabalho"),
        ("8:00 - 14:00", "Trabalho"),
        ("14:00 - 14:45", "Deslocamento para casa"),
        ("14:45 - 15:00", "Almoço"),
        ("15:00 - 17:00", "Tempo com namorada"),
        ("17:00 - 18:00", "Treino B (Inferiores e Core)"),
        ("18:00 - 18:10", "Lanche pós-treino"),
        ("18:10 - 19:00", "Deslocamento para faculdade"),
        ("19:00 - 22:00", "Faculdade"),
        ("22:00 - 22:45", "Deslocamento para casa"),
        ("22:45 - 23:00", "Comida leve"),
        ("23:00 - 23:15", "Relaxar (ler, ouvir música, conversar)"),
        ("23:15", "Dormir")
    ],
    "Sexta-feira": [
        ("6:45 - 6:45", "Acordar + tomar levotiroxina com água em jejum"),
        ("7:00 - 7:20", "Café da manhã"),
        ("7:20 - 8:00", "Deslocamento para o trabalho"),
        ("8:00 - 14:00", "Trabalho"),
        ("14:00 - 14:45", "Deslocamento para casa"),
        ("14:45 - 15:00", "Almoço"),
        ("15:00 - 17:00", "Tempo com namorada"),
        ("17:30 - 18:30", "Projeto Back-End"),
        ("18:30 - 19:30", "Treino A (Superior)"),
        ("19:30 - 19:45", "Janta"),
        ("20:00 - 22:00", "Estudos"),
        ("22:00 - 22:15", "Comida leve"),
        ("23:00 - 23:15", "Relaxar (ler, ouvir música, conversar)"),
        ("23:15", "Dormir")
    ],
    "Sábado": [
        "Estudar Elementos de Segurança"
    ],
    "Domingo": [
        "Estudar Estrutura de Dados e Paradigmas"
        "Estudar Física"
    ]
}
