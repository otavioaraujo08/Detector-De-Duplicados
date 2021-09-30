import pandas as pd


# Classe Principal
class DetectDuplicator:
    # Instanciando variaveis
    def __init__(self):
        self.file_name = ""
        self.data_frame = None

    # Verificando se o formato do arquivo é xlsx, caso não seja adicionar um format no final do arquivo
    def open_excel(self, fn):
        if ".xlsx" not in fn:
            fn += ".xlsx"
        self.file_name = fn
        self.data_frame = pd.read_excel(self.file_name, sheet_name=0)

        # Caso Possua uma Coluna "CONSOLIDADO", Remover o "JA LANCADO"
        try:
            self.data_frame.columns = [x.upper() for x in self.data_frame.columns]

            index_names = self.data_frame[self.data_frame["CONSOLIDADO"] == "JA LANCADO"].index
            self.data_frame.drop(index_names, inplace=True)
        # Caso Não Possua A Coluna "Consolidado"
        except:
            print("Não há (CONSOLIDADO) nesse Arquivo !")

    # Recebendo os valores de Colunas
    def get_columns(self):
        return list(self.data_frame.columns)

    # Recebendo os Valores Chaves para receber filtro e V
    def filter_duplicated(self, columns_to_filter):
        # Configurando as variaveis para serem comparadas
        dup_index = self.data_frame.duplicated(subset=columns_to_filter, keep=False)

        # Caso a coluna duplicado não exista, criar uma nova coluna duplicado com todos os valores como não.
        if "DUPLICADO" not in self.data_frame:
            self.data_frame = self.data_frame.assign(DUPLICADO="NAO")

        # Ira pegar todas as linhas retornadas da função duplicated e ira escrever "Sim" na coluna duplicado
        self.data_frame.loc[(dup_index), 'DUPLICADO'] = 'SIM'

    # Caso não seja uma entensão em formato excel, renomear para um
    def export_excel(self, name):
        if ".xlsx" not in name:
            name += ".xlsx"
        self.data_frame.to_excel(name, index_label=False, index=False)
