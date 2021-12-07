class Cadastro():

    def __init__(self,nome,cnpj,endereco=list):
        self.__nome=nome
        self.__cnpj=cnpj
        self.__endereco=endereco

        self.lista1=[]
        self.listaname=[]
        self.lista2=[]
        self.listaest=[]
        self.listaprod=[]

    def add_lista1(self,valor):
        self.lista1.reverse()
        self.lista1.append(valor)
        self.lista1.reverse()

        return self.lista1

    def add_listaname(self, valor):
        self.listaname.reverse()
        self.listaname.append(valor)
        self.listaname.reverse()

        return self.listaname

    def add_lista2(self, valor):
        self.lista2.reverse()
        self.lista2.append(valor)
        self.lista2.reverse()

        return self.lista2

    def add_listaest(self, valor):
        self.listaest.reverse()
        self.listaest.append(valor)
        self.listaest.reverse()

        return self.listaest

    def add_listaprod(self, valor):
        self.listaprod.reverse()
        self.listaprod.append(valor)
        self.listaprod.reverse()

        return self.listaprod

    def ultimas_req(self):
        print("As ultimas requisições da {} foram:".format(self.__nome))
        self.lista1
        self.lista2
        self.listaest
        self.listaprod
        self.listaname

        print("nome           |Direct id| Data   | Estimate (latam,br) | Produtos")

        a=len(self.lista1)
        i=0
        while i<a:
            print("{}          |{}|{}   | {} |{} ".format(self.listaname[i],self.lista1[i],self.lista2[i],self.listaest[i],self.listaprod[i]))
            i=i+1

    @property
    def nome(self):
        return self.__nome
    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self,endereco):
        self.__endereco=endereco

    @staticmethod
    def codigo_comprador(a):
        codigo={'Brastemp.SA':'001','Americanas S.A':'002', 'CEMIG':'003'}
        return codigo[a]

    pass

############################################
conta=Cadastro("CEMIG","000000000789",["Rua das palmeiras, 0 Belo Horizonte","Av. dos Inconfidentes, 45 Belo Horizonte"])

class Requisicao():
    def __init__(self,directid,directname,data,cadastro,estimsteid=list,produtos=list):
        self.__directid=directid
        self.__directname=directname
        self.__estimateid+estimsteid
        self.__data=data
        self.__produtos=produtos
        self.__quantidade={}
        for valor in self.__produtos:
            b=int(input("Digite a quantidade de {} pedido:".format(valor)))
            self.__quantidade[valor]=b

        self.__cadastro=cadastro
        self.billto=self.bill_to(cadastro.endereco)
        self.shipto=self.ship_to(cadastro.endereco)


        #criar lista com as requisições

        cadastro._Cadastro__listaname=cadastro.add_listaname(self.__directname)
        cadastro._Cadastro__lista1 = cadastro.add_lista1(self.__directid)
        cadastro._Cadastro__lista2 = cadastro.add_lista2(self.__data)
        cadastro._Cadastro__listaest = cadastro.add_listaest(self.__estimateid)
        cadastro._Cadastro__listaprod = cadastro.add_listaprod(self.__quantidade)

    def imprimequant(self):
        return self.__quantidade

    def bill_to(self,l=list):
        a=len(l)
        i=0
        while i<a:
            print("{}-{}".format(i,l[i]))
            i=i+1
        b=int(input("Digite qual é o numero referente ao endereço de bill to"))
        bill=l[b]
        return bill

    def ship_to(self,l=list):
        a=len(l)
        i=0
        while i<a:
            print("{}-{}".format(i,l[i]))
            i=i+1
        s=int(input("Digite qual é o numero referente ao endereço de bship to"))
        ship=l[s]
        return ship

    @property
    def directname(self):
        return self.__directname

    @property
    def data(self):
        return self.__data

    @property
    def directid(self):
        return self.__directid

    @property
    def estimateid(self):
        return self.__estimateid

    @staticmethod
    def leadtime(a):
        tempo={'Switch C9200L-48P':'136 dias', 'Switch C9200-48P':'160 dias'}
        return tempo[a]


primreq=Requisicao("7890345","CEMIG","12/12/1989",conta,['245361s'],["Switch C9200L-48P"])

