# RoadmadSH-Chinook-database
Trabalho colaborativo roadmap.sh py, sqllite
URL do projeto 
```https://roadmap.sh/projects/querying-sql-python```




## Requisitos do projeto

Baixe o arquivo de banco de dados Chinook e conecte-se a ele usando sqlite3a biblioteca do Python.
Explore o esquema do banco de dados: identifique todas as tabelas e seus relacionamentos.
Escreva consultas SQL para responder às seguintes perguntas:

1- Quais são as 10 músicas mais vendidas?

2- Qual país gera a maior receita?

3- Quem é o funcionário de vendas com melhor desempenho?

Carregar resultados de consulta em DataFrames do Pandas
Visualize pelo menos um resultado com um gráfico de barras.


1- Quais são as 10 músicas mais vendidas?
```sql
select sum(IL.Quantity) as coun, t.Name, t.TrackId from Track t
inner join InvoiceLine IL on t.trackId = IL.TrackId 
GROUP by t.Name
order by coun DESC
limit 10
```

2- Qual país gera a maior receita?

```sql
SELECT i.BillingCountry as pais, SUM(i.Total)as Total FROM Invoice i 
GROUP by i.BillingCountry
order by total DESC
limit 1
```

3- Quem é o funcionário de vendas com melhor desempenho?

```sql
SELECT  COUNT(DISTINCT i.CustomerId) as customer, SUM(i.Total)as Total, 
c.supportrepid as suporte, e.FirstName
from Customer c
inner join Employee e on c.SupportRepId = e.EmployeeId
inner join Invoice i on c.CustomerId = i.CustomerId
GROUP by c.SupportRepId, e.FirstName
```

4- Valor médio de venda por cliente por funcionário - BONUS

```sql
SELECT  COUNT(DISTINCT i.CustomerId) as customer, SUM(i.Total)as Total, sum(i.Total)/count(DISTINCT i.CustomerId) as media,
c.supportrepid as suporte, e.FirstName
from Customer c
inner join Employee e on c.SupportRepId = e.EmployeeId
inner join Invoice i on c.CustomerId = i.CustomerId
GROUP by c.SupportRepId, e.FirstName
```