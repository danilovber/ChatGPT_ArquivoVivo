# Cálculo teste t

**ID:** `673481ec-c2c0-8012-b19b-4e710e076950`
**Criado (America/Sao_Paulo):** 2024-11-13 07:39:40 -03

---

**Usuário — 2024-11-13 07:39:40 -03**
Chat, pode realizar o cálculo deste script:
from scipy.stats import ttest_ind
import numpy as np

# Dados dos dois conjuntos
grupo1 = np.array([71.0, 85.0, 69.4, 67.5, 69.8, 59.1, 91.8, 87.1])
grupo2 = np.array([72.2, 76.9, 70.9])

# Estatísticas básicas dos grupos
media_grupo1 = np.mean(grupo1)
media_grupo2 = np.mean(grupo2)
var_grupo1 = np.var(grupo1, ddof=1)  # variância amostral
var_grupo2 = np.var(grupo2, ddof=1)

# Teste t de Student para amostras independentes
t_stat, p_value = ttest_ind(grupo1, grupo2, equal_var=False)

media_grupo1, var_grupo1, media_grupo2, var_grupo2, t_stat, p_value

**Chat — 2024-11-13 07:39:54 -03**
_(mensagem vazia)_

**Chat — 2024-11-13 07:39:54 -03**
75a48806-7403-461f-9b61-ea95906e7171
finished_successfully
python

**Chat — 2024-11-13 07:39:54 -03**
Parece que não consigo realizar uma análise de dados avançada neste momento. Por favor, tente novamente mais tarde, e estarei pronto para ajudar! Se precisar, também posso fornecer orientações sobre como rodar o script em seu próprio ambiente Python.

**Usuário — 2024-11-13 07:46:45 -03**
Você pode realizar está análise?

**Chat — 2024-11-13 07:46:55 -03**
85621938-07df-4edf-a2fb-1163b54b48ac
finished_successfully
python

**Chat — 2024-11-13 07:46:55 -03**
Parece que não consigo realizar a análise de dados no momento. Por favor, tente novamente mais tarde, ou, se preferir, posso orientá-lo a executar o script em um ambiente Python próprio.
