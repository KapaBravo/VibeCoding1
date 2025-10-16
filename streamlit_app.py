# Import and run the Streamlit app
import streamlit as st
import random
from typing import Dict, List, Tuple

# Configure page
st.set_page_config(
    page_title="Calculadora de Calorias & Refeições",
    page_icon="🍎",
    layout="wide"
)

# Database de refeições expandido
MEALS_DATABASE = {
    "lose": [
        # CAFÉ DA MANHÃ - PERDER PESO
        {
            "name": "Aveia com Frutas Vermelhas",
            "calories": 320,
            "protein": 12,
            "carbs": 58,
            "fat": 6,
            "time": "10 min",
            "category": "Café da Manhã",
            "ingredients": [
                "1/2 xícara de aveia em flocos",
                "1 xícara de leite desnatado",
                "1/4 xícara de frutas vermelhas mistas",
                "1 colher de sopa de mel",
                "1 colher de chá de canela",
                "1 colher de sopa de sementes de chia"
            ],
            "recipe": [
                "Em uma panela, aqueça o leite em fogo médio.",
                "Adicione a aveia e mexa bem para não grudar.",
                "Cozinhe por 5-7 minutos mexendo ocasionalmente.",
                "Adicione a canela e o mel, misture bem.",
                "Retire do fogo e deixe esfriar por 2 minutos.",
                "Coloque em uma tigela e adicione as frutas vermelhas por cima.",
                "Finalize com as sementes de chia e sirva."
            ]
        },
        {
            "name": "Omelete de Espinafre",
            "calories": 280,
            "protein": 20,
            "carbs": 8,
            "fat": 18,
            "time": "8 min",
            "category": "Café da Manhã",
            "ingredients": [
                "3 ovos inteiros",
                "1 xícara de espinafre fresco",
                "2 tomates cereja",
                "1 colher de sopa de azeite",
                "1/4 xícara de queijo cottage",
                "1 dente de alho picado",
                "Sal e pimenta a gosto"
            ],
            "recipe": [
                "Bata os ovos em uma tigela com sal e pimenta.",
                "Aqueça o azeite em frigideira antiaderente.",
                "Refogue o alho e espinafre por 2 minutos.",
                "Despeje os ovos batidos na frigideira.",
                "Adicione o queijo cottage e tomates cereja.",
                "Cozinhe por 3-4 minutos até firmar embaixo.",
                "Dobre a omelete ao meio e sirva quente."
            ]
        },
        {
            "name": "Smoothie Verde Detox",
            "calories": 180,
            "protein": 8,
            "carbs": 32,
            "fat": 4,
            "time": "5 min",
            "category": "Café da Manhã",
            "ingredients": [
                "1 xícara de espinafre fresco",
                "1/2 banana congelada",
                "200ml de água de coco",
                "1/2 maçã verde",
                "Suco de 1/2 limão",
                "1 colher de chá de gengibre ralado",
                "Hortelã fresca"
            ],
            "recipe": [
                "Adicione todos os ingredientes no liquidificador.",
                "Bata por 2-3 minutos até ficar homogêneo.",
                "Prove e ajuste o sabor se necessário.",
                "Sirva imediatamente com gelo.",
                "Decore com hortelã fresca."
            ]
        },
        {
            "name": "Torrada Integral com Abacate",
            "calories": 220,
            "protein": 8,
            "carbs": 25,
            "fat": 12,
            "time": "5 min",
            "category": "Café da Manhã",
            "ingredients": [
                "2 fatias de pão integral",
                "1/2 abacate maduro",
                "Sal e pimenta",
                "Suco de 1/2 limão",
                "Tomate cereja",
                "Rúcula",
                "Sementes de gergelim"
            ],
            "recipe": [
                "Toste o pão integral até ficar dourado.",
                "Amasse o abacate com garfo em tigela.",
                "Tempere com limão, sal e pimenta.",
                "Espalhe sobre as torradas.",
                "Decore com tomate cereja e rúcula.",
                "Finalize com sementes de gergelim."
            ]
        },
        {
            "name": "Panquecas de Banana Light",
            "calories": 250,
            "protein": 12,
            "carbs": 35,
            "fat": 8,
            "time": "12 min",
            "category": "Café da Manhã",
            "ingredients": [
                "1 banana madura",
                "2 ovos",
                "2 colheres de sopa de aveia",
                "1 colher de chá de canela",
                "1 colher de chá de fermento",
                "1 colher de sopa de mel",
                "Frutas vermelhas para decorar"
            ],
            "recipe": [
                "Amasse a banana em uma tigela.",
                "Adicione os ovos e misture bem.",
                "Incorpore a aveia, canela e fermento.",
                "Aqueça uma frigideira antiaderente.",
                "Despeje pequenas porções da massa.",
                "Cozinhe por 2-3 minutos de cada lado.",
                "Sirva com mel e frutas vermelhas."
            ]
        },
        
        # ALMOÇO - PERDER PESO
        {
            "name": "Salada de Frango Grelhado",
            "calories": 420,
            "protein": 35,
            "carbs": 15,
            "fat": 25,
            "time": "15 min",
            "category": "Almoço",
            "ingredients": [
                "150g de peito de frango",
                "2 xícaras de folhas verdes mistas",
                "1/2 pepino fatiado",
                "10 tomates cereja",
                "1/2 abacate fatiado",
                "2 colheres de sopa de azeite de oliva",
                "1 colher de sopa de vinagre balsâmico",
                "Sal e pimenta a gosto"
            ],
            "recipe": [
                "Tempere o frango com sal e pimenta.",
                "Aqueça uma grelha ou frigideira antiaderente.",
                "Grelhe o frango por 6-8 minutos de cada lado.",
                "Enquanto isso, lave e seque bem as folhas verdes.",
                "Corte o pepino, tomates e abacate.",
                "Monte a salada em um prato grande.",
                "Misture o azeite com vinagre balsâmico.",
                "Corte o frango em fatias e coloque sobre a salada.",
                "Regue com o molho e sirva imediatamente."
            ]
        },
        {
            "name": "Salmão com Legumes Assados",
            "calories": 380,
            "protein": 30,
            "carbs": 12,
            "fat": 22,
            "time": "20 min",
            "category": "Almoço",
            "ingredients": [
                "150g de filé de salmão",
                "1 xícara de brócolis",
                "1 cenoura média",
                "1/2 pimentão vermelho",
                "2 colheres de sopa de azeite",
                "1 dente de alho",
                "Suco de 1/2 limão",
                "Sal, pimenta e ervas finas"
            ],
            "recipe": [
                "Preaqueça o forno a 200°C.",
                "Corte os legumes em pedaços uniformes.",
                "Tempere o salmão com sal, pimenta e limão.",
                "Em uma assadeira, coloque os legumes com azeite e alho.",
                "Asse os legumes por 10 minutos.",
                "Adicione o salmão na assadeira.",
                "Asse por mais 12-15 minutos até o salmão ficar dourado.",
                "Tempere com ervas finas antes de servir."
            ]
        },
        {
            "name": "Quinoa com Legumes",
            "calories": 350,
            "protein": 14,
            "carbs": 55,
            "fat": 12,
            "time": "20 min",
            "category": "Almoço",
            "ingredients": [
                "1/2 xícara de quinoa",
                "1 xícara de água",
                "1/2 pimentão vermelho",
                "1/2 pimentão amarelo",
                "1/2 abobrinha",
                "1 cenoura pequena",
                "2 colheres de sopa de azeite",
                "Sal, pimenta e cominho"
            ],
            "recipe": [
                "Lave a quinoa e cozinhe em água fervente por 15 min.",
                "Corte todos os legumes em cubos pequenos.",
                "Aqueça o azeite em frigideira grande.",
                "Refogue a cenoura por 3 minutos.",
                "Adicione os pimentões e abobrinha.",
                "Tempere com sal, pimenta e cominho.",
                "Cozinhe por 8-10 minutos mexendo sempre.",
                "Misture com a quinoa cozida e sirva."
            ]
        },
        {
            "name": "Wrap de Atum Light",
            "calories": 300,
            "protein": 25,
            "carbs": 35,
            "fat": 10,
            "time": "10 min",
            "category": "Almoço",
            "ingredients": [
                "1 tortilha integral",
                "1 lata de atum em água",
                "2 colheres de sopa de iogurte grego",
                "1/4 de cebola roxa",
                "1/2 tomate",
                "Folhas de alface",
                "1 colher de chá de sumo de limão",
                "Sal e pimenta"
            ],
            "recipe": [
                "Escorre bem o atum e coloque em tigela.",
                "Misture o atum com o iogurte grego.",
                "Adicione o sumo de limão e tempere.",
                "Corte a cebola e o tomate em pedaços pequenos.",
                "Aqueça a tortilha levemente.",
                "Espalhe a mistura de atum na tortilha.",
                "Adicione os vegetais e a alface.",
                "Enrola bem e corte ao meio."
            ]
        },
        {
            "name": "Sopa de Legumes Detox",
            "calories": 220,
            "protein": 8,
            "carbs": 35,
            "fat": 6,
            "time": "25 min",
            "category": "Almoço",
            "ingredients": [
                "1/2 cenoura cortada em cubos",
                "1/2 abobrinha em cubos",
                "1/2 xícara de brócolis",
                "1 tomate picado",
                "1/2 cebola picada",
                "2 dentes de alho",
                "500ml de caldo de legumes",
                "1 colher de sopa de azeite",
                "Ervas frescas"
            ],
            "recipe": [
                "Aqueça o azeite em panela média.",
                "Refogue cebola e alho até dourar.",
                "Adicione cenoura e cozinhe por 5 minutos.",
                "Acrescente abobrinha e brócolis.",
                "Adicione o tomate e o caldo de legumes.",
                "Deixe ferver e cozinhe por 15 minutos.",
                "Tempere com sal, pimenta e ervas frescas.",
                "Sirva quente em tigela funda."
            ]
        },
        
        # JANTAR - PERDER PESO
        {
            "name": "Peixe Branco com Aspargos",
            "calories": 320,
            "protein": 28,
            "carbs": 8,
            "fat": 18,
            "time": "18 min",
            "category": "Jantar",
            "ingredients": [
                "150g de filé de peixe branco",
                "1 maço de aspargos",
                "2 colheres de sopa de azeite",
                "1 dente de alho",
                "Suco de 1/2 limão",
                "Sal, pimenta e ervas finas",
                "Tomate cereja para decorar"
            ],
            "recipe": [
                "Tempere o peixe com sal, pimenta e limão.",
                "Lave e corte as pontas dos aspargos.",
                "Aqueça o azeite em frigideira.",
                "Grelhe o peixe por 4-5 minutos de cada lado.",
                "Em outra panela, refogue os aspargos com alho.",
                "Cozinhe por 5-6 minutos até ficarem tenros.",
                "Sirva o peixe com os aspargos.",
                "Decore com tomate cereja e ervas."
            ]
        },
        {
            "name": "Frango com Vegetais ao Vapor",
            "calories": 340,
            "protein": 32,
            "carbs": 18,
            "fat": 16,
            "time": "25 min",
            "category": "Jantar",
            "ingredients": [
                "150g de peito de frango",
                "Abobrinha",
                "Berinjela",
                "Pimentão",
                "Cebola",
                "2 colheres de sopa de azeite",
                "Temperos mediterrâneos",
                "Sal e pimenta"
            ],
            "recipe": [
                "Corte o frango em cubos pequenos.",
                "Tempere bem com sal e temperos.",
                "Corte todos os vegetais em pedaços uniformes.",
                "Aqueça o azeite em frigideira grande.",
                "Refogue o frango até dourar.",
                "Adicione os vegetais e refogue por 8 minutos.",
                "Tempere com sal e pimenta.",
                "Sirva quente."
            ]
        },
        {
            "name": "Berinjela Recheada Light",
            "calories": 280,
            "protein": 15,
            "carbs": 25,
            "fat": 16,
            "time": "35 min",
            "category": "Jantar",
            "ingredients": [
                "1 berinjela média",
                "100g de ricota light",
                "1 tomate picado",
                "Manjericão fresco",
                "2 colheres de sopa de azeite",
                "1 dente de alho",
                "Sal e pimenta"
            ],
            "recipe": [
                "Corte a berinjela ao meio longitudinalmente.",
                "Retire a polpa com cuidado.",
                "Refogue a polpa com alho e tomate.",
                "Misture com ricota e manjericão.",
                "Tempere com sal e pimenta.",
                "Recheie as cascas da berinjela.",
                "Asse no forno a 180°C por 25 minutos.",
                "Sirva quente."
            ]
        },
        
        # LANCHE - PERDER PESO
        {
            "name": "Iogurte Grego com Nozes",
            "calories": 180,
            "protein": 15,
            "carbs": 8,
            "fat": 12,
            "time": "2 min",
            "category": "Lanche",
            "ingredients": [
                "150g de iogurte grego natural",
                "30g de nozes picadas",
                "1 colher de chá de mel",
                "1 pitada de canela",
                "Algumas gotas de essência de baunilha"
            ],
            "recipe": [
                "Coloque o iogurte grego em uma tigela.",
                "Adicione a essência de baunilha e misture.",
                "Regue com mel por cima.",
                "Adicione as nozes picadas.",
                "Polvilhe com canela.",
                "Sirva imediatamente gelado."
            ]
        },
        {
            "name": "Maçã com Pasta de Amêndoa",
            "calories": 190,
            "protein": 6,
            "carbs": 20,
            "fat": 12,
            "time": "3 min",
            "category": "Lanche",
            "ingredients": [
                "1 maçã verde média",
                "2 colheres de sopa de pasta de amêndoa",
                "1 pitada de canela",
                "1 colher de chá de mel (opcional)",
                "Algumas gotas de limão"
            ],
            "recipe": [
                "Lave e corte a maçã em fatias médias.",
                "Pingue algumas gotas de limão nas fatias.",
                "Espalhe a pasta de amêndoa sobre as fatias.",
                "Polvilhe canela por cima.",
                "Se desejar, regue levemente com mel.",
                "Sirva imediatamente para manter crocante."
            ]
        },
        {
            "name": "Mix de Oleaginosas Light",
            "calories": 200,
            "protein": 8,
            "carbs": 8,
            "fat": 16,
            "time": "1 min",
            "category": "Lanche",
            "ingredients": [
                "15g de amêndoas",
                "10g de nozes",
                "5g de castanha do Brasil",
                "Canela em pó",
                "Sal marinho"
            ],
            "recipe": [
                "Misture todas as oleaginosas em uma tigela.",
                "Polvilhe levemente com canela.",
                "Adicione uma pitada de sal marinho.",
                "Misture bem todos os ingredientes.",
                "Sirva em porção individual.",
                "Conserve o restante em recipiente hermético."
            ]
        }
    ],
    "maintain": [
        # CAFÉ DA MANHÃ - MANTER PESO
        {
            "name": "Panquecas de Aveia",
            "calories": 420,
            "protein": 18,
            "carbs": 45,
            "fat": 15,
            "time": "15 min",
            "category": "Café da Manhã",
            "ingredients": [
                "1/2 xícara de aveia em flocos",
                "2 ovos inteiros",
                "1/4 xícara de leite",
                "1 banana madura",
                "1 colher de chá de fermento",
                "1 colher de chá de mel",
                "Canela a gosto",
                "Frutas vermelhas para decorar"
            ],
            "recipe": [
                "No liquidificador, bata a banana com os ovos e leite.",
                "Adicione a aveia, fermento, mel e canela.",
                "Bata até obter uma massa homogênea.",
                "Deixe descansar por 5 minutos.",
                "Aqueça uma frigideira antiaderente.",
                "Despeje pequenas porções da massa na frigideira.",
                "Cozinhe por 2-3 minutos de cada lado até dourar.",
                "Sirva com frutas vermelhas."
            ]
        },
        {
            "name": "Torrada de Abacate com Ovo",
            "calories": 380,
            "protein": 18,
            "carbs": 30,
            "fat": 22,
            "time": "10 min",
            "category": "Café da Manhã",
            "ingredients": [
                "2 fatias de pão integral",
                "1 abacate maduro",
                "1 ovo",
                "1 colher de sopa de azeite",
                "Sal e pimenta a gosto",
                "Suco de 1/2 limão",
                "Temperos verdes",
                "Tomate cereja para decorar"
            ],
            "recipe": [
                "Toste as fatias de pão integral.",
                "Amasse o abacate com garfo em tigela.",
                "Tempere o abacate com limão, sal e pimenta.",
                "Faça um ovo pochê em água com vinagre.",
                "Espalhe o abacate sobre as torradas.",
                "Coloque o ovo pochê por cima.",
                "Tempere com sal, pimenta e ervas.",
                "Decore com tomate cereja cortado."
            ]
        },
        {
            "name": "Aveia com Frutas e Granola",
            "calories": 450,
            "protein": 15,
            "carbs": 55,
            "fat": 18,
            "time": "8 min",
            "category": "Café da Manhã",
            "ingredients": [
                "1/2 xícara de aveia em flocos",
                "1 xícara de leite",
                "1/4 xícara de granola",
                "1/2 banana fatiada",
                "1/4 xícara de frutas vermelhas",
                "1 colher de sopa de mel",
                "1 colher de sopa de sementes de chia",
                "Canela em pó"
            ],
            "recipe": [
                "Aqueça o leite em panela média.",
                "Adicione a aveia e cozinhe por 5 minutos.",
                "Mexa ocasionalmente até ficar cremoso.",
                "Retire do fogo e adicione mel e canela.",
                "Coloque em tigela e adicione granola.",
                "Decore com banana e frutas vermelhas.",
                "Finalize com sementes de chia.",
                "Sirva quente."
            ]
        },
        {
            "name": "Omelete de Queijo e Ervas",
            "calories": 320,
            "protein": 22,
            "carbs": 5,
            "fat": 24,
            "time": "8 min",
            "category": "Café da Manhã",
            "ingredients": [
                "3 ovos",
                "50g de queijo mussarela",
                "Ervas frescas (manjericão, orégano)",
                "2 colheres de sopa de azeite",
                "Sal e pimenta",
                "Tomate cereja",
                "Rúcula"
            ],
            "recipe": [
                "Bata os ovos em tigela com sal e pimenta.",
                "Aqueça o azeite em frigideira antiaderente.",
                "Despeje os ovos batidos na frigideira.",
                "Adicione o queijo por cima.",
                "Cozinhe por 3-4 minutos até firmar embaixo.",
                "Dobre a omelete ao meio.",
                "Sirva com tomate cereja e rúcula.",
                "Tempere com ervas frescas."
            ]
        },
        
        # ALMOÇO - MANTER PESO
        {
            "name": "Arroz Integral com Carne",
            "calories": 550,
            "protein": 40,
            "carbs": 50,
            "fat": 18,
            "time": "25 min",
            "category": "Almoço",
            "ingredients": [
                "150g de carne magra (alcatra)",
                "1/2 xícara de arroz integral",
                "1/2 cebola picada",
                "2 dentes de alho",
                "1 tomate picado",
                "2 colheres de sopa de óleo",
                "Sal, pimenta e temperos verdes",
                "Ervas finas"
            ],
            "recipe": [
                "Cozinhe o arroz integral conforme instruções da embalagem.",
                "Corte a carne em cubos pequenos.",
                "Tempere a carne com sal e pimenta.",
                "Aqueça o óleo em uma panela.",
                "Refogue a cebola e alho até dourar.",
                "Adicione a carne e doure por todos os lados.",
                "Acrescente o tomate e cozinhe por 5 minutos.",
                "Tempere com ervas finas e sirva com o arroz."
            ]
        },
        {
            "name": "Quinoa com Legumes Coloridos",
            "calories": 460,
            "protein": 16,
            "carbs": 70,
            "fat": 14,
            "time": "20 min",
            "category": "Almoço",
            "ingredients": [
                "1/2 xícara de quinoa",
                "1 xícara de água",
                "1/2 pimentão vermelho",
                "1/2 pimentão amarelo",
                "1/2 abobrinha",
                "1 cenoura pequena",
                "2 colheres de sopa de azeite",
                "Sal, pimenta e cominho",
                "Salsinha fresca"
            ],
            "recipe": [
                "Lave a quinoa e cozinhe em água fervente por 15 min.",
                "Corte todos os legumes em cubos pequenos.",
                "Aqueça o azeite em frigideira grande.",
                "Refogue a cenoura por 3 minutos.",
                "Adicione os pimentões e abobrinha.",
                "Tempere com sal, pimenta e cominho.",
                "Cozinhe por 8-10 minutos mexendo sempre.",
                "Misture com a quinoa cozida e sirva com salsinha."
            ]
        },
        {
            "name": "Salmão Grelhado com Salada",
            "calories": 480,
            "protein": 35,
            "carbs": 20,
            "fat": 28,
            "time": "18 min",
            "category": "Almoço",
            "ingredients": [
                "150g de salmão",
                "2 xícaras de folhas verdes",
                "1/2 pepino fatiado",
                "10 tomates cereja",
                "1/4 de abacate",
                "2 colheres de sopa de azeite",
                "1 colher de sopa de vinagre balsâmico",
                "Sal, pimenta e ervas"
            ],
            "recipe": [
                "Tempere o salmão com sal, pimenta e ervas.",
                "Grelhe o salmão por 6-8 minutos de cada lado.",
                "Prepare a salada com folhas verdes.",
                "Adicione pepino, tomates e abacate.",
                "Misture azeite com vinagre balsâmico.",
                "Corte o salmão em fatias.",
                "Monte a salada e coloque o salmão por cima.",
                "Regue com o molho e sirva."
            ]
        },
        {
            "name": "Wrap Integral Completo",
            "calories": 420,
            "protein": 25,
            "carbs": 45,
            "fat": 16,
            "time": "12 min",
            "category": "Almoço",
            "ingredients": [
                "1 tortilha integral grande",
                "100g de peito de frango grelhado",
                "2 folhas de alface",
                "2 fatias de tomate",
                "2 colheres de sopa de queijo cream cheese",
                "1/4 de abacate",
                "1 colher de sopa de azeite",
                "Temperos: sal, pimenta, páprica"
            ],
            "recipe": [
                "Grelhe o frango temperado com sal e páprica.",
                "Deixe esfriar e corte em tiras finas.",
                "Aqueça a tortilha levemente na frigideira.",
                "Espalhe o cream cheese sobre a tortilha.",
                "Adicione alface, tomate e abacate fatiado.",
                "Coloque as tiras de frango por cima.",
                "Enrole firmemente e corte ao meio.",
                "Sirva imediatamente."
            ]
        },
        {
            "name": "Massa com Frango e Pesto",
            "calories": 520,
            "protein": 22,
            "carbs": 68,
            "fat": 20,
            "time": "15 min",
            "category": "Almoço",
            "ingredients": [
                "100g de macarrão penne integral",
                "150g de peito de frango",
                "2 colheres de sopa de pesto",
                "1/2 cebola picada",
                "2 dentes de alho",
                "2 colheres de sopa de azeite",
                "Queijo parmesão ralado",
                "Sal e pimenta"
            ],
            "recipe": [
                "Cozinhe o macarrão conforme instruções da embalagem.",
                "Corte o frango em cubos e tempere.",
                "Aqueça o azeite e doure o frango.",
                "Adicione cebola e alho, refogue até dourar.",
                "Misture o macarrão escorrido com o frango.",
                "Adicione o pesto e misture bem.",
                "Finalize com parmesão ralado.",
                "Sirva quente."
            ]
        },
        
        # JANTAR - MANTER PESO
        {
            "name": "Frango com Batata Doce",
            "calories": 480,
            "protein": 35,
            "carbs": 45,
            "fat": 12,
            "time": "30 min",
            "category": "Jantar",
            "ingredients": [
                "150g de peito de frango",
                "200g de batata doce",
                "1 colher de sopa de azeite",
                "1 colher de chá de páprica",
                "1/2 colher de chá de alecrim",
                "Sal e pimenta a gosto",
                "1 dente de alho",
                "Salsinha para finalizar"
            ],
            "recipe": [
                "Preaqueça o forno a 200°C.",
                "Descasque e corte a batata doce em cubos.",
                "Tempere o frango com sal, pimenta e páprica.",
                "Em uma assadeira, coloque as batatas com azeite e alecrim.",
                "Asse as batatas por 15 minutos.",
                "Adicione o frango temperado na assadeira.",
                "Asse por mais 15-20 minutos até dourar.",
                "Finalize com salsinha picada antes de servir."
            ]
        },
        {
            "name": "Picanha com Batata",
            "calories": 520,
            "protein": 38,
            "carbs": 35,
            "fat": 25,
            "time": "20 min",
            "category": "Jantar",
            "ingredients": [
                "150g de picanha",
                "200g de batata",
                "1 colher de sopa de azeite",
                "Sal grosso a gosto",
                "Pimenta do reino",
                "Alecrim fresco",
                "2 dentes de alho",
                "Manteiga para finalizar"
            ],
            "recipe": [
                "Preaqueça o forno a 200°C.",
                "Corte as batatas em pedaços médios.",
                "Tempere a picanha com sal grosso e pimenta.",
                "Tempere as batatas com azeite, sal e alecrim.",
                "Asse as batatas por 20 minutos.",
                "Grelhe a picanha em frigideira bem quente.",
                "Cozinhe 4-5 minutos de cada lado.",
                "Finalize com manteiga e alho."
            ]
        },
        {
            "name": "Salmão com Quinoa",
            "calories": 450,
            "protein": 30,
            "carbs": 40,
            "fat": 22,
            "time": "25 min",
            "category": "Jantar",
            "ingredients": [
                "150g de salmão",
                "1/2 xícara de quinoa",
                "1 xícara de água",
                "2 colheres de sopa de azeite",
                "1 dente de alho",
                "Suco de 1/2 limão",
                "Sal, pimenta e ervas finas",
                "Aspargos para acompanhar"
            ],
            "recipe": [
                "Cozinhe a quinoa em água fervente por 15 minutos.",
                "Tempere o salmão com sal, pimenta e limão.",
                "Aqueça o azeite em frigideira.",
                "Grelhe o salmão por 6-8 minutos de cada lado.",
                "Refogue os aspargos com alho.",
                "Sirva o salmão sobre a quinoa.",
                "Acompanhe com os aspargos.",
                "Tempere com ervas finas."
            ]
        },
        
        # LANCHE - MANTER PESO
        {
            "name": "Smoothie Proteico",
            "calories": 280,
            "protein": 25,
            "carbs": 30,
            "fat": 8,
            "time": "5 min",
            "category": "Lanche",
            "ingredients": [
                "1 scoop de whey protein (baunilha)",
                "1 banana média",
                "200ml de leite",
                "1 colher de sopa de aveia",
                "1/2 colher de chá de canela",
                "Gelo a gosto",
                "Frutas vermelhas para decorar"
            ],
            "recipe": [
                "Adicione todos os ingredientes no liquidificador.",
                "Bata por 1-2 minutos até ficar cremoso.",
                "Prove e ajuste a doçura se necessário.",
                "Adicione gelo se preferir mais gelado.",
                "Sirva em um copo alto.",
                "Decore com frutas vermelhas por cima."
            ]
        },
        {
            "name": "Chocolate com Amêndoas",
            "calories": 240,
            "protein": 8,
            "carbs": 12,
            "fat": 20,
            "time": "1 min",
            "category": "Lanche",
            "ingredients": [
                "30g de chocolate 70% cacau",
                "20g de amêndoas tostadas",
                "1 pitada de sal marinho",
                "1 colher de chá de mel (opcional)"
            ],
            "recipe": [
                "Quebre o chocolate em pedaços pequenos.",
                "Toste levemente as amêndoas se necessário.",
                "Coloque chocolate e amêndoas em tigela.",
                "Adicione uma pitada de sal marinho.",
                "Se desejar, regue com mel.",
                "Consuma com moderação como sobremesa."
            ]
        },
        {
            "name": "Barra de Cereal Caseira",
            "calories": 220,
            "protein": 8,
            "carbs": 32,
            "fat": 8,
            "time": "10 min + 30 min forno",
            "category": "Lanche",
            "ingredients": [
                "1 xícara de aveia",
                "1/2 xícara de mel",
                "1/4 xícara de castanhas picadas",
                "1/4 xícara de frutas secas",
                "2 colheres de sopa de sementes",
                "1 colher de chá de canela",
                "1 pitada de sal"
            ],
            "recipe": [
                "Misture todos os ingredientes secos em tigela.",
                "Aqueça o mel até ficar líquido.",
                "Adicione o mel aos ingredientes secos.",
                "Misture bem até formar uma massa pegajosa.",
                "Pressione em forma forrada com papel manteiga.",
                "Asse no forno a 180°C por 30 minutos.",
                "Deixe esfriar antes de cortar em barras."
            ]
        }
    ],
    "gain": [
        # CAFÉ DA MANHÃ - GANHAR PESO
        {
            "name": "Vitamina Calórica",
            "calories": 520,
            "protein": 25,
            "carbs": 65,
            "fat": 18,
            "time": "5 min",
            "category": "Café da Manhã",
            "ingredients": [
                "1 banana média",
                "200ml de leite integral",
                "2 colheres de sopa de aveia",
                "1 scoop de whey protein",
                "1 colher de sopa de pasta de amendoim",
                "1 colher de sopa de mel",
                "1 colher de chá de cacau em pó",
                "Gelo a gosto"
            ],
            "recipe": [
                "Adicione a banana cortada no liquidificador.",
                "Acrescente o leite integral.",
                "Adicione a aveia, whey protein e pasta de amendoim.",
                "Coloque o mel e o cacau em pó.",
                "Adicione gelo conforme preferência.",
                "Bata por 2-3 minutos até ficar cremoso.",
                "Sirva imediatamente em copo grande."
            ]
        },
        {
            "name": "Shake Verde Proteico",
            "calories": 480,
            "protein": 30,
            "carbs": 45,
            "fat": 20,
            "time": "5 min",
            "category": "Café da Manhã",
            "ingredients": [
                "1 xícara de espinafre fresco",
                "1 banana média",
                "1 scoop de whey protein",
                "200ml de leite de coco",
                "1 colher de sopa de pasta de amendoim",
                "1 colher de sopa de aveia",
                "1 colher de chá de mel",
                "Gelo a gosto"
            ],
            "recipe": [
                "Adicione todos os ingredientes no liquidificador.",
                "Comece com o líquido e espinafre.",
                "Adicione banana, proteína e pasta de amendoim.",
                "Coloque aveia e mel para adoçar.",
                "Bata por 2-3 minutos até ficar homogêneo.",
                "Adicione gelo se preferir mais gelado.",
                "Sirva imediatamente em copo grande."
            ]
        },
        {
            "name": "Panqueca Americana Proteica",
            "calories": 580,
            "protein": 28,
            "carbs": 65,
            "fat": 24,
            "time": "15 min",
            "category": "Café da Manhã",
            "ingredients": [
                "1/2 xícara de aveia",
                "1 scoop de whey protein",
                "2 ovos inteiros",
                "1/4 xícara de leite integral",
                "1 banana madura",
                "1 colher de chá de fermento",
                "2 colheres de sopa de mel",
                "Frutas vermelhas",
                "Pasta de amendoim"
            ],
            "recipe": [
                "No liquidificador, bata a aveia com whey protein.",
                "Adicione os ovos, leite e banana.",
                "Bata até obter uma massa homogênea.",
                "Adicione fermento e mel.",
                "Deixe descansar por 5 minutos.",
                "Aqueça uma frigideira antiaderente.",
                "Despeje porções maiores da massa.",
                "Cozinhe por 3-4 minutos de cada lado.",
                "Sirva empilhadas com pasta de amendoim."
            ]
        },
        {
            "name": "Bowl de Granola Hipercalórico",
            "calories": 620,
            "protein": 22,
            "carbs": 78,
            "fat": 28,
            "time": "5 min",
            "category": "Café da Manhã",
            "ingredients": [
                "1/2 xícara de granola",
                "200ml de iogurte integral",
                "1/2 banana fatiada",
                "1/4 xícara de frutas vermelhas",
                "2 colheres de sopa de mel",
                "1 colher de sopa de castanhas picadas",
                "1 colher de sopa de coco ralado",
                "1 colher de sopa de pasta de amendoim"
            ],
            "recipe": [
                "Coloque o iogurte em uma tigela grande.",
                "Adicione a granola por cima.",
                "Decore com banana e frutas vermelhas.",
                "Regue generosamente com mel.",
                "Adicione as castanhas e coco ralado.",
                "Finalize com pasta de amendoim.",
                "Misture tudo antes de comer.",
                "Sirva imediatamente."
            ]
        },
        {
            "name": "Torrada de Abacate com Ovo e Amendoim",
            "calories": 520,
            "protein": 18,
            "carbs": 45,
            "fat": 32,
            "time": "5 min",
            "category": "Café da Manhã",
            "ingredients": [
                "2 fatias de pão integral",
                "1 abacate maduro",
                "1 ovo",
                "2 colheres de sopa de pasta de amendoim",
                "Sal e pimenta",
                "Suco de 1/2 limão",
                "Tomate cereja",
                "Sementes de gergelim"
            ],
            "recipe": [
                "Toste o pão integral até ficar dourado.",
                "Espalhe pasta de amendoim nas torradas.",
                "Amasse o abacate com limão, sal e pimenta.",
                "Faça um ovo frito.",
                "Espalhe o abacate sobre as torradas.",
                "Coloque o ovo por cima.",
                "Decore com tomate cereja.",
                "Finalize com sementes de gergelim."
            ]
        },
        
        # ALMOÇO - GANHAR PESO
        {
            "name": "Massa com Frango",
            "calories": 680,
            "protein": 45,
            "carbs": 75,
            "fat": 20,
            "time": "20 min",
            "category": "Almoço",
            "ingredients": [
                "100g de macarrão penne integral",
                "150g de peito de frango",
                "2 colheres de sopa de azeite",
                "1/2 cebola picada",
                "2 dentes de alho",
                "200ml de creme de leite light",
                "2 colheres de sopa de queijo parmesão",
                "Temperos verdes a gosto",
                "Sal e pimenta"
            ],
            "recipe": [
                "Cozinhe o macarrão conforme instruções da embalagem.",
                "Corte o frango em cubos e tempere com sal e pimenta.",
                "Aqueça o azeite e doure o frango.",
                "Adicione a cebola e alho, refogue até dourar.",
                "Acrescente o creme de leite e deixe ferver.",
                "Misture o macarrão escorrido ao molho.",
                "Finalize com parmesão e temperos verdes.",
                "Sirva quente imediatamente."
            ]
        },
        {
            "name": "Arroz Integral com Carne Cremoso",
            "calories": 620,
            "protein": 24,
            "carbs": 78,
            "fat": 26,
            "time": "30 min",
            "category": "Almoço",
            "ingredients": [
                "1/2 xícara de arroz arbóreo",
                "150g de cogumelos variados",
                "500ml de caldo de legumes",
                "50g de queijo parmesão",
                "2 colheres de sopa de vinho branco",
                "2 colheres de sopa de manteiga",
                "1/2 cebola picada",
                "2 dentes de alho",
                "Sal e pimenta"
            ],
            "recipe": [
                "Refogue a cebola e alho na manteiga.",
                "Adicione os cogumelos e refogue por 5 minutos.",
                "Adicione o arroz e mexa por 2 minutos.",
                "Adicione o vinho branco e deixe evaporar.",
                "Vá adicionando caldo quente aos poucos.",
                "Mexa constantemente até o arroz ficar cremoso.",
                "Finalize com queijo parmesão e manteiga.",
                "Tempere com sal e pimenta."
            ]
        },
        {
            "name": "Sanduíche de Frango Completo",
            "calories": 580,
            "protein": 38,
            "carbs": 52,
            "fat": 24,
            "time": "12 min",
            "category": "Almoço",
            "ingredients": [
                "1 pão francês",
                "150g de peito de frango grelhado",
                "2 fatias de queijo mussarela",
                "2 fatias de bacon",
                "1/4 de abacate",
                "2 colheres de sopa de maionese",
                "Alface",
                "Tomate",
                "Sal e pimenta"
            ],
            "recipe": [
                "Grelhe o frango temperado com sal e pimenta.",
                "Frite o bacon até ficar crocante.",
                "Toste o pão francês.",
                "Espalhe maionese nas fatias do pão.",
                "Monte o sanduíche com todos os ingredientes.",
                "Adicione alface e tomate.",
                "Feche o sanduíche.",
                "Sirva quente."
            ]
        },
        {
            "name": "Massa com Frango ao Forno",
            "calories": 650,
            "protein": 32,
            "carbs": 68,
            "fat": 28,
            "time": "40 min",
            "category": "Almoço",
            "ingredients": [
                "150g de massa integral",
                "200ml de molho de tomate",
                "100g de queijo mussarela",
                "50g de queijo parmesão",
                "100g de peperoni",
                "Manjericão fresco",
                "2 colheres de sopa de azeite",
                "Sal e pimenta"
            ],
            "recipe": [
                "Cozinhe a massa conforme instruções.",
                "Abra a massa em forma untada.",
                "Adicione molho de tomate por cima.",
                "Coloque queijos e peperoni.",
                "Tempere com sal, pimenta e manjericão.",
                "Regue com azeite.",
                "Asse no forno a 200°C por 25 minutos.",
                "Sirva quente."
            ]
        },
        {
            "name": "Bowl de Quinoa Completo",
            "calories": 590,
            "protein": 28,
            "carbs": 72,
            "fat": 22,
            "time": "25 min",
            "category": "Almoço",
            "ingredients": [
                "1/2 xícara de quinoa",
                "150g de frango grelhado",
                "1/4 de abacate",
                "50g de queijo feta",
                "1/2 pepino",
                "10 tomates cereja",
                "2 colheres de sopa de molho tahine",
                "Sementes de girassol"
            ],
            "recipe": [
                "Cozinhe a quinoa em água fervente por 15 min.",
                "Grelhe o frango temperado.",
                "Corte o abacate, pepino e tomates.",
                "Monte o bowl com quinoa como base.",
                "Adicione frango, abacate e vegetais.",
                "Espalhe queijo feta por cima.",
                "Regue com molho tahine.",
                "Finalize com sementes de girassol."
            ]
        },
        
        # JANTAR - GANHAR PESO
        {
            "name": "Picanha com Batata Completa",
            "calories": 720,
            "protein": 42,
            "carbs": 58,
            "fat": 32,
            "time": "20 min",
            "category": "Jantar",
            "ingredients": [
                "150g de picanha",
                "200g de batata",
                "1 colher de sopa de azeite",
                "Sal grosso a gosto",
                "Pimenta do reino",
                "Alecrim fresco",
                "2 dentes de alho",
                "Manteiga para finalizar"
            ],
            "recipe": [
                "Preaqueça o forno a 200°C.",
                "Corte as batatas em pedaços médios.",
                "Tempere a picanha com sal grosso e pimenta.",
                "Tempere as batatas com azeite, sal e alecrim.",
                "Asse as batatas por 20 minutos.",
                "Grelhe a picanha em frigideira bem quente.",
                "Cozinhe 4-5 minutos de cada lado.",
                "Finalize com manteiga e alho."
            ]
        },
        {
            "name": "Carne com Arroz e Feijão",
            "calories": 620,
            "protein": 42,
            "carbs": 55,
            "fat": 22,
            "time": "25 min",
            "category": "Jantar",
            "ingredients": [
                "150g de carne bovina (contrafilé)",
                "1/3 xícara de arroz branco",
                "1/2 xícara de feijão cozido",
                "1/2 cebola picada",
                "2 dentes de alho",
                "1 tomate picado",
                "2 colheres de sopa de óleo",
                "Temperos: louro, sal, pimenta",
                "Cebolinha para finalizar"
            ],
            "recipe": [
                "Cozinhe o arroz branco tradicionalmente.",
                "Aqueça o feijão em uma panela separada.",
                "Corte a carne em bifes e tempere.",
                "Grelhe a carne em frigideira quente.",
                "Em outra panela, refogue cebola e alho.",
                "Adicione o tomate e temperos ao refogado.",
                "Monte o prato com arroz, feijão e carne.",
                "Finalize com cebolinha picada."
            ]
        },
        {
            "name": "Wrap de Frango",
            "calories": 580,
            "protein": 42,
            "carbs": 45,
            "fat": 24,
            "time": "15 min",
            "category": "Jantar",
            "ingredients": [
                "1 tortilha integral grande",
                "150g de peito de frango grelhado",
                "2 folhas de alface",
                "2 fatias de tomate",
                "2 colheres de sopa de queijo cream cheese",
                "1/4 de abacate",
                "1 colher de sopa de azeite",
                "Temperos: sal, pimenta, páprica"
            ],
            "recipe": [
                "Grelhe o frango temperado com sal e páprica.",
                "Deixe esfriar e corte em tiras finas.",
                "Aqueça a tortilha levemente na frigideira.",
                "Espalhe o cream cheese sobre a tortilha.",
                "Adicione alface, tomate e abacate fatiado.",
                "Coloque as tiras de frango por cima.",
                "Enrole firmemente e corte ao meio.",
                "Sirva imediatamente."
            ]
        },
        {
            "name": "Salmão com Quinoa",
            "calories": 650,
            "protein": 38,
            "carbs": 48,
            "fat": 32,
            "time": "25 min",
            "category": "Jantar",
            "ingredients": [
                "150g de salmão",
                "1/2 xícara de quinoa",
                "1 xícara de água",
                "2 colheres de sopa de manteiga",
                "Suco de 1/2 limão",
                "Aspargos",
                "Temperos mediterrâneos",
                "Sal e pimenta"
            ],
            "recipe": [
                "Cozinhe a quinoa em água fervente por 15 minutos.",
                "Tempere o salmão com temperos mediterrâneos.",
                "Aqueça manteiga em frigideira.",
                "Grelhe o salmão por 6-8 minutos de cada lado.",
                "Refogue os aspargos com manteiga.",
                "Sirva o salmão sobre a quinoa.",
                "Acompanhe com os aspargos.",
                "Finalize com limão."
            ]
        },
        {
            "name": "Frango à Parmegiana",
            "calories": 680,
            "protein": 48,
            "carbs": 42,
            "fat": 32,
            "time": "35 min",
            "category": "Jantar",
            "ingredients": [
                "150g de peito de frango",
                "200ml de molho de tomate",
                "100g de queijo mussarela",
                "50g de queijo parmesão",
                "Farinha de rosca",
                "2 ovos",
                "1/2 xícara de arroz",
                "Sal e pimenta"
            ],
            "recipe": [
                "Empane o frango com farinha, ovo e farinha de rosca.",
                "Frite o frango até dourar.",
                "Cubra com molho de tomate.",
                "Adicione queijos por cima.",
                "Asse no forno até gratinar.",
                "Cozinhe o arroz separadamente.",
                "Sirva o frango sobre o arroz.",
                "Tempere com sal e pimenta."
            ]
        },
        {
            "name": "Costela com Mandioca",
            "calories": 720,
            "protein": 45,
            "carbs": 55,
            "fat": 35,
            "time": "2 horas",
            "category": "Jantar",
            "ingredients": [
                "200g de costela bovina",
                "300g de mandioca",
                "Temperos para churrasco",
                "1 cebola",
                "Cerveja para marinar",
                "Sal grosso",
                "Pimenta do reino",
                "Alecrim"
            ],
            "recipe": [
                "Tempere a costela com sal grosso e temperos.",
                "Marine na cerveja por 1 hora.",
                "Cozinhe a mandioca até ficar macia.",
                "Grelhe a costela lentamente.",
                "Cozinhe por 1-2 horas até ficar macia.",
                "Sirva com mandioca cozida.",
                "Tempere com alecrim.",
                "Sirva bem quente."
            ]
        },
        {
            "name": "Lasanha de Berinjela",
            "calories": 450,
            "protein": 28,
            "carbs": 25,
            "fat": 28,
            "time": "40 min",
            "category": "Jantar",
            "ingredients": [
                "1 berinjela média",
                "100g de carne moída magra",
                "200ml de molho de tomate",
                "100g de queijo mussarela",
                "2 colheres de sopa de queijo parmesão",
                "1/2 cebola picada",
                "2 dentes de alho",
                "Sal, pimenta e orégano"
            ],
            "recipe": [
                "Corte a berinjela em fatias de 1cm.",
                "Grelhe as fatias de berinjela até dourar.",
                "Refogue cebola, alho e carne moída.",
                "Adicione molho de tomate e temperos.",
                "Em refratário, faça camadas alternadas.",
                "Comece com berinjela, carne e queijo.",
                "Finalize com mussarela e parmesão.",
                "Asse por 25 minutos a 180°C."
            ]
        },
        
        # LANCHE - GANHAR PESO
        {
            "name": "Mix de Castanhas",
            "calories": 380,
            "protein": 12,
            "carbs": 15,
            "fat": 32,
            "time": "1 min",
            "category": "Lanche",
            "ingredients": [
                "10 amêndoas",
                "5 nozes",
                "5 castanhas do Brasil",
                "10 castanhas de caju",
                "1 colher de sopa de uvas passas",
                "1 colher de chá de mel (opcional)"
            ],
            "recipe": [
                "Misture todas as castanhas em uma tigela.",
                "Adicione as uvas passas.",
                "Se desejar, regue levemente com mel.",
                "Misture bem todos os ingredientes.",
                "Sirva em porção individual.",
                "Conserve o restante em recipiente hermético."
            ]
        },
        {
            "name": "Vitamina de Banana com Aveia",
            "calories": 420,
            "protein": 18,
            "carbs": 58,
            "fat": 16,
            "time": "5 min",
            "category": "Lanche",
            "ingredients": [
                "1 banana média",
                "200ml de leite integral",
                "2 colheres de sopa de aveia",
                "1 colher de sopa de mel",
                "1 colher de chá de canela",
                "1 scoop de whey protein",
                "Gelo a gosto"
            ],
            "recipe": [
                "Adicione todos os ingredientes no liquidificador.",
                "Bata por 2-3 minutos até ficar cremoso.",
                "Ajuste a consistência com mais leite se necessário.",
                "Adicione gelo se preferir mais gelado.",
                "Sirva imediatamente em copo grande.",
                "Decore com canela por cima."
            ]
        },
        {
            "name": "Torrada de Abacate com Ovo e Amendoim",
            "calories": 480,
            "protein": 20,
            "carbs": 52,
            "fat": 24,
            "time": "3 min",
            "category": "Lanche",
            "ingredients": [
                "2 fatias de pão integral",
                "1 abacate maduro",
                "2 colheres de sopa de pasta de amendoim",
                "1 colher de sopa de mel",
                "1 colher de sopa de granola",
                "Suco de 1/2 limão",
                "Sal e pimenta"
            ],
            "recipe": [
                "Toste o pão integral até ficar dourado.",
                "Espalhe pasta de amendoim nas torradas.",
                "Amasse o abacate com limão, sal e pimenta.",
                "Espalhe o abacate sobre as torradas.",
                "Regue com mel por cima.",
                "Finalize com granola.",
                "Feche o sanduíche.",
                "Sirva imediatamente."
            ]
        },
        {
            "name": "Milkshake Proteico",
            "calories": 520,
            "protein": 28,
            "carbs": 48,
            "fat": 24,
            "time": "5 min",
            "category": "Lanche",
            "ingredients": [
                "200ml de sorvete de baunilha",
                "200ml de leite integral",
                "1 scoop de whey protein",
                "2 colheres de sopa de pasta de amendoim",
                "1 colher de sopa de mel",
                "Gelo a gosto"
            ],
            "recipe": [
                "Adicione todos os ingredientes no liquidificador.",
                "Bata por 2-3 minutos até ficar cremoso.",
                "Adicione gelo se preferir mais gelado.",
                "Sirva em copo grande.",
                "Decore com pasta de amendoim por cima.",
                "Consuma imediatamente."
            ]
        },
        {
            "name": "Chocolate 70% com Amêndoas",
            "calories": 350,
            "protein": 22,
            "carbs": 35,
            "fat": 16,
            "time": "3 min",
            "category": "Lanche",
            "ingredients": [
                "1 scoop de whey protein chocolate",
                "1 ovo",
                "2 colheres de sopa de farinha de aveia",
                "1 colher de chá de fermento",
                "200ml de leite",
                "1 colher de sopa de cacau em pó",
                "1 colher de sopa de mel"
            ],
            "recipe": [
                "Misture todos os ingredientes numa caneca.",
                "Mexa bem até formar uma massa homogênea.",
                "Coloque no microondas por 90 segundos.",
                "Deixe esfriar por 1 minuto.",
                "Sirva quente.",
                "Decore com cacau em pó por cima."
            ]
        }
    ]
}

# Funções de cálculo
def calculate_bmr(sex, age, weight, height):
    """Calculate Basal Metabolic Rate using Mifflin-St Jeor formula."""
    if sex == 'M':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:  # Female
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    return bmr

def calculate_tdee(bmr, activity_level):
    """Calculate Total Daily Energy Expenditure based on activity level."""
    activity_factors = {
        1: 1.2,    # Sedentary
        2: 1.375,  # Lightly active
        3: 1.55,   # Moderately active
        4: 1.725,  # Very active
        5: 1.9     # Extremely active
    }
    tdee = bmr * activity_factors[activity_level]
    return tdee

def adjust_for_goal(tdee, goal):
    """Adjust calories based on the user's goal."""
    if goal == "lose":
        calories = tdee * 0.8  # 20% reduction
    elif goal == "gain":
        calories = tdee * 1.15  # 15% increase
    else:  # maintain
        calories = tdee
    return calories

def calculate_macros(calories, weight):
    """Calculate macronutrient distribution."""
    # Protein: 2g per kg of body weight
    protein_grams = 2 * weight
    protein_calories = protein_grams * 4  # 4 calories per gram of protein
    
    # Fat: 25% of total calories
    fat_calories = calories * 0.25
    fat_grams = fat_calories / 9  # 9 calories per gram of fat
    
    # Carbohydrates: remaining calories
    carb_calories = calories - protein_calories - fat_calories
    carb_grams = carb_calories / 4  # 4 calories per gram of carbohydrate
    
    return protein_grams, fat_grams, carb_grams

def get_meal_suggestions(goal, target_calories, num_meals=3):
    """Get personalized meal suggestions based on goal and calories."""
    meals = MEALS_DATABASE.get(goal, MEALS_DATABASE["maintain"])
    calories_per_meal = target_calories / num_meals
    
    # Filter meals that fit within ±100 calories of target per meal
    suitable_meals = [meal for meal in meals if abs(meal["calories"] - calories_per_meal) <= 100]
    
    if not suitable_meals:
        # If no meals fit perfectly, get the closest ones
        suitable_meals = sorted(meals, key=lambda x: abs(x["calories"] - calories_per_meal))
    
    return random.sample(suitable_meals, min(num_meals, len(suitable_meals)))

def display_meal_card(meal):
    """Exibe um cartão de refeição com todos os detalhes."""
    with st.expander(f"🍽️ {meal['name']} - {meal['calories']} kcal", expanded=False):
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.write(f"**Categoria:** {meal['category']}")
            st.write(f"**Tempo de Preparação:** {meal['time']}")
            
            # Macros
            st.write("**Macronutrientes:**")
            col_macro1, col_macro2, col_macro3 = st.columns(3)
            with col_macro1:
                st.metric("Proteína", f"{meal['protein']}g")
            with col_macro2:
                st.metric("Hidratos", f"{meal['carbs']}g")
            with col_macro3:
                st.metric("Gordura", f"{meal['fat']}g")
        
        with col2:
            st.metric("Calorias", f"{meal['calories']}")
        
        # Ingredients
        st.write("**Ingredientes:**")
        for ingredient in meal['ingredients']:
            st.write(f"• {ingredient}")
        
        # Recipe
        st.write("**Modo de Preparação:**")
        for i, step in enumerate(meal['recipe'], 1):
            st.write(f"{i}. {step}")

# CSS para o header personalizado
def add_custom_css():
    st.markdown("""
    <style>
    .header-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem 2rem;
        margin: -1rem -1rem 2rem -1rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        border-radius: 0 0 12px 12px;
    }
    
    .header-content {
        display: flex;
        justify-content: space-between;
        align-items: center;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    .logo-section {
        display: flex;
        align-items: center;
        gap: 1rem;
    }
    
    .logo {
        width: 80px;
        height: 80px;
        border-radius: 50%;
        background: white;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2rem;
        font-weight: bold;
        color: #667eea;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    .brand-info h1 {
        color: white;
        font-size: 1.5rem;
        font-weight: bold;
        margin: 0;
    }
    
    .brand-info p {
        color: rgba(255, 255, 255, 0.9);
        font-size: 0.875rem;
        margin: 0;
    }
    
    .app-title {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        color: white;
        font-weight: 600;
        font-size: 1.1rem;
    }
    
    .dumbbell-icon {
        font-size: 1.5rem;
    }
    
    /* Melhorar o design dos cards */
    .main .block-container {
        padding-top: 2rem;
    }
    
    .stMetric {
        background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 1rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }
    
    .stExpander {
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
    }
    
    .stExpander > div {
        background: white;
        border-radius: 12px;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
    }
    
    .stSuccess {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        border: none;
        border-radius: 12px;
        color: white;
    }
    
    .stInfo {
        background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
        border: none;
        border-radius: 12px;
        color: white;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #f8fafc 0%, #e2e8f0 100%);
    }
    
    @media (max-width: 768px) {
        .header-content {
            flex-direction: column;
            gap: 1rem;
            text-align: center;
        }
        
        .logo-section {
            flex-direction: column;
            gap: 0.5rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)

def create_header():
    # Tenta carregar o logo, se não existir usa emoji
    import os
    logo_path = "assets/logo.png"
    
    if os.path.exists(logo_path):
        # Usar imagem do logo
        import base64
        with open(logo_path, "rb") as f:
            logo_data = base64.b64encode(f.read()).decode()
        
        st.markdown(f"""
        <div class="header-container">
            <div class="header-content">
                <div class="logo-section">
                    <div class="logo-image">
                        <img src="data:image/png;base64,{logo_data}" alt="Luis Ferreira Logo" style="width: 120px; height: 120px; object-fit: contain;">
                    </div>
                    <div class="brand-info">
                        <h1>Calculadora Fitness by Luís Ferreira 🍎</h1>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        # Fallback para emoji se imagem não existir
        st.markdown("""
        <div class="header-container">
            <div class="header-content">
                <div class="logo-section">
                    <div class="logo">💪</div>
                    <div class="brand-info">
                        <h1>Calculadora Fitness by Luís Ferreira 🍎</h1>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Interface principal
def main():
    # Adicionar CSS personalizado
    add_custom_css()
    
    # Criar header personalizado
    create_header()
    
    # Título principal
    st.markdown("### 👈🏽 Para fazeres magia, preenche as tuas informações do lado esquerdo")
    st.markdown("---")
    
    # Sidebar para informações pessoais
    with st.sidebar:
        st.header("📊 As Tuas Informações")
        
        sex = st.selectbox("Sexo", ["M", "F"], help="M para Masculino, F para Feminino")
        age = st.number_input("Idade (anos)", min_value=1, max_value=120, value=25)
        weight = st.number_input("Peso (kg)", min_value=1.0, max_value=500.0, value=70.0, step=0.1)
        height = st.number_input("Altura (cm)", min_value=50.0, max_value=300.0, value=170.0, step=0.1)
        
        activity_level = st.selectbox(
            "Nível de Actividade",
            [1, 2, 3, 4, 5],
            format_func=lambda x: {
                1: "Sedentário (pouco ou nenhum exercício)",
                2: "Ligeiramente activo (exercício leve 1-3 dias/semana)",
                3: "Moderadamente activo (exercício moderado 3-5 dias/semana)",
                4: "Muito activo (exercício intenso 6-7 dias/semana)",
                5: "Extremamente activo (exercício muito intenso, trabalho físico)"
            }[x]
        )
        
        goal = st.selectbox("Objectivo", ["lose", "maintain", "gain"], 
                          format_func=lambda x: {
                              "lose": "Perder peso",
                              "maintain": "Manter peso", 
                              "gain": "Ganhar peso"
                          }[x])
        
        calculate_button = st.button("🧮 Calcular as Minhas Calorias", type="primary")
    
    # Cálculos e resultados
    if calculate_button:
        # Calculate BMR
        bmr = calculate_bmr(sex, age, weight, height)
        
        # Calculate TDEE
        tdee = calculate_tdee(bmr, activity_level)
        
        # Adjust for goal
        daily_calories = adjust_for_goal(tdee, goal)
        
        # Calculate macronutrients
        protein_grams, fat_grams, carb_grams = calculate_macros(daily_calories, weight)
        
        # Store results in session state
        st.session_state.calculated = True
        st.session_state.results = {
            'bmr': bmr,
            'tdee': tdee,
            'daily_calories': daily_calories,
            'protein': protein_grams,
            'fat': fat_grams,
            'carbs': carb_grams,
            'goal': goal
        }
    
    # Display results if calculated
    if st.session_state.get('calculated', False):
        results = st.session_state.results
        
        st.success("🎯 As Tuas Recomendações Calóricas Diárias")
        
        # Métricas principais
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Calorias Diárias", f"{results['daily_calories']:.0f}")
        with col2:
            st.metric("TMB", f"{results['bmr']:.0f}")
        with col3:
            st.metric("TDEE", f"{results['tdee']:.0f}")
        with col4:
            objetivo_label = {
                'lose': 'Perder',
                'maintain': 'Manter',
                'gain': 'Ganhar'
            }[results['goal']]
            st.metric("Objectivo", objetivo_label)
        
        # Gráfico de macros
        st.subheader("📊 Distribuição de Macronutrientes")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Proteína", f"{results['protein']:.1f} g")
        with col2:
            st.metric("Gordura", f"{results['fat']:.1f} g")
        with col3:
            st.metric("Hidratos de Carbono", f"{results['carbs']:.1f} g")
        
        # Sugestões de refeições
        st.subheader("🍽️ Sugestões de Refeições Personalizadas")
        objetivo_text = {
            'lose': 'perder',
            'maintain': 'manter',
            'gain': 'ganhar'
        }[results['goal']]
        st.write(f"Baseado no teu objectivo de **{objetivo_text}** peso e **{results['daily_calories']:.0f}** calorias diárias")
        
        # Get meal suggestions
        suggested_meals = get_meal_suggestions(results['goal'], results['daily_calories'])
        
        # Display meals
        for meal in suggested_meals:
            display_meal_card(meal)
        
        # Dica do personal trainer
        st.info("💡 **Dica do Personal Trainer:** " + {
            'lose': "Para perda de peso, foca em proteínas magras e vegetais. Bebe bastante água e mantém consistência.",
            'maintain': "Para manutenção, equilibra bem os macronutrientes e pratica exercícios regulares.",
            'gain': "Para ganho de peso, aumenta gradualmente as calorias e combina com treino de força."
        }[results['goal']])
        
        # Botão para gerar novas sugestões
        if st.button("🔄 Gerar Novas Sugestões de Refeições"):
            st.rerun()
    
    # Footer personalizado
    create_footer()

def create_footer():
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 2rem 0; background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%); margin: 2rem -1rem -1rem -1rem; border-radius: 12px 12px 0 0;">
        <div style="display: flex; justify-content: center; align-items: center; gap: 1rem; margin-bottom: 1rem;">
            <div style="width: 40px; height: 40px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 1.2rem;">💪</div>
            <div>
                <h3 style="margin: 0; color: #1f2937; font-size: 1.1rem;">Luis Ferreira</h3>
                <p style="margin: 0; color: #6b7280; font-size: 0.9rem;">Personal Trainer</p>
            </div>
        </div>
        <p style="color: #6b7280; font-size: 0.9rem; margin: 0;">
            Desenvolvido com ❤️ para te ajudar a alcançar os teus objectivos fitness
        </p>
        <p style="color: #9ca3af; font-size: 0.8rem; margin: 0.5rem 0 0 0;">
            © 2024 - Todos os direitos reservados
        </p>
    </div>
    """, unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    main()