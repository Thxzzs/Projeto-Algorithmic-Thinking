import csv
import os

class Imovel:
    def __init__(self, tipo, quartos, garagem=False, vagas_estudio=0, possui_criancas=True):
        self.tipo = tipo.lower()
        self.quartos = quartos
        self.garagem = garagem
        self.vagas_estudio = vagas_estudio
        self.possui_criancas = possui_criancas
        self.valor_base = self.definir_valor_base()
        self.valor_final = self.calcular_valor_final()

    def definir_valor_base(self):
        if self.tipo == "apartamento":
            return 700.0
        elif self.tipo == "casa":
            return 900.0
        elif self.tipo == "estudio":
            return 1200.0
        else:
            raise ValueError("Tipo de imóvel inválido")

    def calcular_valor_final(self):
        valor = self.valor_base
        if self.tipo == "apartamento" and self.quartos == 2:
            valor += 200
        elif self.tipo == "casa" and self.quartos == 2:
            valor += 250
        if self.tipo in ["apartamento", "casa"] and self.garagem:
            valor += 300
        if self.tipo == "estudio" and self.vagas_estudio > 0:
            if self.vagas_estudio >= 2:
                valor += 250 + (self.vagas_estudio - 2) * 60
            else:
                valor += self.vagas_estudio * 125
        if self.tipo == "apartamento" and not self.possui_criancas:
            valor *= 0.95
        return valor

    def gerar_csv_parcelas(self, valor_contrato=2000, parcelas=5):
        nome_arquivo = f"orcamento_{self.tipo}.csv"
        caminho = r"C:\Users\mathe\OneDrive\Área de Trabalho"
        caminho_completo = os.path.join(caminho, nome_arquivo)
        parcelas_mensais = [round((valor_contrato / parcelas), 2)] * parcelas
        aluguel_anual = [round(self.valor_final, 2)] * 12
        with open(caminho_completo, "w", newline="") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(["Mês", "Aluguel (R$)", "Parcela do Contrato (R$)"])
            for i in range(12):
                parcela = parcelas_mensais[i % parcelas]
                escritor.writerow([f"Mês {i+1}", aluguel_anual[i], parcela])
        print(f"Arquivo salvo em: {caminho_completo}")

    def __str__(self):
        return (
            f"Tipo: {self.tipo.capitalize()}\n"
            f"Quartos: {self.quartos}\n"
            f"Garagem: {'Sim' if self.garagem else 'Não'}\n"
            f"Crianças: {'Sim' if self.possui_criancas else 'Não'}\n"
            f"Valor final mensal: R$ {self.valor_final:.2f}"
        )

def main():
    print("=== Sistema de Orçamento R.M Imobiliária ===")
    tipo = input("Tipo do imóvel (Apartamento / Casa / Estudio): ").strip()
    quartos = int(input("Número de quartos: "))
    possui_criancas = input("Possui crianças? (s/n): ").lower() == 's'
    garagem = False
    vagas_estudio = 0

    if tipo.lower() in ["apartamento", "casa"]:
        garagem = input("Deseja garagem? (s/n): ").lower() == 's'
    elif tipo.lower() == "estudio":
        vagas_estudio = int(input("Quantas vagas de estacionamento deseja? "))

    imovel = Imovel(tipo, quartos, garagem, vagas_estudio, possui_criancas)
    print("\nResumo do orçamento:")
    print(imovel)
    imovel.gerar_csv_parcelas()

if __name__ == "__main__":
    main()
