# Boxplot lado a lado

**ID:** `67358659-672c-8012-b998-01ddac06182e`
**Criado (America/Sao_Paulo):** 2024-11-14 02:10:49 -03

---

**Usuário — 2024-11-14 02:10:49 -03**
Olá Chat, boa noite, como vai?
Chat, gostaria de um código do R para gerar dois boxplots, o primeiro azul e o segundo vermelho, em uma mesma figura, lado-a-lado. Pode fazer?

**Chat — 2024-11-14 02:11:05 -03**
_(mensagem vazia)_

**Chat — 2024-11-14 02:11:05 -03**
Boa noite, Danilo! Vou bem, obrigado! E você?

Claro, posso te ajudar com o código em R para gerar dois boxplots lado a lado, um azul e outro vermelho. Vou criar um exemplo simples para ilustrar, usando dados aleatórios para os dois conjuntos. 

Aqui está o código:

```r
# Gerando dados de exemplo
set.seed(123) # Para reprodutibilidade
dados1 <- rnorm(50, mean = 5, sd = 1)  # Dados para o primeiro boxplot
dados2 <- rnorm(50, mean = 7, sd = 1.5) # Dados para o segundo boxplot

# Criando um data frame para facilitar o plot
dados <- data.frame(
  valores = c(dados1, dados2),
  grupo = factor(rep(c("Grupo 1", "Grupo 2"), each = 50))
)

# Plotando os boxplots lado a lado com cores diferentes
boxplot(valores ~ grupo, data = dados, 
        col = c("blue", "red"), # Cores: azul para o primeiro, vermelho para o segundo
        main = "Comparação entre Grupos",
        ylab = "Valores",
        xlab = "Grupos")
```

Esse código cria dois boxplots, onde os dados de `Grupo 1` ficam em azul e os de `Grupo 2` ficam em vermelho, ambos lado a lado em uma mesma figura. A legenda e o título são personalizados para indicar os grupos e os valores.

Se precisar de algum ajuste, é só me avisar!
