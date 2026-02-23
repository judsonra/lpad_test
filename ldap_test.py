from ldap3 import Server, Connection, ALL, Tls
import ssl

# ==========================
# CONFIGURAÇÕES
# ==========================

use_ssl = True  # True para LDAPS (ex: 636), False para LDAP (ex: 389)
host = "127.0.0.1"
port = 6636 if use_ssl else 389

user_dn = "usuario@domino.com"
password = "Evermat@2026"

base_dn = "DC=dominio,DC=local"
search_filter = "(objectClass=person)"  # Pode alterar ou deixar None

# ==========================
# CONEXÃO
# ==========================

try:
    if use_ssl:
        tls_configuration = Tls(
            validate=ssl.CERT_REQUIRED,  # Altere para CERT_NONE para ignorar validacao certificado valor default CERT_REQUIRED
            version=ssl.PROTOCOL_TLSv1_2
        )
        server = Server(host, port=port, use_ssl=True, get_info=ALL, tls=tls_configuration)
    else:
        server = Server(host, port=port, use_ssl=False, get_info=ALL)

    print(f"[INFO] Conectando ao servidor {host}:{port} (SSL={use_ssl})")

    conn = Connection(server, user=user_dn, password=password, auto_bind=True)

    print("[OK] Bind realizado com sucesso!")

    # ==========================
    # PESQUISA LDAP (opcional)
    # ==========================

    if search_filter:
        print(f"[INFO] Executando busca com filtro: {search_filter}")
        
        conn.search(
            search_base=base_dn,
            search_filter=search_filter,
            attributes=['cn', 'distinguishedName']
        )

        print(f"[INFO] Total de entradas encontradas: {len(conn.entries)}")
        
        for entry in conn.entries:
            print(entry)

    conn.unbind()
    print("[INFO] Conexão encerrada com sucesso.")

except Exception as e:
    print("[ERRO] Falha na conexão LDAP/LDAPS")
    print(str(e))
