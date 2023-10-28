use bdestoqueloja

select * from produtos;

select nome from fornecedores;

select * from CategoriasDeProdutos;

select * from Produtos where Fornecedor = 2;

select * from Produtos where Preco > 5;

select * from itensdevenda where IddoProduto = 1;

select * from Vendas inner join ItensDeVenda; 
select * from Vendas V inner join ItensDeVenda IV;
select * from Vendas V inner join ItensDeVenda IV 
on V.ID = IV.IDDaVenda;
select * from Vendas V inner join ItensDeVenda IV 
on V.ID = IV.IDDaVenda where IV.IDDoProduto = 2;
    
select SUM(QuantidadeEmEstoque * Preco) from Produtos;   

select Categoria, SUM(QuantidadeEmEstoque * Preco) from Produtos
group by Categoria;

select * from Produtos where Categoria = 2;

select * from Vendas where Funcionario = "Maria Santos";

select * from ItensDeVenda iv
inner join Produtos p on iv.IDDoProduto = p.ID
where iv.IDDaVenda = 1; 
    
SELECT * from fornecedores INNER JOIN produtos;
SELECT * from Fornecedores f INNER JOIN Produtos p
SELECT * from Fornecedores f INNER JOIN Produtos p ON f.ID = p.Fornecedor;
SELECT * from Fornecedores f INNER JOIN Produtos p ON f.ID = p.Fornecedor GROUP BY f.ID;
SELECT * from Fornecedores f INNER JOIN Produtos p ON f.ID = p.Fornecedor GROUP BY f.ID
HAVING p.QuantidadeEmEstoque > 10;