# Teste de Conectividade LDAP/LDAPS

[English](README.md)

## Objetivo

Este projeto contém um pequeno script Python, `ldap_test.py`, usado para testar conectividade LDAP ou LDAPS com a biblioteca `ldap3`.

O script:

- Conecta a um servidor LDAP ou LDAPS.
- Executa um bind usando as credenciais configuradas.
- Opcionalmente executa uma busca LDAP.
- Exibe as entradas encontradas.
- Encerra a conexão.

## Requisitos

- Python 3
- `ldap3`

Instale o pacote necessário:

```bash
pip install ldap3
```

## Configuração

Edite as variáveis de configuração no início do arquivo `ldap_test.py` antes de executar o script:

```python
use_ssl = True
host = "127.0.0.1"
port = 6636 if use_ssl else 389

user_dn = "usuario@domino.com"
password = "Evermat@2026"

base_dn = "DC=dominio,DC=local"
search_filter = "(objectClass=person)"
```

Detalhes da configuração:

- `use_ssl`: use `True` para LDAPS, normalmente porta `636`; use `False` para LDAP, normalmente porta `389`.
- `host`: nome DNS ou endereço IP do servidor LDAP.
- `port`: porta LDAP ou LDAPS. O script atual usa `6636` quando SSL está habilitado e `389` caso contrário.
- `user_dn`: DN do usuário ou nome de login usado na autenticação bind.
- `password`: senha do usuário usado no bind.
- `base_dn`: base DN LDAP usada na busca.
- `search_filter`: filtro de busca LDAP. Defina como `None` ou deixe sem valor se não quiser executar uma busca.

## Validação de Certificado LDAPS

Quando `use_ssl` está habilitado, o script cria uma configuração TLS com:

```python
validate=ssl.CERT_REQUIRED
```

Isso significa que o certificado do servidor precisa ser válido e confiável para o sistema local. Apenas para testes temporários, você pode alterar para:

```python
validate=ssl.CERT_NONE
```

Não desabilite a validação de certificado em ambientes de produção.

## Execução

Execute o script com:

```bash
python ldap_test.py
```

Dependendo do seu sistema, pode ser necessário usar:

```bash
python3 ldap_test.py
```

## Saída Esperada

Em uma conexão e bind bem-sucedidos, o script exibe mensagens semelhantes a:

```text
[INFO] Conectando ao servidor 127.0.0.1:6636 (SSL=True)
[OK] Bind realizado com sucesso!
```

Se `search_filter` estiver configurado, o script também exibe:

```text
[INFO] Executando busca com filtro: (objectClass=person)
[INFO] Total de entradas encontradas: N
```

Se ocorrer falha na conexão, bind, validação TLS ou busca, o script exibe:

```text
[ERRO] Falha na conexão LDAP/LDAPS
```

seguido pela mensagem de exceção do Python.

## Notas de Segurança

Não faça commit de usuários, senhas ou dados reais de servidores de produção no repositório.

Para ambientes de produção ou compartilhados, prefira usar variáveis de ambiente, um gerenciador de segredos ou um arquivo de configuração local ignorado pelo Git.
