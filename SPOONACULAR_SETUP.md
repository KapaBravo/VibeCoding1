# 🔐 Configuração Segura da Spoonacular API

## ⚠️ IMPORTANTE: Segurança da API Key

**NUNCA partilhes a tua API key publicamente!**

## 📝 Passos para Configurar

### 1. Criar o ficheiro `.env`

```bash
# Na raiz do projeto, cria o ficheiro .env
cp .env.example .env
```

### 2. Adicionar a tua API Key

Abre o ficheiro `.env` (NÃO o `.env.example`) e adiciona a tua chave:

```
SPOONACULAR_API_KEY=a1b2c3d4e5f6g7h8i9j0  # ← SUBSTITUI isto pela tua chave real
```

### 3. Verificar que está no .gitignore

O ficheiro `.env` já está no `.gitignore`, então **nunca** será enviado para o GitHub.

✅ Seguro: `.env` (este fica local, nunca vai para o GitHub)
❌ Não edites: `.env.example` (este é só um modelo)

## 🚀 Como Usar

### Testar a API localmente:

```bash
# Instalar dependências
pip install -r requirements.txt

# Executar script de teste
python spoonacular_helper.py
```

### Procurar receitas:

```python
from spoonacular_helper import SpoonacularAPI

# Inicializar
api = SpoonacularAPI()

# Procurar receitas
recipes = api.search_recipes("grilled chicken")

# Ver detalhes
for recipe in recipes:
    print(recipe['title'])
```

## 📊 Funcionalidades Disponíveis

### 1. `search_recipes(query, diet, max_results)`
Procura receitas por nome

### 2. `get_recipe_nutrition(recipe_id)`
Obtém dados nutricionais precisos

### 3. `get_recipe_details(recipe_id)`
Obtém receita completa (ingredientes, instruções, imagens)

### 4. `format_recipe_for_app(recipe_data)`
Formata dados para o formato da tua app

## 🎯 Próximos Passos

1. ✅ Criaste conta na Spoonacular
2. ✅ Obtiveste a API key
3. ✅ Criaste o ficheiro `.env`
4. ⏳ Adicionaste a chave ao `.env`
5. ⏳ Testaste com `python spoonacular_helper.py`
6. ⏳ Vamos atualizar as receitas da app!

## 💡 Dicas de Segurança

- 🔒 **NUNCA** partilhes a API key em chat, email, ou código
- 🔒 **NUNCA** faças commit do ficheiro `.env`
- 🔒 Verifica sempre o `.gitignore` antes de fazer push
- 🔒 Se acidentalmente expuseres a chave, gera uma nova imediatamente

## 🆘 Problemas Comuns

### "SPOONACULAR_API_KEY não encontrada"
→ Certifica-te que criaste o `.env` e adicionaste a chave

### "API key inválida"
→ Verifica se copiaste a chave completa sem espaços

### "Limite de requests excedido"
→ Plano gratuito: 150 requests/dia. Gere com cuidado!

## 📚 Links Úteis

- [Documentação Spoonacular](https://spoonacular.com/food-api/docs)
- [Dashboard (ver uso)](https://spoonacular.com/food-api/console)
- [Preços e Limites](https://spoonacular.com/food-api/pricing)

