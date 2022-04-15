import sqlite3


class CadastraUsuario:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()
    
    def inserir(self, nome, tell, cpf, email):
        consulta = "INSERT OR IGNORE INTO clientes (nome, telefone, cpf, email) VALUES (?, ?, ?, ?)"
        self.cursor.execute(consulta, (nome, tell, cpf, email))
        self.conn.commit()

    def editar(self, id, nome, tell, email):
        consulta = "UPDATE OR IGNORE clientes SET nome=?, telefone=?, email=? WHERE id=?"
        self.cursor.execute(consulta, (nome, tell, email, id))
        self.conn.commit()

    def excluir(self, id):
        consulta = "DELETE FROM clientes WHERE id=?"
        self.cursor.execute(consulta, (id,))
        self.conn.commit()
    
    def buscar(self, valor):
        consulta = "SELECT * FROM clientes WHERE nome LIKE ?"
        self.cursor.execute(consulta, (f'%{valor}%',))

        for people in self.cursor.fetchall():
            id, nome, tell, cpf, email = people

            print(f"\tID: {id}  NAME: {nome}  TELEPHONE: {tell}  CPF: {cpf}  E-MAIL: {email}")

    def listar(self):
        self.cursor.execute("SELECT * FROM clientes")

        for value in self.cursor.fetchall():
            id, nome, telefone, cpf, email = value
            
            print(f"\tID: {id}  NAME: {nome}  TELEPHONE: {telefone}  CPF: {cpf}  E-MAIL: {email}")

    def fechar(self):
        self.cursor.close()
        self.conn.close()


if __name__ == "__main__":
    cadastro = CadastraUsuario("basededados.db")
    cadastro.inserir("Leandro Leonardo", "11 9 1111-2222", "15560349542", "leandro.leo@gmail.com")
    cadastro.inserir("Teste do Teste", "14 9 3333-4444", "51545372896", "teste@teste.com.br")

