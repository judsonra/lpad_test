# LDAP/LDAPS Connectivity Test

[Português Brasil](README.pt-BR.md)

## Purpose

This project contains a small Python script, `ldap_test.py`, used to test LDAP or LDAPS connectivity with the `ldap3` library.

The script:

- Connects to an LDAP or LDAPS server.
- Performs a bind using the configured user credentials.
- Optionally runs an LDAP search.
- Prints the matching entries.
- Closes the connection.

## Requirements

- Python 3
- `ldap3`

Install the required package:

```bash
pip install ldap3
```

## Configuration

Edit the configuration variables at the top of `ldap_test.py` before running the script:

```python
use_ssl = True
host = "127.0.0.1"
port = 6636 if use_ssl else 389

user_dn = "usuario@domino.com"
password = "Evermat@2026"

base_dn = "DC=dominio,DC=local"
search_filter = "(objectClass=person)"
```

Configuration details:

- `use_ssl`: set to `True` to use LDAPS, usually port `636`; set to `False` to use LDAP, usually port `389`.
- `host`: LDAP server hostname or IP address.
- `port`: LDAP or LDAPS port. The current script uses `6636` when SSL is enabled and `389` otherwise.
- `user_dn`: user DN or login name used for bind authentication.
- `password`: password for the bind user.
- `base_dn`: LDAP base DN used for the search.
- `search_filter`: LDAP search filter. Set it to `None` or an empty value if you do not want to run a search.

## LDAPS Certificate Validation

When `use_ssl` is enabled, the script creates a TLS configuration with:

```python
validate=ssl.CERT_REQUIRED
```

This means the server certificate must be valid and trusted by the local system. For temporary testing only, you can change it to:

```python
validate=ssl.CERT_NONE
```

Do not disable certificate validation in production environments.

## Running

Run the script with:

```bash
python ldap_test.py
```

Depending on your system, you may need to use:

```bash
python3 ldap_test.py
```

## Expected Output

On a successful connection and bind, the script prints messages similar to:

```text
[INFO] Conectando ao servidor 127.0.0.1:6636 (SSL=True)
[OK] Bind realizado com sucesso!
```

If `search_filter` is configured, the script also prints:

```text
[INFO] Executando busca com filtro: (objectClass=person)
[INFO] Total de entradas encontradas: N
```

If the connection, bind, TLS validation, or search fails, the script prints:

```text
[ERRO] Falha na conexão LDAP/LDAPS
```

followed by the Python exception message.

## Security Notes

Do not commit real usernames, passwords, or production server details to the repository.

For production or shared environments, prefer using environment variables, a secrets manager, or a local configuration file ignored by Git.
